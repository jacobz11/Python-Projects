import requests
import smtplib

MY_LAT = 31.3141
MY_LONG = 34.6203

parameters = {
    "lat": MY_LAT,
    "lon": MY_LONG,
    "appid": "bb7ce6657b4ad188537accac3ebdbf2a",
    "cnt": 4
}

response = requests.get("https://api.openweathermap.org/data/2.5/forecast", params=parameters)
response.raise_for_status()
data = response.json()

My_GMAIL = "pydeveloper102@Gmail.com"
PASSWORD = "mmtzummbeadzndpy"

will_rain = False
weather_list = [weather["weather"][0]["id"] for weather in data["list"]]
for wid in weather_list:
    if wid < 700:
        will_rain = True

if will_rain:
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=MY_GMAIL, password=PASSWORD)
        connection.sendmail(from_addr=MY_GMAIL,
                            to_addrs=MY_GMAIL,
                            msg="Subject: Rainy day!\n\nIt's going to rain today. Grab an ☂️".encode("utf8"))
