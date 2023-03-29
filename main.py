import requests
import connect
import os
from twilio.rest import Client

MY_LAT = 33.787914
MY_LNG = -117.853104
OMW_Endpoint = "https://api.openweathermap.org/data/2.5/weather"

parameter = {
    "lat": MY_LAT,
    "lon": MY_LNG,
    "appid": connect.api_key
}

response = requests.get(OMW_Endpoint, params=parameter)
response.raise_for_status()
weather_data = response.json()

# print(weather_data)
if weather_data["weather"][0]["id"] <= 700:
    print("Bring an umbrella")
else:
    print("Enjoy the weather.")

APP_ID = os.environ["TWILIO_ACCOUNT_SID"]
API_KEY = os.environ["TWILIO_AUTH_TOKEN"]
client = Client(connect.account_sid, connect.auth_token)

message = client.messages \
                .create(
                     body="Test",
                     from_='+18662711651',
                     to='+17143231961'
                 )

# print(message.status)
