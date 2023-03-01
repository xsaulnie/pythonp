from matplotlib import pyplot as plt

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


imp = ImageProcessor()
arr = imp.load('no_exist')
print(arr)

# arr = imp.load('nothing')
# print(arr)

# arr = imp.load('noright')
# print(arr)

arr = imp.load('42AI.png')
print(arr)

imp.display(arr)

