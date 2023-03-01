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

        base[:, :, :3] = base[:, :, :3] - m_green[:, :, :3] - m_blue[:, :, :3]
        return base

    def to_celluloid(self, array):
        """
        Applies a celluloid filter to the image received as a numpy array.
        Celluloid filter must display at least four thresholds of shades.
        Be careful! You are not asked to apply black contour on the object,
        you only have to work on the shades of your images.
        Remarks:
        celluloid filter is also known as cel-shading or toon-shading.
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
        gap = np.linspace(0, 1, num = 5)

        def trf(num):
            if num < gap[1]:
                return gap[0]
            if num < gap[2]:
                return gap[1]
            if num < gap[3]:
                return gap[2]
            return gap[3]

        m_celluloid = np.copy(array)
        for lin in m_celluloid:
            for col in lin:
                col[0] = trf(col[0])
                col[1] = trf(col[1])
                col[2] = trf(col[2])
        return m_celluloid
    def to_grayscale(self, array, filter, **kwargs):
        """
        Applies a grayscale filter to the image received as a numpy array.
        For filter = 'mean'/'m': performs the mean of RBG channels.
        For filter = 'weight'/'w': performs a weighted mean of RBG channels.
        Args:
        -----
        array: numpy.ndarray corresponding to the image.
        filter: string with accepted values in ['m','mean', 'w','weight']
        weights: [kwargs] list of 3 floats where the sum equals to 1,
        corresponding to the weights of each RBG channels.
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
        if (filter != "w" and filter != "weight" and filter != "m" and filter != "mean"):
            return None
        if (filter == "weight" or filter == "w"):
            if not "weights" in kwargs.keys():
                return None
            if (len(kwargs["weights"]) != 3):
                return None
            w = kwargs["weights"]
            for num in w:
                if (not type(num) is float):
                    return None
            if (w[0] + w[1] + w[2] != 1):
                return None
        res = array.astype(float)

        if (filter == "mean" or filter == "m"):        
            for lin in res:
                for col in lin:
                    col[:3] = np.broadcast_to(sum(col[:3]) / 3, (1, 3))
            return res

        for lin in res:
            for col in lin:
                col[:3] = np.broadcast_to(col[0] * w[0] + col[1] * w[1] + col[2] * w[2], (1, 3))
        return res


imp = ImageProcessor()

arr = imp.load('elon_canaGAN.png')

cf = ColorFilter()

inv = cf.invert(arr)
#imp.display(inv)
blue = cf.to_blue(arr)
#imp.display(blue)
green = cf.to_green(arr)
#imp.display(green)
red = cf.to_red(arr)
#imp.display(red)
celluloid = cf.to_celluloid(arr)
#imp.display(celluloid)
gray = cf.to_grayscale(arr, "weight", weights = [0.2, 0.3, 0.5])
#imp.display(gray)

plt.subplot(2, 3, 1)
plt.imshow(gray, interpolation='nearest')
plt.axis('off')
plt.title("Grey Musk")

plt.subplot(2, 3, 2)
plt.imshow(inv, interpolation='nearest')
plt.axis('off')
plt.title("Invert Musk")

plt.subplot(2, 3, 3)
plt.imshow(blue, interpolation='nearest')
plt.axis('off')
plt.title("Blue Musk")

plt.subplot(2, 3, 4)
plt.imshow(green, interpolation='nearest')
plt.axis('off')
plt.title("Green Musk")

plt.subplot(2, 3, 5)
plt.imshow(red, interpolation='nearest')
plt.axis('off')
plt.title("Red Musk")

plt.subplot(2, 3, 6)
plt.imshow(celluloid, interpolation='nearest')
plt.axis('off')
plt.title("Celluloid Musk")

plt.show()

