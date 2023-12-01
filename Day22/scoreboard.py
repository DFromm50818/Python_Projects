from turtle import Turtle


ALIGMENT = "center"
FONT = ("Arial", 30, "normal")

class Scoreboard(Turtle):
    def __init__(self, coords):
        super().__init__()
        self.scoreboard_coords = coords
        self.score_points = 0
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(self.scoreboard_coords)
        self.screen_update()

    def middle_bar(self):
        self.right(90)
        for _ in range(30):
            self.forward(10)
            self.pendown()
            self.forward(10)
            self.penup()

    def screen_update(self):
        self.write(arg=self.score_points, align=ALIGMENT, font=FONT)

    def add_point(self):
        self.score_points += 1
        self.clear()
        self.screen_update()
