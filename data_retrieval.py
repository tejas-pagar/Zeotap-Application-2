import requests
import config

BASE_URL = 'http://api.openweathermap.org/data/2.5/weather'

def fetch_weather(city):
    params = {
        'q': city,
        'appid': config.API_KEY,
        'units': 'metric'  # Get temperature in Celsius
    }
    response = requests.get(BASE_URL, params=params)
    
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error fetching data for {city}: {response.status_code}")
        return None
