from turtle import Turtle

starting_position = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:
    def __init__(self):
        self.segments = []
        self. snake_positioning()
        self.head = self.segments[0]

    def snake_positioning(self):
        for position in starting_position:
            self.add_segment(position)

    def add_segment(self, position):
        snake_part = Turtle(shape="square")
        snake_part.color("green")
        snake_part.penup()
        snake_part.goto(position)
        self.segments.append(snake_part)

    def extend(self):
        self.add_segment(self.segments[-1].position())

    def snake_move(self):
        for seg_num in range(len(self.segments) -1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.segments[0].forward(MOVE_DISTANCE)

    def reset(self):
        for seg in self.segments:
            seg.goto(1000, 1000)
        self.segments.clear()
        self.snake_positioning()
        self.head = self.segments[0]

    def snake_up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def snake_down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def snake_left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def snake_right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)


