from turtle import Turtle

MOVE_DISTANCE = 20
MAX_UP = 240
MAX_DOWN = -240

class Paddle(Turtle):
    def __init__(self, coords):
        super().__init__()
        self.add_paddle(coords)

    def add_paddle(self, position):
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid= 5, stretch_len= 1)
        self.penup()
        self.goto(position)

    def paddle_move(self):
        self.paddle_up()

    def paddle_up(self):
        if self.ycor() < MAX_UP:
            new_y = self.ycor() + MOVE_DISTANCE
            self.goto(self.xcor(), new_y)

    def paddle_down(self):
        if self.ycor() > MAX_DOWN:
            new_y = self.ycor() - MOVE_DISTANCE
            self.goto(self.xcor(), new_y)
