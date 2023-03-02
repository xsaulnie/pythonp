from FileLoader import FileLoader
import pandas as pandas

def how_many_medals(df, name):
    info = df.loc[df["Name"] == name, ["Year", "Medal"]]

    ret = {}

    keys = (info.drop_duplicates(subset="Year")).to_numpy()

    for event in keys:
        ret[event[0]] = {'G' : 0, 'S': 0, 'B': 0}

    for event in info.to_numpy():
        if (event[1] == 'Gold'):
            ret[event[0]]['G'] = ret[event[0]]['G'] + 1
        elif (event[1] == 'Silver'):
            ret[event[0]]['S'] = ret[event[0]]['S'] + 1
        elif (event[1] == 'Bronze'):
            ret[event[0]]['B'] = ret[event[0]]['B'] + 1

    return ret

if __name__ == "__main__":
    path = './athlete_events.csv'
    loader = FileLoader()
    data = loader.load(path)
    if data is None:
        sys.exit()
    print(how_many_medals(data, 'Kjetil Andr Aamodt'))
    
