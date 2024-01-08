import requests
from datetime import datetime


NUTRI_KEY = '0b499597f7fb5b475e955c12196c41a2'
NUTRI_APP_ID = '05b8f36d'
GENDER = 'male'
WEIGHT = 71
HEIGHT = 170
AGE = 30
SHEETY_TOKEN = 'Bearer x3gnnp2UPh8LhYHz*9PB#pM4DMMhm^B!T7PtutY9CLiXsiSsLQW9$wK^'

exercise_text = input("Tell me which exercises you did: ")

nutri_headers = {
    "x-app-id":NUTRI_APP_ID,
    "x-app-key":NUTRI_KEY,
}

nutri_body = {
    "query":str(exercise_text),
    "gender":GENDER,
    "weight_kg":WEIGHT,
    "height_cm":HEIGHT,
    "age":AGE
}
nutri_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"


r = requests.post(url=nutri_endpoint, json=nutri_body, headers=nutri_headers)
r.raise_for_status()
print(r.json())
result = r.json()


today_date = datetime.now().strftime("%d/%m/%Y")
now_time = datetime.now().strftime("%X")

sheety_endpoint = 'https://api.sheety.co/d24005cafc5956c7349822e7aa5b146e/workoutTracking/workouts'

sheety_headers = {
    "Authorization":SHEETY_TOKEN
}

for exercise in result["exercises"]:
    sheety_body = {
            "workout": {
                "date": str(today_date),
                "time": str(now_time),
                "exercise": exercise["name"].title(),
                "duration": exercise["duration_min"],
                "calories": exercise["nf_calories"]
            }
    }
    print(sheety_body)
    sh_r = requests.post(url=sheety_endpoint, json=sheety_body, headers=sheety_headers)
    sh_r.raise_for_status()

#print(sh_r.json())
