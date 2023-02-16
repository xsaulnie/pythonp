import functools
def ft_filter(function_to_apply, iterable):
    """Filter the result of function apply to all elements of the iterable.
    Args:
    function_to_apply: a function taking an iterable.
    iterable: an iterable object (list, tuple, iterator).
    Return:
    An iterable.
    None if the iterable can not be used by the function.
    """

    if not hasattr(iterable, "__iter__"):
        raise TypeError(f" object type '{type(iterable).__name__}' is not iterable")

    res = []
    for x in iterable:
        try:
            verif = function_to_apply(x)
        except:
            return None
        if (verif):
            res.append(x)
    return res
    
x = [1, 2, 3, 4, 5]
y = (8, 5, 2)
print(ft_filter(lambda dum: not (dum % 2), x))
print(ft_filter(lambda dum: not (dum % 2), y))

print(x)
print(y)

