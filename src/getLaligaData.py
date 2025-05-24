import requests
import pandas as pd
from dotenv import load_dotenv
import os

def getLaligaData():
    load_dotenv()  # Take API from .env
    API_TOKEN = os.getenv('API_TOKEN')
    BASE_URL = "https://api.football-data.org/v4/"


    headers = {'X-Auth-Token': API_TOKEN}
    url = BASE_URL + "competitions/PL/matches"

    response = requests.get(url, headers = headers)
    data = response.json()

    matches = data["matches"]
    print(matches)

    # Extract relevant fields into the list
    match_list = []
    for match in matches:
        match_day = match["matchday"]
        home_team = match["homeTeam"]["name"]
        away_team = match["awayTeam"]["name"]
        home_goals = match["score"]["fullTime"]["home"]
        away_goals = match["score"]["fullTime"]["away"]
        winner = match["score"]["winner"]
        winner_name = "draw"
        
        # Winner of the match
        if (winner == "HOME_TEAM"): 
            winner_name = home_team
        elif (winner == "AWAY_TEAM"):
            winner_name = away_team
        
        # If the match is not played yet
        if (home_goals == None or away_goals == None):
            winner_name = "Not play yet"

        match_list.append({
            'match_day': match_day,
            'home_team': home_team,
            'away_team': away_team,
            'home_goals': home_goals,
            'away_goals': away_goals,
            'winner': winner_name
        })

    df = pd.DataFrame(match_list)
    print(df)