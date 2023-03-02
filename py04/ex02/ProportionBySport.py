from FileLoader import FileLoader
import pandas as pd
import sys

def proportion_by_sport(df, year, sport, gender):
    total = df.loc[((df["Year"]) == year) & (df["Sex"] == gender)]
    total_participants = total.drop_duplicates(subset=["Name"]).shape[0]
    sport = df.loc[((df["Year"]) == year) & (df["Sex"] == gender) & (df["Sport"] == sport)]
    sport_participants = sport.drop_duplicates(subset=["Name"]).shape[0] 
    return( sport_participants /  total_participants)

if __name__ == "__main__":
    path='./athlete_events.csv'
    loader = FileLoader()
    data = loader.load(path)
    if data is None:
        sys.exit()
    print(proportion_by_sport(data, 2004, "Tennis", "F"))
