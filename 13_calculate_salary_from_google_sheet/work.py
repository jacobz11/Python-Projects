import gspread
sa = gspread.service_account()
sh = sa.open("SynergyCables")

wks = sh.worksheet("demo")
working_day = wks.get_all_records()

DAY = "day_id"
HOURS = "hours"
ENTER = "enter"
EXIT = "exit"

ADD125 = 1.25
ADD150 = 1.5
ADD175 = 1.75
ADD200 = 2
PER_HOUR = 33.6
ENTER_HOLIDAY = 16
salaries = []
total_salary = 0


def mixed_hours(special_hours, regular_hours):
    return special_hours * PER_HOUR * ADD150 + regular_hours * PER_HOUR


for day in working_day:
    day_salary = 0
    regular = 0
    special = 0
    if 1 <= day[DAY] <= 5:
        if 4 <= day[EXIT] <= 10:
            if 7 <= day[HOURS] <= 9:
                day_salary = 7 * PER_HOUR + (day[HOURS] - 7) * PER_HOUR * ADD125
            elif day[HOURS] > 9:
                day_salary = 7 * PER_HOUR + 2 * PER_HOUR * ADD125 + (day[HOURS] - 9) * PER_HOUR * ADD150
        else:
            if 8 <= day[HOURS] <= 10:
                day_salary = 8 * PER_HOUR + (day[HOURS] - 8) * PER_HOUR * ADD125
            elif day[HOURS] > 10:
                day_salary = 8 * PER_HOUR + 2 * PER_HOUR * ADD125 + (day[HOURS] - 10) * PER_HOUR * ADD150
    elif day[DAY] == 6:
        if day[EXIT] > ENTER_HOLIDAY:
            regular = ENTER_HOLIDAY - day[ENTER]
            special = day[HOURS] - regular
        if 4 <= day[EXIT] <= 10:
            if 7 <= day[HOURS] <= 9:
                if regular <= 0:
                    day_salary = 7 * PER_HOUR * ADD150 + (day[HOURS] - 7) * PER_HOUR * ADD175
                else:
                    day_salary = mixed_hours(special, regular)
            elif day[HOURS] > 9:
                if regular <= 0:
                    day_salary = 7 * PER_HOUR * ADD150 + 2 * PER_HOUR * ADD175 + (day[HOURS] - 9) * PER_HOUR * ADD200
                else:
                    day_salary = mixed_hours(special, regular)
        else:
            if 8 <= day[HOURS] <= 10:
                if regular <= 0:
                    day_salary = 8 * PER_HOUR * ADD150 + (day[HOURS] - 8) * PER_HOUR * ADD175
                else:
                    day_salary = mixed_hours(special, regular)
            elif day[HOURS] > 10:
                if regular <= 0:
                    day_salary = 7 * PER_HOUR * ADD150 + 2 * PER_HOUR * ADD175 + (day[HOURS] - 9) * PER_HOUR * ADD200
                else:
                    day_salary = mixed_hours(special, regular)
    elif day[DAY] == 7:
        if 4 < day[EXIT] < 8:
            regular = day[EXIT] - 4
            special = day[HOURS] - regular
            if 7 <= day[HOURS] <= 9:
                day_salary = (regular - 1) * PER_HOUR + regular * PER_HOUR + (day[HOURS] - regular) * PER_HOUR * ADD150
            elif day[HOURS] > 9:
                day_salary = 7 * PER_HOUR * ADD150 + 2 * PER_HOUR * ADD175 + PER_HOUR * ADD200 + 2 * PER_HOUR
        else:
            if 8 <= day[HOURS] <= 10:
                day_salary = 7 * PER_HOUR * ADD150 + (day[HOURS] - 7) * PER_HOUR * ADD175
            elif day[HOURS] > 10:
                day_salary = 7 * PER_HOUR * ADD150 + 2 * PER_HOUR * ADD175 + (day[HOURS] - 9) * PER_HOUR * ADD200
    salaries.append(day_salary)

for i in range(len(working_day)):
    print(f"{working_day[i]} | Day salary: {salaries[i]:.2f}₪")

for sal in salaries:
    total_salary += sal
print(f"Your total salary for this month is approximately: {total_salary:.2f}₪")
