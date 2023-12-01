from turtle import Screen
from paddle import Paddle
from scoreboard import Scoreboard
from ball import Ball
import time

game_is_on = True
max_plus_ycor = 280
max_minus_ycor = -280
max_plus_xcor = 400
max_minus_xcor = -400

screen = Screen()
screen.colormode(255)
screen.setup(width= 800, height= 600)
screen.bgcolor("black")
screen.title("Pong Game")
screen.tracer(0)

player = Paddle((-350, 0))
player2 = Paddle((350, 0))

middle_bar = Scoreboard((0, 300))
middle_bar.middle_bar()

ball_coords = (0, 0)
ball = Ball(ball_coords)

player_score = Scoreboard((-50, 250))
player2_score = Scoreboard((50, 250))

screen.listen()
screen.onkeypress(fun= player.paddle_up, key="w")
screen.onkeypress(fun= player.paddle_down, key="s")
screen.onkeypress(fun= player2.paddle_up, key="Up")
screen.onkeypress(fun= player2.paddle_down, key="Down")

while game_is_on:
    time.sleep(0.01)
    screen.update()
    ball.move_ball()

    if ball.ycor() >= max_plus_ycor or ball.ycor() <= max_minus_ycor:
        ball.bounce_y()

    if ball.distance(player2) < 50 and ball.xcor() > 320 or ball.distance(player) < 50 and ball.xcor() < -320:
        ball.bounce_x()
        # ball.speed_up()

    if ball.xcor() > 380:
        ball.reset_position()
        player_score.add_point()
        # ball.speed_reset()

    if ball.xcor() < -380:
        ball.reset_position()
        player2_score.add_point()
        # ball.speed_reset()

screen.exitonclick()