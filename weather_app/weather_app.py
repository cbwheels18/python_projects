import requests
from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.getenv("API_KEY")

def today_weather():
    city_name = input('What city do you want to look up the weather for? ')
    city_name_formatted = '%20'.join(city_name.split())
    url = f'https://api.openweathermap.org/data/2.5/weather?q={city_name_formatted}&units=imperial&appid={api_key}'

    response = requests.get(url)

    if response.status_code == 200:
        weather = response.json()
        temp = weather['main']['temp']
        print(f'The weather for {city_name} is: ')
        print(f'{temp} °F') 
    else:
        print(f'Error: {response.status_code}')

def get_lat_long():
    city_name = input('What city do you want to look up the weather for? ').strip()
    city_name_formatted = '%20'.join(city_name.split())
    state_code = input('What state do you want to look up the weather for? ').strip()
    country_code = input('What country do you want to look up the weather for? ').strip()
    url = f'http://api.openweathermap.org/geo/1.0/direct?q={city_name_formatted},{state_code},{country_code}&limit=1&units=imperial&appid={api_key}'

    response = requests.get(url)

    if response.status_code == 200:
        lat_lon = response.json()
        weather = get_weather_by_week(lat_lon[0]['lat'], lat_lon[0]['lon'])
        # lon = get_weather_by_week(lat_lon[0]['lon'])
    else:
        print(f'Error: {response.status_code}')

    return weather

#I Guess to use this COSTS money so it fails with 401.
def get_weather_by_week(lat, lon):
    url = f'https://api.openweathermap.org/data/3.0/onecall?lat={lat}&lon={lon}&exclude=minutely,hourly,alerts&units=imperial&appid={api_key}'
    
    response = requests.get(url)

    if response.status_code == 200:
        weather_by_week = response.json()
        print(weather_by_week)
    else:
        print(f'Error: {response.status_code}')

    


print('Welcome to the Weather Data Center!')
print('Enter what you would like to do.')
user_input = input('Would you like to look up the weather for today or for the week? today, week: ')
if user_input == 'today':
    today_weather()
elif user_input == 'week':
    get_lat_long()
else: 
    print('Error, try again.')