from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet.", prompt="Which turtle will win the race? Enter a color: (red, blue, green, yellow, purple, orange) ")
screen.colormode(255)
y_pos = -70
turtle_race = False

red = Turtle()
blue = Turtle()
green = Turtle()
yellow = Turtle()
purple = Turtle()
orange = Turtle()
turtles = [{"turtle": red, "color": "red", "route": 0},
           {"turtle": blue, "color": "blue", "route": 0},
           {"turtle": green, "color": "green", "route": 0},
           {"turtle": yellow, "color": "yellow", "route": 0},
           {"turtle": purple, "color": "purple", "route": 0},
           {"turtle": orange, "color": "orange", "route": 0}]

for turtle_starting in turtles:
    turtle_starting["turtle"].penup()
    turtle_starting["turtle"].shape("turtle")
    turtle_starting["turtle"].color(turtle_starting["color"])
    turtle_starting["turtle"].setpos(x= -240,y= y_pos)
    y_pos += 30

if user_bet:
    turtle_race = True

while(turtle_race):
    for turtle in turtles:
        turtle["turtle"].speed("slow")
        route = random.randint(0, 10)
        turtle["turtle"].forward(route)
        turtle["route"] += route
        if turtle["route"] >= 480:
            if user_bet == turtle["color"]:
                print(f"You've win! Turtle {turtle['color']} has won the race.")
                turtle_race = False
                break
            else:
                print(f"You've lost! Turtle {turtle['color']} has won the race.")
                turtle_race = False
                break