import random


def calculate_score(participant):
    score = 0
    for card in participant:
        score += card
    return score


def blackjack(player_cards, dealer_cards, player_score, dealer_score, can_show_card, who_won):
    if player_score == 21 and len(player_cards) == 2:
        who_won["Player"] = True
        return who_won
    if dealer_score == 21 and len(dealer_cards) == 2:
        who_won["Player"] = True
        return who_won
    if player_score > 21:
        if 11 in player_cards:
            player_card_idx = player_cards.index(11)
            switch_ace = input("Do you want to switch your ace card? Type 'y' or 'n'\n")
            if switch_ace == "y":
                player_cards[player_card_idx] = 1
                player_score = calculate_score(player_cards)
                print_scores(player_cards, dealer_cards, player_score, dealer_score, can_show_card=True)
            if player_score > 21:
                who_won["Dealer"] = True
                return who_won
            else:
                draw_another_card(player_score, dealer_score, can_show_card, who_won)
        else:
            who_won["Dealer"] = True
            return who_won
    else:
        draw_another_card(player_score, dealer_score, can_show_card, who_won)


def draw_another_card(player_score, dealer_score, can_show_card, who_won):
    draw_another = input("Do you want to draw another card? Type 'y' or 'n'\n")
    if draw_another == "y":
        player_pick.append(random.choice(cards))
        player_score = calculate_score(player_pick)
        print_scores(player_pick, dealer_pick, player_score, dealer_score, can_show_card=True)
        blackjack(player_pick, dealer_pick, player_score, dealer_score, can_show_card, who_won)
    elif dealer_score > player_score:
        who_won["Dealer"] = True
        print_scores(player_pick, dealer_pick, player_score, dealer_score, can_show_card=True)
        return who_won
    else:
        while dealer_score < 17:
            print("\nThe dealer takes another card...")
            dealer_pick.append(random.choice(cards))
            dealer_score = calculate_score(dealer_pick)
            can_show_card = True
            print_scores(player_pick, dealer_pick, player_score, dealer_score, can_show_card)
        if not can_show_card:
            print_scores(player_pick, dealer_pick, player_score, dealer_score, can_show_card=True)
        if dealer_score > 21:
            who_won["Dealer"] = True
            return who_won
        elif player_score > dealer_score:
            who_won["Player"] = True
            return who_won
        elif player_score < dealer_score:
            who_won["Dealer"] = True
            return who_won
        else:
            return who_won


def print_scores(player_cards, dealer_cards, player_score, dealer_score, can_show_card):
    if can_show_card:
        print(f"Dealer's cards are: {dealer_cards}")
        print(f"Dealer's score is: {dealer_score}")
    else:
        print(f"Dealer's cards are: [{dealer_cards[0]}, ]")
        print(f"Dealer's score is: {dealer_cards[0]}")
    print(f"Your cards are: {player_cards}")
    print(f"Your score is: {player_score}")


play_again = True
while play_again:
    play = input("Do you want to play a game of Blackjack? Type 'y' or 'n'\n")
    if play == 'y':
        play_again = True
        # initialize game with fresh start
        cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
        dealer_pick = [random.choice(cards), random.choice(cards)]
        player_pick = [random.choice(cards), random.choice(cards)]
        win_menu = {
            "Player": False,
            "Dealer": False
        }
        # end initialization
        score_player = calculate_score(player_pick)
        score_dealer = calculate_score(dealer_pick)
        print_scores(player_pick, dealer_pick, score_player, score_dealer, can_show_card=False)
        is_show_card = False
        blackjack(player_pick, dealer_pick, score_player, score_dealer, is_show_card, win_menu)
        if win_menu["Player"]:
            print("Player Wins!")
        elif win_menu["Dealer"]:
            print("Dealer Wins!")
        else:
            print("It's a Draw!")
    else:
        play_again = False
