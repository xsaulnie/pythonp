from FileLoader import FileLoader
import pandas as pd
import sys

def how_many_medals_by_country(df, name):
    if not type(name) is str or not isinstance(df, pd.DataFrame):
        return None
    #print(df.loc[:, ["Sport"]].drop_duplicates(subset=["Sport"]).to_numpy())
    team_sports = ['Basketball', 'Football', 'Tug-Of-War', 'Badminton', 'Handball', 'Water Polo', 'Hockey', 'Rowing', 'Bobsleight', 'Volleyball', 'Synchronized Swimming', 'Baseball', 'Rugby Sevens', 'Beach Volleyball', 'Curling', 'Rugby', 'Lacrosse', 'Polo']
    ret = {}

    years = df.loc[df["Team"] == name, ["Year"]].drop_duplicates(subset=["Year"]).to_numpy()
    #self.info = df.loc[:, ["Year", "City"]].drop_duplicates(subset=["Year"])
    for y in years:
        ret[y[0]] = {'G' : 0, 'S' : 0, 'B' : 0}

    def to_medal(m):
        if m == "Gold":
            return 'G'
        elif m == "Silver":
            return 'S'
        elif m == "Bronze":
            return 'B'

    medals = df.loc[(df["Team"] == name) , ["Year", "Medal", "Sport"]]

    #aff = [x for x in medals.to_numpy() if x[1] != 'nan']
    #print (aff)
    print(medals.to_numpy())

    earned_team_sport = []

    for m in medals.to_numpy():
        if (m[2] in team_sports):
            if (m[2] in earned_team_sport):
                continue
            else:
                earned_team_sport.append(m[2])
        if (m[1] == "Gold"):
            ret[m[0]]['G'] = ret[m[0]]['G'] + 1
        elif (m[1] == "Silver"):
            ret[m[0]]['S'] = ret[m[0]]['S'] + 1
        elif (m[1] == "Bronze"):
            ret[m[0]]['B'] = ret[m[0]]['B'] + 1
    
    print(earned_team_sport)

    rmlist = []
    for itkey in ret.keys():
        count = 0
        for me, nb in ret[itkey].items():
            count = count + nb
        if count == 0:
            rmlist.append(itkey)

    for torm in rmlist:
        ret.pop(torm)

    #print(ret)
    return ret


if __name__ == "__main__":
    path = 'athlete_events.csv'
    loader = FileLoader()
    data = loader.load(path)
    if data is None:
        print("Error loading data")
        sys.exit()
    ret = how_many_medals_by_country(data, 'France')
    print(ret[1924])