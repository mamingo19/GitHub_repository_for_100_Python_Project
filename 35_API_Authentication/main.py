from twilio.rest import Client
import requests

OWM_Endpoint = "https://api.openweathermap.org/data/2.5/forecast"
api_key = ""
account_sid = ''
auth_token = ''


weather_params = {
    "lat": 10.957413,
    "lon": 106.842690,
    "appid":api_key,
    "cnt": 4,
}

response = requests.get(OWM_Endpoint, params = weather_params)
response.raise_for_status()
weather_data = response.json()
# print(weather_data["list"][0]['weather'][0]["id"])
will_rain = False
for hour_data in weather_data["list"]:
    weather_condition_no = hour_data["weather"][0]["id"]
    if int(weather_condition_no) < 700:
        will_rain = True
if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        from_='whatsapp:',
        body="It's going to rain today. Remember to bring an umbrella",
        to='whatsapp:'
    )
    print(message.status)

