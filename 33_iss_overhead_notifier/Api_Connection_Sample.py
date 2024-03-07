import requests
from datetime import datetime
response = requests.get("http://api.open-notify.org/iss-now.json")
print(response.raise_for_status())

data = response.json()

longitude = data["iss_position"]["longitude"]
latitude = data["iss_position"]["latitude"]

print(f"longitude: {longitude}")
print(f"latitude: {latitude}")

iss_position = (longitude, latitude)

print(iss_position)
parameters = {
    "lat": 31.046051,
    "lng": 34.851612,
    "formatted": 0
}

response = requests.get(" https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
print(data)
sunrise = data["results"]["sunrise"].split("T")[1].split(":")[0]
sunset = data["results"]["sunset"].split("T")[1].split(":")[0]
print(sunrise)
print(sunset)
time_now = datetime.now()
