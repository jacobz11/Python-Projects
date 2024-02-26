from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


make_coffee = CoffeeMaker()
money_machine = MoneyMachine()
coffee_type = Menu()
options = Menu().get_items()
is_turn_on = True
while is_turn_on:
    user_choice = input(f"What would you like? ({options}): ")
    if user_choice == "report":
        make_coffee.report()
        money_machine.report()
    elif user_choice == "espresso" or user_choice == "latte" or user_choice == "cappuccino":
        drink = coffee_type.find_drink(user_choice)
        if make_coffee.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
            make_coffee.make_coffee(drink)
    user_input = input("Turn off the machine? Type 'y' or 'n' ")
    if user_input == 'y':
        is_turn_on = False
    elif user_input == 'n':
        is_turn_on = True
    else:
        print("Wrong input")
