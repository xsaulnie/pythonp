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
        ret[y[0]] = {'G' : '0', 'S' : '0', 'B' : '0'}
    print(ret)


if __name__ == "__main__":
    path = 'athlete_events.csv'
    loader = FileLoader()
    data = loader.load(path)
    if data is None:
        print("Error loading data")
        sys.exit()
    how_many_medals_by_country(data, 'France')