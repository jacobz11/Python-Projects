import game_data
import random


def an_or_a(famous_description):
    an = 'a'
    match famous_description[0]:
        case 'a':
            an = 'an'
        case 'o':
            an = 'an'
        case 'e':
            an = 'an'
        case 'i':
            an = 'an'
        case 'u':
            an = 'an'
    return an


def check_if_same(first, second, updated_data):
    while first == second:
        second = random.choice(updated_data)
    if first != second:
        return second


def higher_lower(data_of_game):
    game_over = False
    score = 0
    updated_game_data = []
    for data in data_of_game:
        updated_game_data.append(data)
    first_famous = random.choice(updated_game_data)
    second_famous = random.choice(updated_game_data)
    second_famous = check_if_same(first_famous, second_famous, updated_game_data)
    while not game_over:
        first_description = str(first_famous['description']).lower()
        second_description = str(second_famous['description']).lower()
        print(f"\nCompare A: {first_famous['name']}, {an_or_a(first_description)} {first_famous['description']}, "
              f"from {first_famous['country']}")
        print("VS")
        print(f"Compare B: {second_famous['name']}, {an_or_a(second_description)} {second_famous['description']}, "
              f"from {second_famous['country']}")

        user_guess = input("Who has more followers? Type 'A' or 'B': ").lower()

        if first_famous['follower_count'] > second_famous['follower_count']:
            if user_guess == 'a':
                score += 1
                print(f"You're right! Current score: {score}")
            elif user_guess == 'b':
                game_over = True
                print(f"That's not correct. Your final score: {score}")
        elif first_famous['follower_count'] < second_famous['follower_count']:
            if user_guess == 'a':
                game_over = True
                print(f"That's not correct. Your final score: {score}")
            elif user_guess == 'b':
                score += 1
                print(f"You're right! Current score: {score}")
        first_famous_idx = updated_game_data.index(first_famous)
        updated_game_data.pop(first_famous_idx)
        print(f"Famous list length = {len(updated_game_data)}")
        first_famous = second_famous
        second_famous = random.choice(updated_game_data)
        second_famous = check_if_same(first_famous, second_famous, updated_game_data)


exit_game = False
while not exit_game:
    restart = input("\nWelcome to higher lower game! Wanna play? Type 'y' or 'n'\n")
    if restart == 'y':
        higher_lower(game_data.data)
        exit_game = False
    else:
        exit_game = True
