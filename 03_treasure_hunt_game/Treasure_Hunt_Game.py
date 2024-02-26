print('Welcome to treasure island.\nYour mission is to find the treasure.\n')
left_right = input('Type L to go left or R to go right\n')
if left_right == 'L':
    swim_wait = input('Type S to swim or W to wait\n')
    if swim_wait == 'S':
        print('Game Over')
    elif swim_wait == 'W':
        color = input('Which door? Type red, blue or yellow\n')
        if color == 'red':
            print('Game Over')
        elif color == 'yellow':
            print('You Win!')
        elif color == 'blue':
            print('Game Over')
        else:
            print('Game Over')
else:
    print('Game Over')
