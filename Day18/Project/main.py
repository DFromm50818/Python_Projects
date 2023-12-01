# from extractor import Extractor
#
# extractor = Extractor()
# extractor.color_extractor()
# paint = extractor.paint_colors
#
# print(paint)
import turtle as t
import random

tim = t.Turtle()
tim.speed("fastest")
tim.hideturtle()
t.colormode(255)
screen = t.Screen()
color_list = [(42, 97, 146), (176, 47, 78), (204, 161, 94), (137, 89, 63), (224, 209, 105), (113, 174, 206), (176, 164, 38), (211, 131, 173), (226, 73, 50), (201, 75, 118), (92, 104, 189), (25, 150, 87), (125, 40, 69), (124, 217, 207), (95, 158, 66), (227, 171, 189), (48, 187, 199), (130, 190, 164), (174, 186, 220), (214, 207, 36), (153, 208, 218), (233, 171, 163), (43, 62, 103), (103, 51, 40), (42, 76, 79), (53, 60, 68), (83, 45, 37), (86, 39, 58), (47, 77, 75)]
y_pos = -250

for columm in range(10):
    tim.penup()
    tim.setpos(-250, y_pos)
    y_pos += 50
    for row in range(10):
        tim.pencolor(random.choice(color_list))
        tim.dot(20)
        tim.forward(50)

screen.exitonclick()