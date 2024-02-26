import time
from turtle import Screen
from car_manager import CarManager
from player import Player
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
tim = Player()
car_manager = CarManager()
car_manager.hideturtle()
scoreboard = Scoreboard()
screen.listen()
screen.onkey(tim.move, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.create_car()
    car_manager.move_cars()

    for car in car_manager.cars:
        if car.distance(tim) < 20:
            game_is_on = False
            scoreboard.game_over()

    if tim.is_finish():
        tim.reset_position()
        car_manager.level_up()
        scoreboard.increase_level()
screen.exitonclick()
