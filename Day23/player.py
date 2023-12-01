from turtle import Turtle

MOVE_DISTANCE = 12.5

class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.setheading(90)
        self.y_pos = -265
        self.x_pos = 0
        self.goto(self.x_pos, self.y_pos)

    def player_start(self):
        self.y_pos = -265
        self.goto(self.x_pos, self.y_pos)

    def move_forward(self):
        self.y_pos += MOVE_DISTANCE
        self.goto(self.x_pos, self.y_pos)