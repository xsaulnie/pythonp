import pandas as pd

class FileLoader:
    def load(self, path):
        if (not type(path) is str):
            return None
        try:
            ret = pd.read_csv(path)
        except:
            return None
        print(f"Loading dataset of dimensions {ret.shape[0]} x {ret.shape[1]}")
        return(ret)
    def display(self, df, n):
        if (not isinstance(df, pd.DataFrame) or not type(n) is int):
            return
        if (n > 0):
            print (df.loc[:n])
        else:
            print(df.loc[df.shape[0] + n:])


if __name__ == "__main__":
    path = "athlete_events.csv"
    loader = FileLoader()
    data = loader.load(path)
    #print(data.shape)
    loader.display(data, 0)