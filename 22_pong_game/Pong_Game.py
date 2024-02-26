from turtle import Screen as Sc
from paddle import Paddle as Pd
from ball import Ball as Bl
from scoreboard import Scoreboard as Sb
import time
screen = Sc()
screen.title("Pong")
screen.setup(width=1280, height=720)
screen.bgcolor("black")
screen.tracer(0)

r_paddle = Pd((620, 0))
l_paddle = Pd((-630, 0))
ball = Bl()
scoreboard = Sb()
screen.listen()
# player 1
screen.onkeypress(r_paddle.go_up, "Up")
screen.onkeypress(r_paddle.go_down, "Down")
# player 2
screen.onkeypress(l_paddle.go_up, "w")
screen.onkeypress(l_paddle.go_down, "s")
game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()
    if ball.ycor() > 345 or ball.ycor() < -345:
        ball.bounce_vertical()
    if ball.xcor() > 600 and ball.distance(r_paddle) < 40 or ball.xcor() < -610 and ball.distance(l_paddle) < 40:
        ball.bounce_horizontal()
    if ball.xcor() > 660:
        ball.reset_position()
        scoreboard.l_point()
    if ball.xcor() < -660:
        ball.reset_position()
        scoreboard.r_point()
screen.exitonclick()
