# import tkinter
#
# window = tkinter.Tk()
# window.title("My First GUI Program")
# window.minsize(width=500, height=300)
#
# #Label
#
# my_label = tkinter.Label(text="I Am a Label", font=("Arial", 24, "bold"))
# my_label.pack(side= "left")
#
# def my_function(a=1, b=2, c=3):
#     pass

# import turtle
#
# tim = turtle.Turtle()
# tim.write(arg="Huh!")
#
# numbers = []
# def add(*args): #args can have a another name :)
#     sum = 0
#     for n in args:
#         sum += n
#     print(sum)
#
# add(5,7,6,8,9)
#
# #
# def calculate(n, **kwargs):
#     print(kwargs)
#     # for key, value in kwargs.items():
#     #     print(key)
#     #     print(value)
#     n += kwargs["add"]
#     n *= kwargs["multiply"]
#     print(n)
#
#
#     print(kwargs)
#
# calculate(2, add=3, multiply=5)
# #
# # window.mainloop()
#
# class Car:
#
#     def __init__(self, **kw):
#         self.make = kw.get("make")
#         self.model = kw.get("model")
#
# my_car = Car(make="Nissan")
# print(my_car.model)