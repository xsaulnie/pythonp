class Vector:
    def __init__(self, arg):
        dim1=0
        dim2=0
        if (type(arg) is not list):
            print("Error constructor : arg is not a list")
            return
        if (type(arg[0]) is not list):
            print("Error constructor : arg is not a list of list")
            return
        dim2 = len(arg[0])
        for x in arg:
            if (type(x) is not list):
                print("Error constructor : list on arg is incorrect")
                return
            for y in x:
                if (type(y) is not float):
                    print("Error constructor : element in vector is not a float")
                    return
            if (len(x) is not dim2):
                print("Error constructor : dimention on arg are inhomogeneous")
                return
            dim1 += 1
        if (dim1 != 1 and dim2 != 1):
            print("Error constructor : dimention on are are incorrect : it is not a vector")
            return
        self.values = arg
        self.shape = (dim1, dim2)
    def dot(self, vec):
        if (type(vec) is not Vector):
            print("Error vector dot method : wrong argument")
            return
        if (self.shape != vec.shape):
            print("Error vector dot method : dimentions of dot product differ")
            return
        

