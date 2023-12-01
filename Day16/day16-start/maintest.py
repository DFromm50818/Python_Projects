# import another_module
# print(another_module.another_module)
#
# # import turtle
# # timmy = turtle.Turtle()
# # print(timmy)
#
# from turtle import Turtle, Screen
# timmy = Turtle()6
# print(timmy)
# timmy.shape("turtle")
# timmy.color("green")
# timmy.forward(100)
#
# my_screen = Screen()
# print(my_screen.canvheight)
# my_screen.exitonclick()

from prettytable import PrettyTable
table = PrettyTable()
table.add_column("Pokemon Name", ["Pikachu", "Squirtle", "Charmander"])
table.add_column("Type", ["Electric", "Water", "Fire"])
# table.align["Pokemon Name"] = "l"
# table.align["Type"] = "l"
# or
table.align = "l"

print(table)


