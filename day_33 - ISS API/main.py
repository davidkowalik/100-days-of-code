import requests
from datetime import datetime
import time
import smtplib

MY_LAT = 50.033112
MY_LNG = 20.217400
MY_EMAIL= "python.study@gmail.com"
PASSWORD = ""

def is_iss_over():
    response = requests.get(url='http://api.open-notify.org/iss-now.json')
    response.raise_for_status()

    data = response.json()
    iss_lng = float(data['iss_position']['longitude'])
    iss_lat = float(data['iss_position']['latitude'])
    iss_position = (iss_lat, iss_lng)

    print(iss_position)

    if abs(MY_LAT - iss_lat) < 5 and abs(MY_LNG - iss_lng) < 5:
        return True
    else:
        return False

def is_night():
    parameters = {
        "lat":MY_LAT,
        "lng":MY_LNG,
        "formatted":0,
    }

    niep_response = requests.get(url='https://api.sunrise-sunset.org/json', params=parameters)
    niep_response.raise_for_status()

    data = niep_response.json()
    sunrise_h = int(data['results']['sunrise'].split('T')[1].split(':')[0])
    sunset_h = int(data['results']['sunset'].split('T')[1].split(':')[0])

    print(f"Sunrise: {sunrise_h}")
    print(f"Sunset: {sunset_h}")
    hour_now = datetime.utcnow().hour
    print(hour_now)
    if sunrise_h >= hour_now or sunset_h <= hour_now:
        return True
    else:
        return False

print(is_iss_over())
print(is_night())

while True:

    if is_iss_over() and is_night():

        message = f"Subject:Look up!!\n\nISS over You."

        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(user=MY_EMAIL, password=PASSWORD)
            connection.sendmail(from_addr=MY_EMAIL, to_addrs=to, msg=message)
    
    time.sleep(60)