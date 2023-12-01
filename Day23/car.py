from turtle import Turtle
import random

CAR_COLORS = ["yellow", "blue", "green", "red", "orange", "grey", "purple", "black"]

class Car(Turtle):
    def __init__(self, move_speed):
        super().__init__()
        self.shape("square")
        self.color(random.choice(CAR_COLORS))
        self.shapesize(stretch_len=2)
        self.penup()
        self.setheading(180)
        self.move_speed = move_speed
        self.y_position = 0
        self.x_position = 420
        self.car_pos()
        self.goto(self.x_position, self.y_position)

    def car_pos(self):
        y_pos = random.choice(range(-240, 240, 20))
        self.y_position = y_pos

    def car_accelerate(self):
        self.move_speed += 10

    def move_forward(self):
        self.x_pos = self.xcor()
        self.y_pos = self.ycor()
        self.new_x = self.x_pos - self.move_speed
        self.goto(self.new_x, self.y_pos)
