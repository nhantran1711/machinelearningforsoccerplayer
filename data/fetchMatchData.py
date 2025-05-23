import requests
import pandas as pd
from dotenv import load_dotenv
import os


load_dotenv()  # Take API from .env
API_TOKEN = os.getenv('API_TOKEN')
BASE_URL = "https://api.football-data.org/v4/"


headers = {'X-Auth-Token': API_TOKEN}
url = BASE_URL + "competitions/CL/matches"

response = requests.get(url, headers = headers)
data = response.json()

print(data)