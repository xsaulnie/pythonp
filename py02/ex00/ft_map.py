def ft_map(function_to_apply, iterable):
    """Map the function to all elements of the iterable.
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
        try :
            elem = function_to_apply(x)
        except:
            return (None)
        res.append(elem)
    return res

x = [1, 2, 3, 4, 5]
y = 0
print(ft_map(lambda t : t + 1, x))
print(ft_map(lambda t : t.display, x))
print(ft_map(lambda t : t + 1, y))
