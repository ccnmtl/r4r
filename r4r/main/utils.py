import requests
from dotenv import load_dotenv
import os

load_dotenv()
COURSEWORKS_API = os.getenv("COURSEWORKS_API")


def fetch_courseworks_data(path):
    response = requests.get(
        f'https://courseworks2.columbia.edu/api/v1/{path}\
            ?per_page=1000&access_token={COURSEWORKS_API}',
        timeout=10)
    if response.status_code == 200:
        return response.json()
    else:
        return None
