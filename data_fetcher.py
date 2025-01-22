# File: data_fetcher.py
import os
import requests
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

API_KEY = os.getenv('API_KEY')
BASE_URL = "https://api.api-ninjas.com/v1/animals?name="

def fetch_data(animal_name):
    """
    Fetches the animal data for the given animal name from the API.
    Returns: a list of animals in the required format or an error message.
    """
    headers = {"X-Api-Key": API_KEY}
    response = requests.get(BASE_URL + animal_name, headers=headers)
    if response.status_code == 200:
        return response.json()
    elif response.status_code == 404:
        return None
    else:
        raise Exception(f"API request failed with status code {response.status_code}: {response.text}")
