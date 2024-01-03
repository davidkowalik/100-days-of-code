import requests
import json
from twilio.rest import Client
import os
import datetime

# openweathermap setup
# api_key = "f0948577a60c4a618eff41de2617ecaa"
api_key = ''
weather_url = "https://api.openweathermap.org/data/2.5/weather"
forecast_url = "https://api.openweathermap.org/data/2.5/forecast"

parameters = {
    "q" : "Niepolomice,pl",
    "appid" : api_key,
    "units" : "metric",
    "lang" : "pl",
    "cnt" : 8,
}

#Twilio setup

account_sid = ''
auth_token = ''



response = requests.get(url=forecast_url, params=parameters)
response.raise_for_status()

message = ""
weather_data = response.json()["list"]
city_data = response.json()["city"]
sunrise_time = datetime.datetime.fromtimestamp(city_data['sunrise']).time()
sunset_time = datetime.datetime.fromtimestamp(city_data['sunset']).time()

temp_min = []
temp_max = []
hhh_repot = []

city_report = f"{city_data['name']},{city_data['country']}, coord: {city_data['coord']}, strefa czasowa: UTC+{int(city_data['timezone']/3600)}, wschód: {sunrise_time}, zachód: {sunset_time}"


for item in weather_data:
    temp_min.append(item["main"]["temp_min"])
    temp_max.append(item["main"]["temp_max"])
    msg = f"{item['dt_txt']} - {item['weather'][0]['description']} -> Temperatura: {item['main']['temp']}C, odczuwalna {item['main']['feels_like']}C, ciśnienie atmosferycznie: {item['main']['grnd_level']}hPa, wilgotność powietrza: {item['main']['humidity']}% "
    hhh_repot.append(msg)


message += f"{city_report}\n"
message += f"Minimalna temperatura w ciągu doby to: {min(temp_min)}C, a maksymalna to:{max(temp_max)}C.\n\n"
for hhh in hhh_repot:
    message += f"{hhh}\n"
print(message)
client = Client(account_sid, auth_token)
message = client.messages \
        .create(
             body=message,
             from_='+',
              to='+'
)
print(message.status)