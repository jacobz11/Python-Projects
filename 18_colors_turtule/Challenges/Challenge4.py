import random
from random import randint
from turtle import Turtle as Tr, Screen as Sc, colormode

colormode(255)
tim = Tr()
tim.pensize(15)
tim.speed(25)
sides = [0, 90, 180, 270]

for i in range(200):
    tim.setheading(random.choice(sides))
    tim.color(randint(0, 255), randint(0, 255), randint(0, 255))
    tim.forward(30)

screen = Sc()
screen.exitonclick()
