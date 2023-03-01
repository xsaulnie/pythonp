import numpy as np
import sys
import random


class CsvReader():
    def __init__(self, filename=None, sep=',', header=False, skip_top=0, skip_bottom=0):
        try:
            fi = open(filename, "r")
        except:
            print(f"Error on opening '{filename}' file")
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

    @staticmethod
    def check_corruption(fi, sep, head):
        full_split = []
        all_body = fi.read()
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
        #random.seed(1532543531)
        def randf(deb, end):
            return (random.random() * (end - deb) + deb )
        min_max=[]
        for x in range(1, 4):
            min_max.append([float(min(X[:, x])), float(max(X[:, x]))])
        #print(min_max)
        for x in range(self.ncentroid):
            self.centroids.append([randf(min_max[0][0], min_max[0][1]), randf(min_max[1][0], min_max[1][1]), randf(min_max[2][0], min_max[2][1])])
        #print("centroids", self.centroids)
        npcentroid = np.array(self.centroids)
        #print(npcentroid)

        newcentroid = np.full(npcentroid.shape, 0.0)
        #print(newcentroid)

        for x in range(self.max_iter):
            for citizen in X:
                dist = np.array([])
                for centroid in npcentroid:
                    #print("dist", dist, end="\n\n")
                    dist = np.append(dist, np.linalg.norm(citizen[1:] - centroid))

                #print("dist", dist)

                mincentroid = np.where(dist == np.min(dist))[0][0]
                # print("cit", citizen[1:])
                # print("n", newcentroid[mincentroid])
                newcentroid[mincentroid] = newcentroid[mincentroid] + citizen[1:]
                self.location[int(citizen[0])] = int(mincentroid)
                self.count[mincentroid] = self.count[mincentroid] + 1
            #print(self.location)

            #print("prenew", newcentroid, end="\n\n")

            for y in range (self.ncentroid):
                if (self.count[y] == 0):
                    newcentroid[y] = npcentroid[y]
                else:
                    newcentroid[y] = newcentroid[y] / self.count[y] 

            # print( "new ", newcentroid, end="\n\n")
            # print("cur", npcentroid,end="\n\n")
            npcentroid = np.copy(newcentroid)
            #print("cur after", npcentroid, end="\n\n")
            newcentroid = np.copy(np.full(npcentroid.shape, 0.0))
            # print("new after", newcentroid, end="\n\n")
            # print(npcentroid, end="\n\n")
            # print("count", self.count)
            #print(self.count)
            #print(x, self.max_iter)
            if (x != self.max_iter - 1):
                self.count = [0] * self.ncentroid
            #print(npcentroid)
            #print(self.location)

        self.centroids = []
        #print(npcentroid)
        for lin in range(npcentroid.shape[0]):
            #self.centroids.append([])
            resl = []
            for col in range(npcentroid.shape[1]):
                #self.centroids[lin].append(npcentroid[lin][col])
                #print(npcentroid[lin][col])
                resl.append(npcentroid[lin][col])
            self.centroids.append(resl)
            #print(end="\n")





        # for x in range (self.ncentroid):
        #     print("hello")
        #     self.centroids.append(randf(min_max[0][0], min_max[0][1]))
        # print(self.centroids)

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

def fileRecoveryStatistics(lstats, count):

    lstat = lstats[:]
    heightmax = lstat[0][0]
    As = lstat[0]
    asidx = 0
    print(lstat)
    for idx, lin in enumerate(lstat):
        for idl, col in enumerate(lin):
            #print("idl", idl, "col", col, "heightmax", heightmax)
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
        print("The flying cities of Venus centroid : ", Vn, f"Counting {count[ret[0]]} citizens")
        print("United nations of Earth centroid : ", Er, f"Counting {count[ret[1]]} citizens")
        print("Mars Republic centroid :", Mr, f"Counting {count[ret[2]]} citizens")
        print("Asteroids' Belt colonies centroid : ", As, f"Counting {count[ret[3]]} citizens")
        print("ret", ret)
        return ret

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
    

    with CsvReader(kwarg["filepath"], header=True, sep=",") as file:
        if file == None:
            sys.exit()
        data = np.array(file.getdata()).astype(float) #tocheck
        head = file.getheader()

        kmc = KmeansClustering(kwarg["max_iter"], kwarg["ncentroid"])

        kmc.fit(data)
        if kwarg["ncentroid"] == 4:
            fileRecoveryStatistics(kmc.centroids, kmc.count)
            print(kmc.predict(data))
        else:
            print("Coordinate of the centroids :")
            print(kmc.centroids)
            print("Number of element in each centroids (by order)")
            print(kmc.count)




