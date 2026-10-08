import requests
from dotenv import load_dotenv
import os

load_dotenv()
COURSEWORKS_API = os.getenv("COURSEWORKS_API")


def fetch_courseworks_data(path: str) -> object | None:
    """Fetch Courseworks data according to the path"""
    response = requests.get(
        f'https://courseworks2.columbia.edu/api/v1/{path}?per_page=1000',
        timeout=10, headers={'Authorization': f'Bearer {COURSEWORKS_API}'})
    if response.status_code == 200:
        return response.json()
    else:
        return None


def get_ll(instance) -> list:
    arr = []
    target = instance
    try:
        while target is not None:
            arr.append(target)
            target = target.next
    except AttributeError:
        pass
    return arr
