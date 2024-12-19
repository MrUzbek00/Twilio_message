import requests
from twilio.rest import Client

parameter = {
    "lat": 45.499686,
    "lon" : 7.547327,
    "appid": "", #twilio app id
    "cnt":4
}

twilio_sid = "" #twilio sid 
twilio_auth = "" #twilio authontication 


api_call =  requests.get(url="http://api.openweathermap.org/data/2.5/forecast", params=parameter)
api_call.raise_for_status()
data = api_call.json()
# print(data["list"][0]["weather"][0]["id"])
will_rain = False
for hour_data in data["list"]:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code)< 700:
        will_rain = True
    # else:
    #     print("nothing to worry")
if will_rain:
    client = Client(twilio_sid, twilio_auth)
    message = client.messages.create(
        from_= , #twilio number 
        to= , #recievers number
        body="Bring your umbrella it is going to rain in that place")

    print(message.status)