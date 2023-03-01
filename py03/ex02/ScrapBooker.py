import numpy as np
class ScrapBooker():
    def crop(self, array, dim, position=(0,0)):
        """
        Crops the image as a rectangle via dim arguments (being the new height
        and width of the image) from the coordinates given by position arguments.
        Args:
        -----
        array: numpy.ndarray
        dim: tuple of 2 integers.
        position: tuple of 2 integers.
        Return:
        -------
        new_arr: the cropped numpy.ndarray.
        None (if combinaison of parameters not compatible).
        Raise:
        ------
        This function should not raise any Exception.
        """
        if (not isinstance(array, np.ndarray) or not type(dim) is tuple or not type(position) is tuple):
            return None
        if (len(position) != 2 or len(dim) != 2):
            return None
        if (dim[0] + position[0] > array.shape[0] or dim[1] + position[1] > array.shape[1]):
            return None
        if (dim[0] < 0 or dim[1] < 0 or position[0] < 0 or position[1] < 0):
            return None
        
        return array[ position[0]: dim[0] + position[0], position[1] : dim[1] + position[1]]
    def thin(self, array, n, axis):
        """
        Deletes every n-th line pixels along the specified axis (0: Horizontal, 1: Vertical)
        Args:
        -----
        array: numpy.ndarray.
        n: non null positive integer lower than the number of row/column of the array
        (depending of axis value).
        axis: positive non null integer.
        Return:
        -------
        new_arr: thined numpy.ndarray.
        None (if combinaison of parameters not compatible).
        Raise:
        ------
        This function should not raise any Exception.
        """
        if (not isinstance(array, np.ndarray) or not type(n) is int or not type(axis) is int):
            return None
        if (axis != 1 and axis != 0):
            return None
        if (n <= 0):
            return None
        if (axis == 0):
            if n > array.shape[1]:
                return None
            tobedeleted = [x for x in range(array.shape[1]) if (x + 1) % n == 0]
            return np.delete(array, tobedeleted, 1)
        else:
            if n > array.shape[0]:
                return None
            tobedeleted = [x for x in range(array.shape[0]) if (x + 1) % n == 0]
            return np.delete(array, tobedeleted, 0)
    def juxtapose(self, array, n, axis):
        """
        Juxtaposes n copies of the image along the specified axis.
        Args:
        -----
        array: numpy.ndarray.
        n: positive non null integer.
        axis: integer of value 0 or 1.
        Return:
        -------
        new_arr: juxtaposed numpy.ndarray.
        None (combinaison of parameters not compatible).
        Raises:
        -------
        This function should not raise any Exception.
        """
        if (not isinstance(array, np.ndarray) or not type(n) is int or not type(axis) is int):
            return None
        if (axis != 1 and axis != 0):
            return None
        if (n <= 0):
            return None
        ret = array
        for x in range(n - 1):
            ret = np.concatenate((ret, array), axis=axis)
        return ret
    def mosaic(self, array, dim):
        """
        Makes a grid with multiple copies of the array. The dim argument specifies
        the number of repetition along each dimensions.
        Args:
        -----
        array: numpy.ndarray.
        dim: tuple of 2 integers.
        Return:
        -------
        new_arr: mosaic numpy.ndarray.
        None (combinaison of parameters not compatible).
        Raises:
        -------
        This function should not raise any Exception.
        """

        if (not isinstance(array, np.ndarray) or not type (dim) is tuple):
            return None
        if (len(dim) != 2):
            return None
        if (dim[0] < 0 or dim[1] < 0):
            return None
        if (dim[0] == 0 and dim[1] == 0):
            return np.empty(shape=[0, 0])
        ret = array

        for x in range(dim[1] - 1):
            ret = np.concatenate((ret, array), axis = 1)
        line_ret = ret
        for x in range(dim[0] - 1):
            ret = np.concatenate((ret, line_ret), axis = 0)
        return ret

spb = ScrapBooker()
arr1 =np.arange(0, 25).reshape(5, 5)

print(arr1)
dim=(2, 1)
pos=(3, 1)
print(f"croped {dim} {pos}:\n", spb.crop(arr1, dim, pos))

arr2 = np.array("A B C D E F G H I".split() * 6).reshape(-1,9)
print(arr2)
print(spb.thin(arr2, 3,0))

arr3 = np.array([[1, 2, 3], [1, 2, 3], [1, 2, 3]])
print(arr3)
print(spb.juxtapose(arr3, 3, 1))

arr4 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(arr4, end="\n\n")
m_shape = (2, 2)
print(f"mosaic {m_shape}:", end="\n\n")
print(spb.mosaic(arr4, m_shape))
