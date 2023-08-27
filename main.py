import requests
from twilio.rest import Client

account_sid = 'ACab5108ca96ace2359f6df63b06b901da'
auth_token = '18325eed876cf969426933dcf7e97fd1'

OWM_ENPOINT = "https://api.openweathermap.org/data/2.5/forecast"
api_key = "dc2a69c72991b1dc87850112a2b8a9fe"

parameter = {
    "lat": 14.268924,
    "lon": 121.072060,
    "cnt": 4,
    "appid": api_key
}
# cnt limits how many timestamps it will get. Each timestamp is a 3 hour gap. cnt = 4 is 12 hours (3*4=12)

response = requests.get(OWM_ENPOINT, params=parameter)
response.raise_for_status()

data = response.json()

will_rain = False

for hour in data["list"]:
    if hour["weather"][0]["id"] <= 700:
        will_rain = True

if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        from_="+16185982324",
        body="It's going to rain today! Remember to bring an umbrella!",
        to="+639171725674"
    )
    print(message.status)

print(will_rain)
