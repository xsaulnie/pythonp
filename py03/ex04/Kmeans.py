import numpy as np
import sys
import random
import os
import matplotlib.pyplot as plt


class CsvReader():
    def __init__(self, filename=None, sep=',', header=False, skip_top=0, skip_bottom=0):
        try:
            fi = open(filename, "r")
        except:
            print(f"Error on opening '{filename}' file")
            self.error_file = True
            return

        if os.stat(filename).st_size == 0:
            print(f"Error file {filename} is empty")
            self.error_file = True
            return
        
        self.error_file = False
        self.fi = fi
        if (self.check_corruption(self.fi, sep, header)):
            self.corrupted = True
            print("corrupted")
            return

        self.filename = filename
        self.sep = sep
        self.header = header
        self.skip_top = skip_top
        self.skip_bottom = skip_bottom
        self.corrupted = False

    def __enter__(self):

        if (self.error_file or self.corrupted):
            return None

        return (self)
    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type is not None:
            print(f"Error CsvReader {exc_type} {exc_val}")
            return True
        elif not self.error_file:
            self.fi.close()
    def getdata(self):
        """ Retrieves the data/records from skip_top to skip bottom.
        Return:
        nested list (list(list, list, ...)) representing the data.
        """
        ret = []
        cur = 0

        if (self.header == True):
            self.fi.readline()

        for x in range(self.skip_top):
            self.fi.readline()

        body = self.fi.read()

        all_line = body.strip('\n').split('\n')

        if (self.skip_bottom != 0):
            all_line[:] = all_line[:-self.skip_bottom]
        for line in all_line:
            splitline = line.split(self.sep)
            elem = [el.strip(' \"\n') for el in splitline]
            ret.append(elem)

        self.fi.seek(0, 0)
        return (ret)

    def getheader(self):
        """ Retrieves the header from csv file.
        Returns:
        list: representing the data (when self.header is True).
        None: (when self.header is False).
        """

        if (self.header == False):
            return None

        line = self.fi.readline()

        ret = line.split(self.sep)
        ret = [label.strip(' \"\n') for label in ret]

        self.fi.seek(0, 0)

        return (ret)

    def check_corruption(self, fi, sep, head):
        full_split = []
        try:
            all_body = fi.read()
        except:
            self.error_file = True
            return

        if (all_body[0] == '\n'):
            print("1")
            return True
        bodysplit = all_body.strip('\n').split('\n')
        if (len (bodysplit) == 0):
            print("2")
            return True
        for line in bodysplit:
            if (len(line) == 0):
                print("3")
                return True
            full_split.append(line.split(sep))
        nb_field = len(full_split[0])
        for idx, line in enumerate(full_split):
            if nb_field != len(line):
                print("4")
                return True
            for word in line:
                if len(word.strip(' \n\"')) == 0:
                    if head == True and idx == 0:
                        continue
                    return True

        fi.seek(0, 0)
        return False

class KmeansClustering:
    def __init__(self, max_iter=20, ncentroid=5):
        self.ncentroid = ncentroid # number of centroids
        self.max_iter = max_iter # number of max iterations to update the centroids
        self.centroids = [] # values of the centroids
        self.location = {}
        self.count = [0 for x in range (self.ncentroid)] 

    def fit(self, X):
        """
        Run the K-means clustering algorithm.
        For the location of the initial centroids, random pick ncentroids from the dataset.
        Args:
        -----
        X: has to be an numpy.ndarray, a matrice of dimension m * n.
        Return:
        -------
        None.
        Raises:
        -------
        This function should not raise any Exception.
        """
        def randf(deb, end):
            return (random.random() * (end - deb) + deb )
        min_max=[]
        for x in range(1, 4):
            min_max.append([float(min(X[:, x])), float(max(X[:, x]))])
        for x in range(self.ncentroid):
            self.centroids.append([randf(min_max[0][0], min_max[0][1]), randf(min_max[1][0], min_max[1][1]), randf(min_max[2][0], min_max[2][1])])
        npcentroid = np.array(self.centroids)

        newcentroid = np.full(npcentroid.shape, 0.0)

        for x in range(self.max_iter):
            for citizen in X:
                dist = np.array([])
                for centroid in npcentroid:
                    dist = np.append(dist, np.linalg.norm(citizen[1:] - centroid))

                mincentroid = np.where(dist == np.min(dist))[0][0]
                newcentroid[mincentroid] = newcentroid[mincentroid] + citizen[1:]
                self.location[int(citizen[0])] = int(mincentroid)
                self.count[mincentroid] = self.count[mincentroid] + 1

            for y in range (self.ncentroid):
                if (self.count[y] == 0):
                    newcentroid[y] = npcentroid[y]
                else:
                    newcentroid[y] = newcentroid[y] / self.count[y] 

            npcentroid = np.copy(newcentroid)
            newcentroid = np.copy(np.full(npcentroid.shape, 0.0))
            if (x != self.max_iter - 1):
                self.count = [0] * self.ncentroid

        self.centroids = []
        for lin in range(npcentroid.shape[0]):
            resl = []
            for col in range(npcentroid.shape[1]):
                resl.append(npcentroid[lin][col])
            self.centroids.append(resl)

    def predict(self, X):
        """
        Predict from wich cluster each datapoint belongs to.
        Args:
        -----
        X: has to be an numpy.ndarray, a matrice of dimension m * n.
        Return:
        -------
        the prediction has a numpy.ndarray, a vector of dimension m * 1.
        Raises:
        -------
        This function should not raise any Exception.
        """
        if (self.centroids == []):
            print("No fit on the dataset have been done")
            return []
        res = np.zeros((X.shape[0], 1), dtype=int)
        npcentroid = np.array(self.centroids)
        for idx, citizen in enumerate(X):
            dist = np.array([])
            for centroid in npcentroid:
                dist = np.append(dist, np.linalg.norm(citizen[1:] - centroid))
            mincentroid = np.where(dist == np.min(dist))[0][0]
            res[idx] = int(mincentroid)
        return res

def fileRecoveryStatistics(lstats, count, head):

    lstat = lstats[:]
    heightmax = lstat[0][0]
    As = lstat[0]
    asidx = 0
    for idx, lin in enumerate(lstat):
        for idl, col in enumerate(lin):
            if idl == 0 and heightmax < col:
                heightmax = col
                As = lin
                asidx = idx
    lstat.remove(As)
    one = lstat[0]
    two = lstat[1]
    three = lstat[2]

    Er = "not"

    def retshift(r3, r0, r1, r2):
        res = [0] * 4

        if r0 >= r3:
            r0 = r0 + 1
        if r1 >= r3:
            r1 = r1 + 1
        if r2 >= r3:
            r2 = r2 + 1
        res[0] = r0
        res[1] = r1
        res[2] = r2
        res[3] = r3
        return res

    if one[1] > two[1]:
        if three[0] > one[0]:
            Er = one
            Vn = two
            Mr = three
            ret = retshift(asidx, 1, 0, 2)

    if two[1] > three[1]:
        if one[0] > two[0]:
            Er = two
            Vn = three
            Mr = one
            ret = retshift(asidx, 2, 1, 0)

    if three[1] > one[1]:
        if two[0] > three[0]:
            Er = three
            Vn = one
            Mr = two
            ret = retshift(asidx, 0, 2, 1)

    if one[1] < two[1]:
        if three[0] > two[0]:
            Er = two
            Vn = one
            Mr = three
            ret = retshift(asidx, 0, 1, 2)

    if two[1] < three[1]:
        if one[0] > three[0]:
            Er = three
            Vn = two
            Mr = one
            ret = retshift(asidx, 1, 2, 0)

    if three[1] < one[1]:
        if two[0] > one[0]:
            Er = one
            Vn = three
            Mr = two
            ret = retshift(asidx, 2, 0, 1)

    if Er == "not":
        print("Citys can not be put on data centroid")
        return None
    else:
        if type(head) is list and len(head) == 4:
            print(f"Centroid coordinate using : \t\t{head[1]}, \t    {head[2]}, \t\t{head[3]}")
        print("The flying cities of Venus centroid : ", Vn, f"Counting {count[ret[0]]} citizens")
        print("United nations of Earth centroid : ", Er, f"Counting {count[ret[1]]} citizens")
        print("Mars Republic centroid :", Mr, f"Counting {count[ret[2]]} citizens")
        print("Asteroids' Belt colonies centroid : ", As, f"Counting {count[ret[3]]} citizens")
        return ret

def coloniecolor(deter, nb):
    col = deter.index(nb)
    if (col == 0):
        return('violet')
    elif (col == 1):
        return('brown')
    elif (col == 2):
        return('red')
    elif(col == 3):
        return ('black')
def colonielabel(deter, nb):
    col = deter.index(nb)
    if (col == 0):
        return("Venus")
    elif (col == 1):
        return("Earth")
    elif (col == 2):
        return ("Mars")
    elif (col == 3):
        return ("Asteroid")

if (__name__ == "__main__"):
    if len(sys.argv) > 4:
        print("Wrong number of argument")
        sys.exit()
    kwarg={}
    kwarg["ncentroid"] = 5
    kwarg["max_iter"] = 20

    for arg in sys.argv[1:]:
        sp = arg.split('=')
        if (len(sp) != 2):
            print("Wrong Argument")
            sys.exit()
        kwarg[sp[0]] = sp[1]
    
    if not "filepath" in kwarg.keys():
        print("no filepath")
        sys.exit()
    if (len(kwarg) > 3):
        print("Bad argument")
        sys.exit()
    if (type(kwarg["ncentroid"]) is str and not kwarg["ncentroid"].isdigit()) or (type(kwarg["max_iter"]) is str and not kwarg["max_iter"].isdigit()):
        print("ncentroid and max_iter must be integer")
        sys.exit()
    valid_arg = ["filepath", "ncentroid", "max_iter"]
    for arg in kwarg.keys():
        if not arg in valid_arg:
            print(f"invalid key argument {arg}")
            sys.exit()
    kwarg["max_iter"] = int(kwarg["max_iter"])
    kwarg["ncentroid"] = int(kwarg["ncentroid"])

    if (kwarg["max_iter"] <= 0):
        print("max_iter must be strictly positiv")
        sys.exit()
    

    with CsvReader(kwarg["filepath"], header=True, sep=",") as file:
        if file == None:
            os._exit(1)
        data = np.array(file.getdata()).astype(float)
        head = file.getheader()

        kmc = KmeansClustering(kwarg["max_iter"], kwarg["ncentroid"])

        kmc.fit(data)
        if kwarg["ncentroid"] == 4:
            if (data.shape[1] != 4):
                print("Coordinate of the centroids using", ' '.join(head[1:]))
                for x in range(len(kmc.centroids)):
                    print(f"Centroid {x} : ", kmc.centroids[x], f"counting {kmc.count[x]} citizens")
                os._exit(0)

            determine = fileRecoveryStatistics(kmc.centroids, kmc.count, head)
            if determine == None:
                os._exit(0)

            pred = kmc.predict(data)

            x = data[:, [0, 1]]
            y = data[:, [0, 2]]

            x0= [idx[1] for idx in x if pred[int(idx[0])][0] == 0]
            y0= [idx[1] for idx in y if pred[int(idx[0])][0] == 0]

            x1= [idx[1] for idx in x if pred[int(idx[0])][0] == 1]
            y1= [idx[1] for idx in y if pred[int(idx[0])][0] == 1]

            x2= [idx[1] for idx in x if pred[int(idx[0])][0] == 2]
            y2= [idx[1] for idx in y if pred[int(idx[0])][0] == 2]

            x3= [idx[1] for idx in x if pred[int(idx[0])][0] == 3]
            y3= [idx[1] for idx in y if pred[int(idx[0])][0] == 3]


            fig, ax = plt.subplots(2, 2)
            plt.get_current_fig_manager().canvas.manager.set_window_title('Kmeans.py')
            fig.suptitle("K-means Clustering, %d iterations 4 centroids." % (kwarg["max_iter"]))

            ax[0][0].scatter(x0, y0, c=coloniecolor(determine, 0))
            ax[0][0].scatter(x1, y1, c=coloniecolor(determine, 1))
            ax[0][0].scatter(x2, y2, c=coloniecolor(determine, 2))
            ax[0][0].scatter(x3, y3, c=coloniecolor(determine, 3))

            ax[0][0].scatter(kmc.centroids[0][0], kmc.centroids[0][1],s=300, marker="*", c=coloniecolor(determine, 0))
            ax[0][0].text(x=kmc.centroids[0][0], y=kmc.centroids[0][1], s=colonielabel(determine, 0))
            ax[0][0].scatter(kmc.centroids[1][0], kmc.centroids[1][1],s=300, marker="*", c=coloniecolor(determine, 1))
            ax[0][0].text(x=kmc.centroids[1][0], y=kmc.centroids[1][1], s=colonielabel(determine, 1))
            ax[0][0].scatter(kmc.centroids[2][0], kmc.centroids[2][1],s=300, marker="*", c=coloniecolor(determine, 2))
            ax[0][0].text(x=kmc.centroids[2][0], y=kmc.centroids[2][1], s=colonielabel(determine, 2))
            ax[0][0].scatter(kmc.centroids[3][0], kmc.centroids[3][1],s=300, marker="*", c=coloniecolor(determine, 3))
            ax[0][0].text(x=kmc.centroids[3][0], y=kmc.centroids[3][1], s=colonielabel(determine, 3))

            ax[0][0].set_title('Height-Weight relation')
            ax[0][0].set_xlabel('height')
            ax[0][0].set_ylabel('weight')

            x = data[:, [0, 2]]
            y = data[:, [0, 3]]

            x0= [idx[1] for idx in x if pred[int(idx[0])][0] == 0]
            y0= [idx[1] for idx in y if pred[int(idx[0])][0] == 0]

            x1= [idx[1] for idx in x if pred[int(idx[0])][0] == 1]
            y1= [idx[1] for idx in y if pred[int(idx[0])][0] == 1]

            x2= [idx[1] for idx in x if pred[int(idx[0])][0] == 2]
            y2= [idx[1] for idx in y if pred[int(idx[0])][0] == 2]

            x3= [idx[1] for idx in x if pred[int(idx[0])][0] == 3]
            y3= [idx[1] for idx in y if pred[int(idx[0])][0] == 3]

            ax[0][1].scatter(x0, y0, c=coloniecolor(determine, 0))
            ax[0][1].scatter(x1, y1, c=coloniecolor(determine, 1))
            ax[0][1].scatter(x2, y2, c=coloniecolor(determine, 2))
            ax[0][1].scatter(x3, y3, c=coloniecolor(determine, 3))

            ax[0][1].scatter(kmc.centroids[0][1], kmc.centroids[0][2],s=300, marker="*", c=coloniecolor(determine, 0))
            ax[0][1].text(x=kmc.centroids[0][1], y=kmc.centroids[0][2], s=colonielabel(determine, 0))
            ax[0][1].scatter(kmc.centroids[1][1], kmc.centroids[1][2],s=300, marker="*", c=coloniecolor(determine, 1))
            ax[0][1].text(x=kmc.centroids[1][1], y=kmc.centroids[1][2], s=colonielabel(determine, 1))
            ax[0][1].scatter(kmc.centroids[2][1], kmc.centroids[2][2],s=300, marker="*", c=coloniecolor(determine, 2))
            ax[0][1].text(x=kmc.centroids[2][1], y=kmc.centroids[2][2], s=colonielabel(determine, 2))
            ax[0][1].scatter(kmc.centroids[3][1], kmc.centroids[3][2],s=300, marker="*", c=coloniecolor(determine, 3))
            ax[0][1].text(x=kmc.centroids[3][1], y=kmc.centroids[3][2], s=colonielabel(determine, 3))

            ax[0][1].set_title('Weight-Bone_density relation')
            ax[0][1].set_xlabel('weight')
            ax[0][1].set_ylabel('bone_density')

            x = data[:, [0, 1]]
            y = data[:, [0, 3]]

            x0= [idx[1] for idx in x if pred[int(idx[0])][0] == 0]
            y0= [idx[1] for idx in y if pred[int(idx[0])][0] == 0]

            x1= [idx[1] for idx in x if pred[int(idx[0])][0] == 1]
            y1= [idx[1] for idx in y if pred[int(idx[0])][0] == 1]

            x2= [idx[1] for idx in x if pred[int(idx[0])][0] == 2]
            y2= [idx[1] for idx in y if pred[int(idx[0])][0] == 2]

            x3= [idx[1] for idx in x if pred[int(idx[0])][0] == 3]
            y3= [idx[1] for idx in y if pred[int(idx[0])][0] == 3]

            ax[1][0].scatter(x0, y0, c=coloniecolor(determine, 0))
            ax[1][0].scatter(x1, y1, c=coloniecolor(determine, 1))
            ax[1][0].scatter(x2, y2, c=coloniecolor(determine, 2))
            ax[1][0].scatter(x3, y3, c=coloniecolor(determine, 3))

            ax[1][0].scatter(kmc.centroids[0][0], kmc.centroids[0][2],s=300, marker="*", c=coloniecolor(determine, 0))
            ax[1][0].text(x=kmc.centroids[0][0], y=kmc.centroids[0][2], s=colonielabel(determine, 0))
            ax[1][0].scatter(kmc.centroids[1][0], kmc.centroids[1][2],s=300, marker="*", c=coloniecolor(determine, 1))
            ax[1][0].text(x=kmc.centroids[1][0], y=kmc.centroids[1][2], s=colonielabel(determine, 1))
            ax[1][0].scatter(kmc.centroids[2][0], kmc.centroids[2][2],s=300, marker="*", c=coloniecolor(determine, 2))
            ax[1][0].text(x=kmc.centroids[2][0], y=kmc.centroids[2][2], s=colonielabel(determine, 2))
            ax[1][0].scatter(kmc.centroids[3][0], kmc.centroids[3][2],s=300, marker="*", c=coloniecolor(determine, 3))
            ax[1][0].text(x=kmc.centroids[3][0], y=kmc.centroids[3][2], s=colonielabel(determine, 3))


            ax[1][0].set_title('Height-Bone_density relation')
            ax[1][0].set_xlabel('height')
            ax[1][0].set_ylabel('bone_density')

            x = data[:, [0, 1]]
            y = data[:, [0, 2]]
            z = data[:, [0, 3]]

            x0= [idx[1] for idx in x if pred[int(idx[0])][0] == 0]
            y0= [idx[1] for idx in y if pred[int(idx[0])][0] == 0]
            z0= [idx[1] for idx in z if pred[int(idx[0])][0] == 0]

            x1= [idx[1] for idx in x if pred[int(idx[0])][0] == 1]
            y1= [idx[1] for idx in y if pred[int(idx[0])][0] == 1]
            z1= [idx[1] for idx in z if pred[int(idx[0])][0] == 1]

            x2= [idx[1] for idx in x if pred[int(idx[0])][0] == 2]
            y2= [idx[1] for idx in y if pred[int(idx[0])][0] == 2]
            z2= [idx[1] for idx in z if pred[int(idx[0])][0] == 2]

            x3= [idx[1] for idx in x if pred[int(idx[0])][0] == 3]
            y3= [idx[1] for idx in y if pred[int(idx[0])][0] == 3]
            z3= [idx[1] for idx in z if pred[int(idx[0])][0] == 3]

            ax[1][1].remove()

            ax[1][1] = fig.add_subplot(224, projection='3d')
            ax[1][1].scatter(x0, y0, z0, c=coloniecolor(determine, 0))
            ax[1][1].scatter(x1, y1, z1, c=coloniecolor(determine, 1))
            ax[1][1].scatter(x2, y2, z2, c=coloniecolor(determine, 2))
            ax[1][1].scatter(x3, y3, z3, c=coloniecolor(determine, 3))

            ax[1][1].scatter(kmc.centroids[0][0], kmc.centroids[0][1], kmc.centroids[0][2], s=150, marker="*", c=coloniecolor(determine, 0))
            ax[1][1].text(x=kmc.centroids[0][0], y=kmc.centroids[0][1], z=kmc.centroids[0][2], s=colonielabel(determine, 0))
            ax[1][1].scatter(kmc.centroids[1][0], kmc.centroids[1][1], kmc.centroids[1][2], s=150, marker="*", c=coloniecolor(determine, 1))
            ax[1][1].text(x=kmc.centroids[1][0], y=kmc.centroids[1][1], z=kmc.centroids[1][2], s=colonielabel(determine, 1))
            ax[1][1].scatter(kmc.centroids[2][0], kmc.centroids[2][1], kmc.centroids[2][2], s=150, marker="*", c=coloniecolor(determine, 2))
            ax[1][1].text(x=kmc.centroids[2][0], y=kmc.centroids[2][1], z=kmc.centroids[2][2], s=colonielabel(determine, 2))
            ax[1][1].scatter(kmc.centroids[3][0], kmc.centroids[3][1], kmc.centroids[3][2], s=150, marker="*", c=coloniecolor(determine, 3))
            ax[1][1].text(x=kmc.centroids[3][0], y=kmc.centroids[3][1], z=kmc.centroids[3][2], s=colonielabel(determine, 3))

            ax[1][1].set_title('Total data relations')
            ax[1][1].set_xlabel('height')
            ax[1][1].set_ylabel('weight')
            ax[1][1].set_zlabel('bone_density')

            plt.show()
        else:
            print("Coordinate of the centroids using", ' '.join(head[1:]))
            for x in range(len(kmc.centroids)):
                print(f"Centroid {x} : ", kmc.centroids[x], f"counting {kmc.count[x]} citizens")
