import requests
import connect
import os
from twilio.rest import Client

OMW_Endpoint = "https://api.openweathermap.org/data/2.5/weather"

parameter = {
    "lat": connect.MY_LAT,
    "lon": connect.MY_LNG,
    "appid": connect.OWM_API_KEY
}

response = requests.get(OMW_Endpoint, params=parameter)
response.raise_for_status()
weather_data = response.json()

print(weather_data)
if weather_data["weather"][0]["id"] <= 700:
    print("Bring an umbrella")
else:
    print("Enjoy the weather.")

APP_ID = os.environ["TWILIO_ACCOUNT_SID"]
API_TOKEN = os.environ["TWILIO_AUTH_TOKEN"]

client = Client(APP_ID, API_TOKEN)

message = client.messages \
                .create(
                     body="Join Earth's mightiest heroes. Like Kevin Bacon.",
                     from_=connect.TWILIO_VIRTUAL_NUMBER,
                     to=connect.TWILIO_VERIFIED_NUMBER
                 )

print(message.sid)
