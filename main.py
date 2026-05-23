import requests
from twilio.rest import Client

import os

api_key = os.environ.get("OWM_API_KEY")
account_sid = os.environ.get("ACCOUNT_SID")
auth_token = os.environ.get("AUTH_TOKEN")

t_number = os.environ.get("T_NUMBER")
c_number = os.environ.get("C_NUMBER")


MY_LAT = 3.759442
MY_LONG = -56.033664

OWM_Endpoint = "https://api.openweathermap.org/data/2.5/forecast"

weathers_params = {
    "lat": MY_LAT,
    "lon": MY_LONG,
    "appid": api_key,
    "cnt": 4,
}

response = requests.get(url=OWM_Endpoint, params=weathers_params)
response.raise_for_status()
weather_data = response.json()

weather_id_list = [item["weather"][0]["id"] for item in weather_data["list"]]

will_rain = False
for weather_id in weather_id_list:
    if int(weather_id) < 700:
        will_rain = True

if will_rain:
    client = Client(account_sid, auth_token)

    message = client.messages.create(
        body="It's going to rain today. Remember to bring an ☔.",
        from_=twilio_number,
        to=cel_number,
    )

    print(message.status)
