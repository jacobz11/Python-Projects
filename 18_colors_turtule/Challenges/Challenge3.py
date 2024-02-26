from random import randint
from turtle import Turtle as Tr, Screen as Sc, colormode

colormode(255)
tim = Tr()
tim.pensize(3)


def change_random_color():
    tim.color(randint(0, 255), randint(0, 255), randint(0, 255))


for i in range(3, 12):
    change_random_color()
    for j in range(i):
        tim.forward(50)
        tim.right(360/i)
screen = Sc()
screen.exitonclick()
