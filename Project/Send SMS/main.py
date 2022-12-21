import os
import requests
from twilio.rest import Client


OWM_Endpoint = "https://api.openweathermap.org/data/2.5/onecall"
api_key = os.environ.get('OWM_API_KEY') # Using environment variable -> export OWM_API_KEY={API Key}
account_sid = "AC10c0f590d3118a16821715aae2c053a5"
auth_token = os.environ.get("AUTH_TOKEN") # Using environment variable -> export AUTH_KEY={Authentication Token}

weather_parameters = {
    "lat": 41.878113,
    "lon": -87.629799,
    "exclude": "current,minutely,daily",
    "appid": api_key
}

response = requests.get(url=OWM_Endpoint, params=weather_parameters)
response.raise_for_status()
# print(response.json())
weather_data = response.json()
weather_slice = weather_data["hourly"][:12]

will_rain = False

for hour_data in weather_slice:
    condition_code = hour_data["weather"][0]["id"]
    if condition_code < 700:
        will_rain = True
        
if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages \
                .create(
                     body="It's going to rain today. Remember to bring an ☔️",
                     from_="+18059181349",
                     to="+66955429616"
                 )
    print(message.status)



# condition_code = [hour_data["weather"][0]["id"] for hour_data in weather_slice]
# weather_condition = [weather_data["hourly"][i]["weather"][0]["id"] for i in range(12)]

# for i in condition_code:
#     if i < 700:
#         print("Bring an umbrella.")
#     else:
#         print("It's good to go out.")
    
# if weather_data["hourly"][0]["weather"][0]["id"] < 700:
#     print("bring an umbrella")