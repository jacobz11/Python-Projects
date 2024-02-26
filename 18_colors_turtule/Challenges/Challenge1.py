from turtle import Turtle as Tr, Screen as Sc

timmy = Tr()
timmy.shape('turtle')
timmy.color('green')

for i in range(4):
    timmy.forward(100)
    timmy.right(90)

timmy.color('red')
timmy.left(60)
timmy.forward(100)
timmy.right(120)
timmy.forward(100)
for i in range(3):
    if i == 0:
        timmy.color('blue')
    if i == 1:
        timmy.color('purple')
    if i == 2:
        timmy.color('deep pink')
    timmy.left(30)
    timmy.forward(100)
    timmy.right(120)
    timmy.forward(100)

screen = Sc()
screen.exitonclick()
