import turtle as t
import random

timmy = t.Turtle()

# colours = ["blue", "red", "green", "black", "orange", "grey", "yellow", "goldenrod4"]

# def draw_shape(num_sides):
#     for _ in range(num_sides):
#         angle = 360 / num_sides
#         timmy.forward(100)
#         timmy.right(angle)
#
# for shape_side_n in range(3, 10):
#     timmy.pencolor(random.choice(colours))
#     draw_shape(shape_side_n)

directions = [0 , 90, 180, 270]
t.colormode(255)

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0 ,255)
    return r, g, b

circle_pit = 0

def draw_circle():
    timmy.shape("turtle")
    timmy.speed(0)
    timmy.circle(100)
    timmy.setheading(circle_pit)


# def random_walk():
#     timmy.shape("turtle")
#     timmy.pensize(5)
#     timmy.speed(0)
#     timmy.setheading(random.choice(directions))
#     timmy.forward(30)

for move_direction in range(73):
    # print(type(random_color()))
    timmy.pencolor(random_color())
    draw_circle()
    circle_pit += 5
    # random_walk()

screen = t.Screen()
screen.exitonclick()