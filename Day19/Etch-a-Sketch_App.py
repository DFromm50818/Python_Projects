from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()

def move_forwards():
    tim.forward(10)

def move_backwards():
    tim.backward(10)

def turn_clockwise():
    tim.right(10)

def turn_anti_clockwise():
    tim.left(10)

def clear_screen():
    screen.resetscreen()

screen.listen()
screen.onkeypress(key="w", fun=move_forwards)
screen.onkeypress(key="s", fun=move_backwards)
screen.onkeypress(key="d", fun=turn_clockwise)
screen.onkeypress(key="a", fun=turn_anti_clockwise)
screen.onkey(key="c", fun=clear_screen)
screen.exitonclick()