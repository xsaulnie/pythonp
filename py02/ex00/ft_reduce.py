import functools
def ft_reduce(function_to_apply, iterable):
    """Apply function of two arguments cumulatively.
    Args:
    function_to_apply: a function taking an iterable.
    iterable: an iterable object (list, tuple, iterator).
    Return:
    A value, of same type of elements in the iterable parameter.
    None if the iterable can not be used by the function.
    """
    if not hasattr(iterable, "__iter__"):
        raise TypeError(f" object type '{type(iterable).__name__}' is not iterable")

    if (len(iterable) == 0):
        raise TypeError("reduce() of empty iterable with no initial value")
    if (len(iterable) == 1):
        return (iterable[0])
    val = iterable[0]

    for x in iterable[1:]:
        try:
            val = function_to_apply(val, x)
        except:
            return None
    return val

lst = ["H", "e", "l", "l", "o", " ", "w", "o", "r", "l", "d"]
#print(functools.reduce(lambda u, v: u + v, lst))
print(ft_reduce(lambda u, v: u + v, lst))

