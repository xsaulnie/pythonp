import functools
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
        if (self.check_corruption(self.fi, sep)):
            self.corrupted = True
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
    def check_corruption(fi, sep):
        full_split = []
        all_body = fi.read()
        if (all_body[0] == '\n'):
            return True
        bodysplit = all_body.strip('\n').split('\n')
        if (len (bodysplit) == 0):
            return True
        for line in bodysplit:
            if (len(line) == 0):
                return True
            full_split.append(line.split(sep))
        nb_field = len(full_split[0])
        for line in full_split:
            if nb_field != len(line):
                return True
            for word in line:
                if len(word.strip(' \n\"')) == 0:
                    return True

        fi.seek(0, 0)
        return False



if __name__ == "__main__":
    with CsvReader("good.csv", header=True, skip_bottom = 0, skip_top = 0) as file:
        data = file.getdata()
        header = file.getheader()
        print("data", data)
        print("header", header)

    with CsvReader("bad.csv") as file:
        if file == None:
            print("File is corrupted")
    with CsvReader("notafile") as file:
        if file == None:
            print("None")