import imageio as iio
from matplotlib import pyplot as plt
import matplotlib

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
        plt.show()


name = 'nothing'
imp = ImageProcessor()
arr = imp.load(name)
