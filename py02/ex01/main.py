def what_are_the_vars(*arg, **kwarg):
    ret = {}
    for idx, val in enumerate(arg):
        ret["var_" + str(idx)] = val

    for key, val in kwarg.items():
        if (key.startswith("var_")):
            if key in ret.keys():
                return None
        ret[key] = val
    return(ObjectC(ret))

# ... Your code here ...
class ObjectC(object):
    def __init__(self, obj):
        if (not type(obj) is dict):
            return
        self.__dict__.update(obj)


def doom_printer(obj):
    if obj is None:
        print("ERROR")
        print("end")
        return
    for attr in dir(obj):
        if attr[0] != '_':
            value = getattr(obj, attr)
            print("{}: {}".format(attr, value))
    print("end")

if __name__ == "__main__":
    obj = what_are_the_vars(7)
    doom_printer(obj)
    obj = what_are_the_vars(None, [])
    doom_printer(obj)
    obj = what_are_the_vars("ft_lol", "Hi")
    doom_printer(obj)
    obj = what_are_the_vars()
    doom_printer(obj)
    obj = what_are_the_vars(12, "Yes", [0, 0, 0], a=10, hello="world")
    doom_printer(obj)
    obj = what_are_the_vars(42, a=10, var_0="world")
    doom_printer(obj)
    obj = what_are_the_vars(42, "Yes", a=10, var_2="world")
    doom_printer(obj)