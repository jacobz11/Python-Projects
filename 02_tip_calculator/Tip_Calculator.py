print('Welcome to the tip calculator.')
total = float(input('What was the total bill?\n'+"$"))
tip_percentage = int(input('What percentage tip would you like to give? 10, 12 or 15?\n'))
num_of_people = int(input('How many people to split the bill?\n'))
tip_percentage /= 100
each_person_payout = total / num_of_people
each_person_final_payout = each_person_payout * tip_percentage + each_person_payout
each_person_final_payout_rounded = "{:.2f}".format(each_person_final_payout)
print(f"Each person should pay: ${each_person_final_payout_rounded}")
