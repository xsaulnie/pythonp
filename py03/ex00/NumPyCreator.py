import numpy as np
from numpy.random import default_rng

class NumpyCreator:
    def from_list(self, lst):
        if ( not type(lst) is list):
            return None
        try: 
            ret = np.array(lst)
        except:
            return None
        return ret
    
    def from_tuple(self, tpl):
        if ( not type(tpl) is tuple):
            return None
        try:
            ret = np.array(tpl)
        except:
            return None
        return ret
    
    def from_iterable(self, itr):
        if ( not hasattr(itr, "__iter__")):
            return None
        try:
            ret = np.array(itr)
        except:
            return None
        return ret
    
    def from_shape(self, shape, value=0):
        if (not type(shape) is tuple):
            return None
        if (len(shape) != 2):
            return None
        for x in shape:
            if (not type(x) is int):
                return None
        return np.full(shape, value)
    
    def random(self, shape):
        if (not type(shape) is tuple):
            return None
        if (len(shape) != 2):
            return None
        for x in shape:
            if (not type(x) is int):
                return None
        return default_rng(42).random(shape)
    
    def identity(self, n):
        return np.eye(n)

npc = NumpyCreator()
print(npc.from_list([[1, 2, 3], [6, 3, 4]]), end="\n\n")
print(npc.from_list([[1,2,3],['a','b','c'],[6,4,7]]), end="\n\n")
print(npc.from_tuple((("a", "x"), ("b", "z"), ("c", "r"))), end="\n\n")
print(npc.from_iterable(range(10)), end="\n\n")
print(npc.from_shape((3, 5)), end="\n\n")
print(npc.random((3, 5)), end="\n\n")
print(npc.identity(4), end="\n\n")


print(npc.from_list([[1,2,3],[6,4]]))
print(npc.from_list(((1,2),(3,4))))
print(npc.from_list(((1,2),(3,4))))
print(npc.from_tuple(["a", "b", "c"]))