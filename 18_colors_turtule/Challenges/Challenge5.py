from random import randint
from turtle import Turtle as Tr, Screen as Sc, colormode

colormode(255)
tim = Tr()
tim.speed(100)

for i in range(0, 362, 5):
    tim.color(randint(0, 255), randint(0, 255), randint(0, 255))
    tim.circle(100)
    tim.setheading(i)

screen = Sc()
screen.exitonclick()
