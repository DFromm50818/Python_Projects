from tkinter import *

window = Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=300)
window.config(padx=100, pady=200)

# Label
my_label = Label(text="I Am a Label", font=("Arial", 24, "bold"))
# my_label.grid(column=0, row=0)
# my_label.config(padx=20, pady=20)
# my_label.place(x=100, y=200)
my_label.pack()

my_label["text"] = "New Text"
my_label.config(text="New Text")

# Button
def button_clicked():
    my_label.config(text= input.get())

button = Button(window, text="Click Me", command=button_clicked)
# button.grid(column=1, row=1)
button.pack()

# Entry
input = StringVar()
input = Entry(window, textvariable= input)
# input.grid(column=3, row=2)
input.pack()

# New_button
new_button = Button(window, text="New Button", command=button_clicked)
# new_button.grid(column= 2, row= 0)
new_button.pack()



window.mainloop()