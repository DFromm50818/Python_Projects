from tkinter import *
from tkinter import messagebox
from random import randint, choice, shuffle
import pyperclip

BLACK = "black"
WHITE = "white"

def generate_password():
    entry_pw.delete(0, END)

    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    pw_new = [choice(letters) for _ in range(randint(8, 10))] + \
             [choice(symbols) for _ in range(randint(2, 4))] + \
             [choice(numbers) for _ in range(randint(2, 4))]

    shuffle(pw_new)
    pw_user = "".join(pw_new)
    entry_pw.insert(0, string=f"{pw_user}")
    pyperclip.copy(pw_user)

def save_data():

    if len(entry_website.get()) == 0 or len(entry_user.get()) == 0 or len(entry_pw.get()) == 0:
        messagebox.showerror(title="Error!", message="The data could not be saved. Please fill out all entries.")

    else:
        rdy_to_save = messagebox.askokcancel(title="Are you sure you want to save?",
                                             message=f"These are the details you entered: \n\nWebsite: "
                                                     f"{entry_website.get()} \nEmail: {entry_user.get()} "
                                                     f"\nPassword: {entry_pw.get()} \n\nIs it ok to save?")

        if rdy_to_save == True:
            with open("data.txt", "a") as save_data:
                save_data.write(f"{entry_website.get()} | {entry_user.get()} | {entry_pw.get()} \n")
                entry_website.delete(0, END)
                # entry_user.delete(0, END)
                entry_pw.delete(0, END)
            messagebox.showinfo(title="Save data", message="Data save success")

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

button_gen_pw = Button(window, text="Generate Password", command=generate_password, bg=BLACK, fg=WHITE)
button_gen_pw.grid(row=3, column=2)

button_add = Button(window, width=44, text="Add", command=save_data, bg=BLACK, fg=WHITE)
button_add.grid(row=4, column=1, columnspan=2)

window.mainloop()
