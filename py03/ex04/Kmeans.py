import numpy as np

class CsvReader():
    def __init__(self, filename=None, sep=',', header=False, skip_top=0, skip_bottom=0):
        # ... Your code here ...

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
        print("fit")

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
        print("predict")

with CsvReader("solar_system_census.csv", header=True, sep=",") as file:
    data = np.array(file.getdata())
    head = file.getheader()
    print(data)
