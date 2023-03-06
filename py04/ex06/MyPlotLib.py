from FileLoader import FileLoader
import pandas as pd
import matplotlib.pyplot as plt
from pandas.api.types import is_numeric_dtype
import sys
import seaborn as sns

class MyPlotLib:
    @staticmethod
    def numericfeatures(data, features):
        if (type(features) is not list):
            return None
        for x in features:
            if (type(x) is not str):
                return None
        if (not isinstance(data, pd.DataFrame)):
            return None
        modifeat  = []
        for feat in features:
            if is_numeric_dtype(data[feat]):
                modifeat.append(feat)
        return modifeat

    def histogram(self, data, features):

        mfeatures = MyPlotLib.numericfeatures(data, features)
        if mfeatures is None:
            return None

        f, sax = plt.subplots(1, len(mfeatures))

        for idx, ax in enumerate(sax):
            ax.hist(data.loc[:, features[idx]].to_numpy())
        plt.show()

    def density(self, data, features):
        mfeatures = MyPlotLib.numericfeatures(data, features)
        if mfeatures is None:
            return None
        sns.kdeplot(data.loc[:, mfeatures])
        plt.show()

    def pair_plot(self, data, features):
        mfeatures = MyPlotLib.numericfeatures(data, features)
        if mfeatures is None:
            return None
        sns.pairplot(data.loc[:, mfeatures])
        plt.show()
    def box_plot(self, data, features):
        mfeatures = MyPlotLib.numericfeatures(data, features)
        if mfeatures is None:
            return None
        sns.boxplot(data.loc[:, mfeatures])
        plt.show()

if __name__ == "__main__":
    loader = FileLoader()
    path = 'athlete_events.csv'
    data = loader.load(path)
    myp = MyPlotLib()

    if data is None:
        print("Error loading file")
        sys.exit()
    myp.box_plot(data, ['Height', 'Weight'])
