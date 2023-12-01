from turtle import Turtle

class Ball(Turtle):
    def __init__(self, coords):
        super().__init__()
        self.coords = coords
        self.initialize_ball()
        self.x_move = 4
        self.y_move = 4

    def initialize_ball(self):
        self.shape("circle")
        self.color("white")
        self.penup()
        self.goto(self.coords)

    def move_ball(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce_y(self):
        self.y_move *= -1

    def bounce_x(self):
        self.x_move *= -1

    def reset_position(self):
        self.goto(0, 0)
        self.bounce_x()

    def speed_up(self):
        self.x_move += 0.25
        self.y_move += 0.25

    def speed_reset(self):
        self.y_move = 4
        self.y_move = 4