from turtle import Turtle as Tr, Screen as Sc, colormode
import random

colormode(255)
color_list = [(213, 154, 96), (52, 107, 132), (179, 77, 31), (202, 142, 31), (115, 155, 171), (124, 79, 99),
              (122, 175, 156), (226, 198, 131), (192, 87, 108), (11, 50, 64), (55, 38, 19), (45, 168, 126),
              (47, 127, 123), (200, 121, 143), (168, 21, 29), (228, 92, 77), (244, 162, 160), (38, 32, 35), (2, 25, 24),
              (78, 147, 171), (170, 23, 18), (19, 79, 90), (101, 126, 158), (235, 166, 171), (177, 204, 185),
              (49, 62, 84), (164, 203, 208), (183, 190, 204), (83, 70, 40),
              (11, 112, 106)]
tim = Tr()
x_position = y_position = -200
tim.speed("fastest")
tim.penup()
tim.setpos(x_position, y_position)
tim.hideturtle()

for i in range(1, 101):
    tim.dot(23, random.choice(color_list))
    if not i % 10 == 0:
        tim.forward(50)
    if i % 10 == 0 and i < 100:
        y_position += 50
        tim.setpos(x_position, y_position)

screen = Sc()
screen.exitonclick()
