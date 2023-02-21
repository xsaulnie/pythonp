import sys
import math
import numpy as np

class TinyStatistician():
    @staticmethod

    def check_type(li):

        niteger = [int, float]
        if type(li) is list:
            for x in li:
                if (not type(x) in niteger):
                    return False
            return True
        if isinstance(li, np.ndarray):
            if (len(li.shape) != 1):
                return False
            if (li.dtype != np.int64 and li.dtype != np.float64):
                return False
            return True
        return False

    def mean(self, li):

        if not TinyStatistician.check_type(li):
            raise TypeError("list/array corrupted")
        if (len(li) == 0):
            return None
        ret = 0
        for x in li:
            ret = ret + x
        return (float(ret / len(li)))

    def median(self, li):
        if not TinyStatistician.check_type(li):
            raise TypeError("list/array corrupted")
        lng = len(li)
        if (lng < 1):
            return None
        sort = sorted(li)
        if lng % 2 == 1:
            return (float(sort[int((lng + 1)/ 2 - 1)]))
        else:
            return(float((sort[int(lng / 2 - 1)] + sort[int(lng / 2)]) / 2))

    def quartiles(self, li):
        if not TinyStatistician.check_type(li):
            raise TypeError("list/array corrupted")
        lng = len(li)
        if (lng < 4):
            return None
        sort = sorted(li)
        
        r1 = math.ceil(lng / 4)
        r2 = math.ceil(lng / 4 * 3)
        return ([float(sort[int(r1 - 1)]), float(sort[int(r2 - 1)])])

        # if lng % 2 == 0:
        #     q1 = sort[:int(lng / 2)]
        #     q3 = sort[int(lng / 2):]
        # else:
        #     q1 = sort[:int(lng / 2)]
        #     q3 = sort[int(lng / 2) + 1:]
        # lq1 = len(q1)
        # lq3 = len(q3)

        # if (lq1 % 2 == 1):
        #     t1 = float(q1[int((lq1 + 1)/ 2 - 1)])
        # else:
        #     t1 = float((q1[int(lq1 / 2 - 1)] + q1[int(lq1 / 2)]) / 2)
        
        # if (lq3 % 2 == 1):
        #     t3 = float(q3[int((lq3 + 1)/ 2 - 1)])
        # else:
        #     t3 = float((q3[int(lq3 / 2 - 1)] + q3[int(lq3 / 2)]) / 2)
        # return ([t1, t3])

    def var(self, li):
        if not TinyStatistician.check_type(li):
            raise TypeError("list/array corrupted")
        lng = len(li)
        if (lng == 0):
            return None
        mean = self.mean(li)

        ret = 0
        for x in li:
            ret = ret + (x - mean)**2
        return (float(ret / lng))
    def std(self, li):
        if not TinyStatistician.check_type(li):
            raise TypeError("list/array corrupted")
        lng = len(li)
        if (lng == 0):
            return None
        mean = self.mean(li)

        ret = 0
        for x in li:
            ret = ret + (x - mean)**2
        return (float(math.sqrt(ret / lng)))

tstat = TinyStatistician()



a = [1, 42, 300, 10, 59]
b = np.array([10, 20, 30, 40])

print("mean")
print(tstat.mean(a))
print(tstat.mean(b))

print("median")
print(tstat.median(a))
print(tstat.median(b))

print("quartiles")
print(tstat.quartiles(a))
print(tstat.quartiles(b))

print("variance")
print(tstat.var(a))
print(tstat.var(b))

print("standard deviation")
print(tstat.std(a))
print(tstat.std(b))

