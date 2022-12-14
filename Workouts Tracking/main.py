import os
import requests
from datetime import datetime

GENDER = "Male"
WEIGHT_KG = "81.5"
HEIGHT_CM = "180"
AGE = "25"

APP_ID = os.environ["NT_APP_ID"]
API_KEY = os.environ["NT_API_KEY"]

exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
sheet_endpoint = "https://api.sheety.co/dc9b0808abdc00ac13094a242e9e073b/myWorkouts/record"

exercise_text = input("Tell me which exercise you did: ")

headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
}

parameters = {
    "query": exercise_text,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE
}

exercise_response = requests.post(exercise_endpoint, json=parameters, headers=headers)
# print(response.status_code)
result = exercise_response.json()

#----------------------------------------------------------------#

today = datetime.now().strftime("%Y-%m-%d")
time = datetime.now().strftime("%X")

sheet_headers = {
    "Authorization": f"Bearer {os.environ['TOKEN']}"
}

for exercise in result["exercises"]:
    sheet_input = {
        "record": {
            "date": today,
            "time": time,
            "exercise": exercise["user_input"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }
    
    sheet_response = requests.post(sheet_endpoint, json=sheet_input, headers=sheet_headers)
    
    print(sheet_response.text)