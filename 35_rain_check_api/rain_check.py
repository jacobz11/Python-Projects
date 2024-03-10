import requests
import smtplib
# account_sid = "ACf706b1e14c4ae9ee013c97dfc84aaed9"
# auth_token = "db02e42d2ebcf77469e1ec7044f5d3cc"


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

# 3T3ZV8C9CFC87R5R5ASTVEK1 ---- Recover Twilio Code ----

MY_GMAIL = "jacobzak11@gmail.com"
PASSWORD = "xtogtvvuslejntkj"

will_rain = False
weather_list = [weather["weather"][0]["id"] for weather in data["list"]]
for wid in weather_list:
    # Change this if to wid < 700
    if wid > 803:
        will_rain = True

if will_rain:
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=MY_GMAIL, password=PASSWORD)
        connection.sendmail(from_addr=MY_GMAIL,
                            to_addrs=MY_GMAIL,
                            msg="Subject: Rainy day!\n\nIt's going to rain today. Grab an ☂️".encode("utf8"))
