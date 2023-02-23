from matplotlib import pyplot as plt
import numpy as np
class ImageProcessor():
    def load(self, name):
        if (not type(name) is str):
            raise(TypeError("ImageProcessor load expect a string as name"))

        try:
            im = plt.imread(name)
        except Exception as e:
            if (hasattr(e, "strerror")):
                print(f"{e.__class__.__name__}, -- strerror: {e.strerror}")
            else:
                print(f"Error {e.__class__.__name__}")
            return None
        print(f"Loading image of dimensions {im.shape[0]} x {im.shape[1]}")
        return im

    def display(self, array):
        plt.imshow(array, interpolation='nearest')
        plt.axis('off')
        plt.show()

class ColorFilter():
    def invert(self, array):
        """
        Inverts the color of the image received as a numpy array.
        Args:
        -----
        array: numpy.ndarray corresponding to the image.
        Return:
        -------
        array: numpy.ndarray corresponding to the transformed image.
        None: otherwise.
        Raises:
        -------
        This function should not raise any Exception.
        """
        if (not isinstance(array , np.ndarray)):
            return None
        if (len(array.shape) != 3):
            return None
        if (arr.shape[2] != 4):
            return None
        m_invert = np.copy(array)
        for lin in m_invert:
            for col in lin:
                col[0] = 1 - col[0]
                col[1] = 1 - col[1]
                col[2] = 1 - col[2]
        return m_invert
    
    def to_blue(self, array):
        """
        Applies a blue filter to the image received as a numpy array.
        Args:
        -----
        array: numpy.ndarray corresponding to the image.
        Return:
        -------
        array: numpy.ndarray corresponding to the transformed image.
        None: otherwise.
        Raises:
        -------
        This function should not raise any Exception.
        """
        if not isinstance(array, np.ndarray):
            return None
        if (len(array.shape) != 3):
            return None
        if (arr.shape[2] != 4):
            return None


        m_blue = np.copy(array)
        print(m_blue.shape)
        x = 0
        for lin in array:
            b = array[x][:, 2]
            t = array[x][:, 3]
            res = np.dstack((np.zeros(array.shape[1]), np.zeros(array.shape[1]), b, t))
            m_blue[x] = res
            x = x + 1

        return m_blue

    def to_green(self, array):
        """
        Applies a green filter to the image received as a numpy array.
        Args:
        -----
        array: numpy.ndarray corresponding to the image.
        Return:
        -------
        array: numpy.ndarray corresponding to the transformed image.
        None: otherwise.
        Raises:
        -------
        This function should not raise any Exception.
        """
        if not isinstance(array, np.ndarray):
            return None
        if (len(array.shape) != 3):
            return None
        if (arr.shape[2] != 4):
            return None
        m_green = np.copy(arr)

        for lin in m_green:
            for col in lin:
                col[0] = 0
                col[2] = 0
        return m_green
    def to_red(self, array):
        """
        Applies a red filter to the image received as a numpy array.
        Args:
        -----
        array: numpy.ndarray corresponding to the image.
        Return:
        -------
        array: numpy.ndarray corresponding to the transformed image.
        None: otherwise.
        Raises:
        -------
        This function should not raise any Exception.
        """
        if not isinstance(array, np.ndarray):
            return None
        if (len(array.shape) != 3):
            return None
        if (arr.shape[2] != 4):
            return None
        base = np.copy(array)
        m_blue = ColorFilter.to_blue(self, array)
        m_green = ColorFilter.to_green(self, array)
        
        

imp = ImageProcessor()

arr = imp.load('elon_canaGAN.png')

cf = ColorFilter()

#imp.display(cf.invert(arr))
#imp.display(cf.to_blue(arr))
#imp.display(cf.to_green(arr))
imp.display(cf.to_red(arr))

print(arr.shape)


