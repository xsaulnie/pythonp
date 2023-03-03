from FileLoader import FileLoader
import pandas as pd
import sys
class SpatioTemporalData:
    def __init__(self, df):
        if (not isinstance(df, pd.DataFrame)):
            return
        print(df.loc[:, ["Year", "City"]].drop_duplicates(subset=["Year"]).to_numpy())
        self.info = df.loc[:, ["Year", "City"]].drop_duplicates(subset=["Year"])
    def when(self, location):
        if not type(location) is str or self.info.empty:
            return None
        ret = []
        for x in self.info.to_numpy():
            if x[1] == location:
                ret.append(x[0])
        return ret
    def where(self, date):
        if not type(date) is int or self.info.empty:
            return None
        for x in self.info.to_numpy():
            if x[0] == date:
                return [x[1]]
        return []

if __name__ == "__main__":
    loader = FileLoader()
    path = './athlete_events.csv'
    data = loader.load(path)
    if data is None:
        print("Error opening file")
        sys.exit()
    sp = SpatioTemporalData(data)
    print("Where in 1896 ? ", sp.where(1896))
    print("Where in 2016 ?", sp.where(2016))
    print("When in Athina ?", sp.when('Athina'))
    print("When in Paris ?", sp.when('Paris'))
    print("Where in 2024 ?", sp.where(2024))
    print("When in Toulouse ?", sp.when('Toulouse'))