import os

import requests
from dotenv import load_dotenv

load_dotenv()

SESSION_ID = os.getenv("SESSION_ID")
INPUT_URL = os.getenv("INPUT_URL")

cookies = {"session": SESSION_ID}


def get_input(year: int, day: int):
    url = f"{INPUT_URL}/{year}/day/{day}/input"
    x = requests.get(url, cookies=cookies)
    return x.text
