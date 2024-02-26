import random
choice = int(input('0 for Rock\n1 for Paper\n2 for Scissors\n'))
random_computer_choice = random.randint(0, 2)
game_list = ['Rock', 'Paper', 'Scissors']
print(f'You chose: {game_list[choice]}')
print(f'Computer chose: {game_list[random_computer_choice]}')
if choice == random_computer_choice:
    print("It's a tie")
if choice == 0 and random_computer_choice == 1:
    print('You lose')
if choice == 0 and random_computer_choice == 2:
    print('You won')
if choice == 1 and random_computer_choice == 0:
    print('You won')
if choice == 1 and random_computer_choice == 2:
    print('You lose')
if choice == 2 and random_computer_choice == 0:
    print('You lose')
if choice == 2 and random_computer_choice == 1:
    print('You won')
