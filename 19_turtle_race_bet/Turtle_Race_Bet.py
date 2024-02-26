from turtle import Turtle as Tr, Screen as Sc
from random import randint

screen = Sc()
screen.setup(width=640, height=480)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Type a color:")

turtle_colors = ['red', 'green', 'blue', 'purple', 'deep pink', 'orange']
turtles = []

x_position = -310
y_position = -150
color_idx = 0

for i in range(6):
    turtles.append(Tr(shape='turtle'))

for i in range(6):
    turtles[i].penup()
    turtles[i].color(turtle_colors[i])
    turtles[i].setpos(x_position, y_position)
    y_position += 50

turtle_positions = []
winner = x_position
finish_line = 290
winner_index = 0
while winner <= finish_line:
    for i in range(len(turtles)):
        turtles[i].forward(randint(1, 10))
        if turtles[i].xcor() > winner:
            winner = turtles[i].xcor()
            winner_index = i

if user_bet == turtles[winner_index].color()[0]:
    print(f"Your {turtles[winner_index].color()[0]} turtle has won! Congrats!")
else:
    print(f"Your turtle lost. The winner is {turtles[winner_index].color()[0]} turtle")
screen.exitonclick()
