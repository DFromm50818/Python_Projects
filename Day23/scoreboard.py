from turtle import Turtle
from car import Car

class Scoreboard(Turtle):
    def __init__(self, coords):
        super().__init__()
        self.level = 1
        self.hideturtle()
        self.penup()
        self.goto(coords)
        self.screen_update()

    def game_over(self):
        self.goto(0, 0)
        self.write(arg= "Game Over", align= "center", font=("Arial", 25, "normal"))

    def screen_update(self):
        self.write(arg=f"Level: {self.level}", align="center", font=("Arial", 20, "normal"))

    def next_level(self):
        self.level += 1
        self.clear()
        self.screen_update()




