from turtle import Turtle as Tr, Screen as Sc

tim = Tr()
tim.color('blue')
for i in range(25):
    tim.forward(5)
    tim.penup()
    tim.forward(5)
    tim.pendown()

screen = Sc()
screen.exitonclick()