import requests
from datetime import datetime
import smtplib
import time
MY_LAT = 31.046051
MY_LONG = 34.851612

MY_GMAIL = "jacobzak11@gmail.com"
PASSWORD = "xtogtvvuslejntkj"


def iss_checker():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])
    if MY_LAT - 5 < iss_latitude < MY_LAT + 5 and MY_LONG - 5 < iss_longitude < MY_LONG + 5:
        return True
    return False


parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
}

response_sun = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response_sun.raise_for_status()
data_sun = response_sun.json()
sunrise = int(data_sun["results"]["sunrise"].split("T")[1].split(":")[0])
sunset = int(data_sun["results"]["sunset"].split("T")[1].split(":")[0])

while True:
    time.sleep(60)
    time_now = datetime.now().hour
    if (time_now >= sunset or time_now <= sunrise) and iss_checker():
        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(user=MY_GMAIL, password=PASSWORD)
            connection.sendmail(from_addr=MY_GMAIL,
                                to_addrs=MY_GMAIL,
                                msg=f"Subject:ISS Above!\n\nLook Up!".encode("utf8"))
