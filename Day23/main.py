from player import Player
from turtle import Screen
from car import Car
from scoreboard import Scoreboard
import random
import time

screen = Screen()
screen.setup(width= 800, height= 600)
screen.title("Turtler")
screen.tracer(0)

player = Player()
level = Scoreboard((-340, 270))
car_list = []

screen.listen()
screen.onkey(fun= player.move_forward, key= "Up")

move_speed = 5
game_is_on = True
while game_is_on:
    time.sleep(0.1)

    rand_int = random.randint(1, 6)
    if rand_int == 1:
        car_list.append(Car(move_speed))

    for car in car_list :
        car.move_forward()
        if car.distance(player) < 21:
            level.game_over()
            game_is_on = False
        if car.xcor() < -450:
            car.hideturtle()
            car_list.remove(car)

    if player.ycor() > 270:
        player.player_start()
        for cars_in_list in car_list:
            cars_in_list.car_accelerate()
        level.next_level()
        level.screen_update()
        move_speed += 10

    screen.update()
screen.exitonclick()