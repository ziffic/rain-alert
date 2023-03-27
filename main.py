import requests

api_key = "23ca05ea06f23b11598c6476ee4eb7c6"
MY_LAT = 33.787914
MY_LNG = -117.853104

parameters = {
    "api_key": api_key,
    "lat": MY_LAT,
    "lon": MY_LNG
}

weather_response = requests.get(url=f"https://api.openweathermap.org/data/2.5/weather?"
                                    f"lat={MY_LAT}&"
                                    f"lon={MY_LNG}&"
                                    f"appid={api_key}")
weather_response.raise_for_status()
weather_data = weather_response.json()

print(weather_data)
