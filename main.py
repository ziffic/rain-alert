import requests
import connect

MY_LAT = 33.787914
MY_LNG = -117.853104

weather_response = requests.get(url=f"https://api.openweathermap.org/data/2.5/weather?"
                                    f"lat={MY_LAT}&"
                                    f"lon={MY_LNG}&"
                                    f"appid={connect.api_key}")
weather_response.raise_for_status()
weather_data = weather_response.json()

print(weather_data)
