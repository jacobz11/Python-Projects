import pandas
import datetime as dt
import smtplib
from random import choice

month = dt.datetime.now().month
day = dt.datetime.now().day
MY_GMAIL = "jacobzak11@gmail.com"
PASSWORD = "xtogtvvuslejntkj"

data = pandas.read_csv("birthdays.csv")
birthdays = {row["name"]: row["email"] for (idx, row) in data.iterrows() if row["day"] == day and row["month"] == month}
b_letters = ["letter_1.txt", "letter_2.txt", "letter_3.txt"]

for name, email in birthdays.items():
    with open(f"./letter_templates/{choice(b_letters)}") as file:
        data_letter = file.read()
    final_letter = data_letter.replace("[NAME]", name.title())
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=MY_GMAIL, password=PASSWORD)
        connection.sendmail(from_addr=MY_GMAIL,
                            to_addrs=email,
                            msg=f"Subject:Happy Birthday!\n\n{final_letter}".encode("utf8"))
