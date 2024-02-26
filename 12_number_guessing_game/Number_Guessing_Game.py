import random
play_again = True
num_of_attempts = 0


def number_guessing_game(attempts):
    while attempts > 0:
        print(f"\nYou have {attempts} attempts remaining to guess a number")
        user_guess = int(input("make a guess: "))
        if user_guess > guess_number:
            print("Too high")
        elif user_guess < guess_number:
            print("Too low")
        else:
            print("You've guessed the number!")
            break
        attempts -= 1
    if attempts == 0:
        print(f"Maybe next time, the number was: {guess_number}")


while play_again:
    restart = input("\nWelcome to the Number Guessing Game! Wanna play? Type 'y' or 'n'\n")
    if restart == 'y':
        play_again = True
        print("I'm thinking of a number between 1 and 100...")
        guess_number = random.randint(1, 100)
        user_difficulty = input("Choose a difficulty. Type 'easy' or 'hard'\n")
        if user_difficulty == 'easy':
            num_of_attempts = 10
            number_guessing_game(num_of_attempts)
        elif user_difficulty == 'hard':
            num_of_attempts = 5
            number_guessing_game(num_of_attempts)
    else:
        play_again = False
        print("Good Bye")
