import coffee_machine_data
print("Welcome to coffee machine ☕")
report = coffee_machine_data.resources
profit = 0


def balance_calculation(choice, user_balance):
    if choice != "report":
        print("Please insert coins.")
        quarters = int(input("How many quarters? "))
        dimes = int(input("How many dimes? "))
        nickels = int(input("How many nickles? "))
        pennies = int(input("How many pennies? "))
        user_balance = quarters * 0.25 + dimes * 0.1 + nickels * 0.05 + pennies * 0.01
    return user_balance


def increase_profit():
    global profit
    profit += coffee_machine_data.MENU[user_choice]['cost']


def manage_payments(choice, user_balance):
    if choice != "report":
        user_balance -= coffee_machine_data.MENU[choice]['cost']
        if user_balance >= 0:
            print(f"Here is ${user_balance:.2f} in change.")
            print(f"Here is your {choice} ☕ Enjoy!")
            increase_profit()
        else:
            user_balance += coffee_machine_data.MENU[choice]['cost']
            print(f"You don't have enough money, Money refunded: ${user_balance}")
    return user_balance


def is_sufficient_ingredients(choice, updated_report, user_balance):
    if choice == "latte" or choice == "cappuccino":
        for item in updated_report:
            if user_balance >= 2.5:
                updated_report[item] -= coffee_machine_data.MENU[choice]['ingredients'][item]
                if updated_report[item] < 0:
                    return False
    elif choice == "espresso":
        if user_balance >= 1.5:
            updated_report['water'] -= coffee_machine_data.MENU['espresso']['ingredients']['water']
            updated_report['coffee'] -= coffee_machine_data.MENU['espresso']['ingredients']['coffee']
            if updated_report['water'] < 0 or updated_report['coffee'] < 0:
                return False
    return True


is_enough_ingredients = True
balance = 0
while is_enough_ingredients:
    user_input = input("Turn off the machine? Type 'y' or 'n' ")
    if user_input == 'y':
        is_enough_ingredients = False
    else:
        user_choice = input("What would you like? (espresso/latte/cappuccino): ")
        if user_choice == "report":
            for ingredient in report:
                print(f"{ingredient.capitalize()}: {report[ingredient]}")
            print(f"Money: ${profit:.2f}")
        balance = balance_calculation(user_choice, balance)
        is_enough_ingredients = is_sufficient_ingredients(user_choice, report, balance)
        if is_enough_ingredients:
            balance = manage_payments(user_choice, balance)
        else:
            print("We're sorry, currently there is not enough ingredients in the machine!")
            print(f"Here is your refund: ${balance:.2f}")
