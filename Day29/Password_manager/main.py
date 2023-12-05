from tkinter import *
import random

BLACK = "black"
WHITE = "white"

def gen_pw():
    list = "abcdefghijklmnopqrstuvwxyz1234567890?!_-ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    liste = list.split(' ')
    print(liste)
    for i in list:
        if i.isupper():
            print(i)
    # for digit in range(len(list)):
    #     digit_numb =


def save_data():
    save_data = open("data.txt", "a")
    save_data.write(f"{entry_website.get()} | {entry_user.get()} | {entry_pw.get()} \n")
    save_data.close()
    entry_website.delete(0, END)
    # entry_user.delete(0, END)
    entry_pw.delete(0, END)

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50, bg=BLACK)

canvas = Canvas(width=200, height=200, bg=BLACK, highlightthickness=0)
picture_png = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=picture_png)
canvas.grid(column=1, row=0)

entry_website = Entry(window, width=52)
entry_website.grid(row=1, column=1, columnspan=2)
entry_website.focus()

entry_user = Entry(window, width=52)
entry_user.grid(row=2, column=1, columnspan=2)
entry_user.insert(END, string="fromm_daniel@yahoo.de")

entry_pw = Entry(window, width=33)
entry_pw.grid(row=3, column=1)

label_website = Label(text="Website: ", bg=BLACK, fg=WHITE)
label_website.grid(row=1, column=0)
label_website.config(padx=0, pady= 3)

label_user = Label(text="Email/Username: ", bg=BLACK, fg=WHITE)
label_user.grid(row=2, column=0)

label_pw = Label(text="Password: ", bg=BLACK, fg=WHITE)
label_pw.grid(row=3, column=0)

button_gen_pw = Button(window, text="Generate Password", command=gen_pw, bg=BLACK, fg=WHITE)
button_gen_pw.grid(row=3, column=2)

button_add = Button(window, width=44, text="Add", command=save_data, bg=BLACK, fg=WHITE)
button_add.grid(row=4, column=1, columnspan=2)

window.mainloop()
