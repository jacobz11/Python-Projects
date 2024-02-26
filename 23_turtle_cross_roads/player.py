from turtle import Turtle as Tr
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Tr):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.reset_position()
        self.setheading(90)

    def move(self):
        self.goto(0, self.ycor() + MOVE_DISTANCE)

    def reset_position(self):
        self.goto(STARTING_POSITION)

    def is_finish(self):
        return self.ycor() > FINISH_LINE_Y