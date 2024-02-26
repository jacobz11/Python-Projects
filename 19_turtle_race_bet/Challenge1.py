from turtle import Turtle as Tr, Screen as Sc


tim = Tr()
screen = Sc()


def move_forward():
    tim.forward(10)


def move_backward():
    tim.backward(10)


def clockwise():
    tim.right(10)


def counter_clockwise():
    tim.left(10)


def clear_drawing():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()


screen.listen()
screen.onkey(fun=move_forward, key="w")
screen.onkey(fun=move_backward, key="s")
screen.onkey(fun=clockwise, key="d")
screen.onkey(fun=counter_clockwise, key="a")
screen.onkey(fun=clear_drawing, key="c")

screen.exitonclick()
