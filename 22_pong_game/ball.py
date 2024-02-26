from turtle import Turtle as Tr


class Ball(Tr):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.shape("circle")
        self.penup()
        self.x_move = 1
        self.y_move = 1
        self.move_speed = 0.01

    def move(self):
        self.goto(self.xcor() + self.x_move, self.ycor() + self.y_move)

    def reset_position(self):
        self.setpos(0, 0)
        self.bounce_horizontal()
        self.move_speed = 0.01

    def bounce_vertical(self):
        self.y_move *= -1

    def bounce_horizontal(self):
        self.x_move *= -1
        self.move_speed *= 0.9
