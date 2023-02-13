class Vector:
    def __init__(self, arg):
        dim1=0
        dim2=0
        if (type(arg) is int):
            self.shape = (arg, 1)
            self.values = []
            for x in range(arg):
                self.values.append([float(x)])
            return
        if (type(arg) is tuple):
            if (len(arg) != 2):
                print("Error constructor : range is incorrect")
                return
            if (type(arg[0]) is not int or type(arg[1]) is not int):
                print("Error constructor : range is incorrect")
                return
            if (arg[1] < arg[0]):
                print("Error constructor : range start is greater than its end")
                return
            self.shape = (arg[1] - arg[0], 1)
            self.values = []
            for x in range(arg[0], arg[1]):
                self.values.append([float(x)])
            return

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
        
        ret = 0
        if (self.shape[0] == 1):
            for x, y in zip(self.values[0], vec.values[0]):
                ret = ret + x * y
            return ret
        for x, y in zip(self.values, vec.values):
            ret = ret + x[0] * y [0]
        return ret

    def T(self):
        ret = []
        if self.shape[0] == 1:
            for x in self.values[0]:
                ret.append([x])
            return(Vector(ret))
        ret = [[]]
        for x in self.values:
            ret[0].append(x[0])
        return (Vector(ret))
    def __repr__(self):
        return (f"{self.values}")
    def __str__(self):
        return (f"{self.values}")

    def __add__(self, vec):
        if (type(vec) is not Vector):
            print("Error Vector add/radd operator : wrong type")
            return
        if (self.shape != vec.shape):
            print("Error Vector add/radd operator : wrong dimension")
            return

        ret = [[]]
        if self.shape[0] == 1:
            for x, y in zip(self.values[0], vec.values[0]):
                ret[0].append(x + y)
            return(Vector(ret))
        ret = []
        for x, y in zip(self.values, vec.values):
            ret.append([x[0] + y[0]])
        return(Vector(ret))

    def __radd__(self, vec):
        return(self.__add__(vec))

    def __sub__(self, vec):
        if (type(vec) is not Vector):
            print("Error Vector sub operator : wrong type")
            return
        if (self.shape != vec.shape):
            print("Error Vector sub operator : wrong dimension")
            return
        ret = [[]]
        if self.shape[0] == 1:
            for x, y in zip(self.values[0], vec.values[0]):
                ret[0].append(x - y)
            return (Vector(ret))
        ret = []
        for x, y in zip(self.values, vec.values):
            ret.append([x[0] - y[0]])
        return (Vector(ret))

    def __rsub__(self, vec):
        if (type(vec) is not Vector):
            print("Error Vector rsub operator : wrong type")
            return
        if (self.shape != vec.shape):
            print("Error Vector rsub operator : wrong dimension")
            return
        return (vec.__sub__(self))

    def __truediv__(self, scalar):
        if (type(scalar) is not int and type(scalar) is not float):
            print("Error Vector truediv operator : wrong type")
            return
        if self.shape[0] == 1:
            ret = [[]]
            for x in self.values[0]:
                ret[0].append(x / scalar)
            return(Vector(ret))
        ret = []
        for x in self.values:
            ret.append([x[0] / scalar])
        return(Vector(ret))

    def __rtruediv__(self, arg):
        raise NotImplementedError("Division of a scalar by a Vector is not defined here.")

    def __mul__(self, scalar):
        if (type(scalar) is not int and type(scalar) is not float):
            print("Error Vector mul operator : wrong type")
            return
        if self.shape[0] == 1:
            ret = [[]]
            for x in self.values[0]:
                ret[0].append(x * scalar)
            return(Vector(ret))
        ret = []
        for x in self.values:
            ret.append([x[0] * scalar])
        return(Vector(ret))

    def __rmul__(self, scalar):
        if (type(scalar) is not int and type(scalar) is not float):
            print("Error Vector rmul operator : wrong type")
            return
        return(self.__mul__(scalar))


    



        

