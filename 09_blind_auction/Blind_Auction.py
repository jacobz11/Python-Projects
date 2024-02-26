print('Welcome to blind auction')
ques = 'yes'
bidders = {}
while ques == 'yes':
    user_name = input('What is your name? ')
    bid_amount = input('What is the bid amount? $')
    ques = input('Are there any other bidders? Type yes is so\n')
    bidders[user_name] = bid_amount

highest_bid = 0
highest_key = ''

for key in bidders:
    bidder = int(bidders[key])
    if bidder > highest_bid:
        highest_bid = bidder
        highest_key = key
print(f'The highest bidder is {highest_key} with the bid of {highest_bid}')
