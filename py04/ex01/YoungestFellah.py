from FileLoader import FileLoader
import pandas as pd
import numpy as np
import sys

def youngest_fellah(df, year):
    if not (isinstance(df, pd.DataFrame) or not type(year) is int):
        return None
    #print(df)
    ret = {}
    male = df.loc[(df['Year'] == year) & (df['Sex'] == 'M'), ['Age']]
    female = df.loc[(df['Year'] == year) & (df['Sex'] == 'F'), ['Age']]

    if male.empty:
        mmin = 'no data'
    else:
        mmin = np.amin(male.to_numpy())
    if female.empty:
        fmin = 'no data'
    else:
        fmin = np.amin(female.to_numpy())

    ret["f"] = fmin
    ret["m"] = mmin
    return ret

if __name__ == '__main__':
    path = './athlete_events.csv'
    loader = FileLoader()
    data = loader.load(path)
    if data is None:
        print("problem loading data")
        sys.exit()

    print(youngest_fellah(data, 2004))
