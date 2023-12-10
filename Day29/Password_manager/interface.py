import tkinter as tk
from tkinter import *
from tools import PasswordTools
from data import Data

from tkinter import messagebox
from tkinter import filedialog
from random import randint, choice, shuffle
import pyperclip
from cryptography.fernet import Fernet
import json
from tkinter import ttk

BLACK = "black"
WHITE = "white"


class WindowGUI(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent
        self.parent.title("Password Manager")
        self.parent.config(padx=50, pady=50, bg=BLACK)
        self.tools = PasswordTools()
        self.data = Data()
        self.gui()
        self.data.open_json_file()
        # self.website = ""
        # self.user = ""
        # self.password = ""



    def gui(self):
        canvas = Canvas(width=200, height=200, bg=BLACK, highlightthickness=0)
        self.picture_png = PhotoImage(file="logo.png")
        canvas.create_image(100, 100, image=self.picture_png)
        canvas.grid(column=1, row=0)

        self.entry_website = tk.Entry(self.parent, width=52)
        self.entry_website.grid(row=1, column=1, columnspan=2)
        self.entry_website.focus()

        self.entry_user = tk.Entry(self.parent, width=52)
        self.entry_user.grid(row=2, column=1, columnspan=2)
        self.entry_user.insert(END, string="fromm_daniel@yahoo.de")

        self.entry_pw = Entry(self.parent, width=52)
        self.entry_pw.grid(row=3, column=1, columnspan=2)
        self.entry_pw.insert(END, string=self.tools.pw_user)

        label_website = Label(text="Website: ", bg=BLACK, fg=WHITE)
        label_website.grid(row=1, column=0)
        label_website.config(padx=0, pady=3)

        label_user = Label(text="Email/Username: ", bg=BLACK, fg=WHITE)
        label_user.grid(row=2, column=0)
        label_user.config(padx=0, pady=3)

        label_pw = Label(text="Password: ", bg=BLACK, fg=WHITE)
        label_pw.grid(row=3, column=0)
        label_pw.config(padx=0, pady=3)

        button_gen_pw = Button(self.parent, width=44, text="Generate Password", command=self.tools.generate_password,
                               bg=BLACK, fg=WHITE)
        button_gen_pw.grid(row=4, column=1, columnspan=2)

        button_add = Button(self.parent, width=44, text="Add Entries", command=self.collect_entries, bg=BLACK,
                            fg=WHITE)
        button_add.grid(row=5, column=1, columnspan=2)

        canvas_oval = Canvas(width=20, height=20, bg=BLACK, highlightthickness=0)
        canvas_oval.create_oval(1, 1, 19, 19, outline="black", fill="green")
        canvas_oval.grid(row=5, column=0)

        label_secure = Label(text="Password\nsecure?", bg=BLACK, fg=WHITE)
        label_secure.grid(row=4, column=0)

        button_copy_user = Button(self.parent, text="Copy", command="copy_user", bg=BLACK, fg=WHITE)
        button_copy_user.grid(row=2, column=4)

        button_copy_pw = Button(self.parent, text="Copy", command="copy_pw", bg=BLACK, fg=WHITE)
        button_copy_pw.grid(row=3, column=4)

        # def copy_pw(self):
        #     pyperclip.copy(WindowGui().password)
        #
        # def copy_user(self):
        #     pyperclip.copy(WindowGui().user)

    def collect_entries(self):
        try:
            website = self.entry_website.get()
            user = self.entry_user.get()
            pw = self.entry_pw.get()
            self.data.save_data(website,user, pw)
            messagebox.showinfo(title="Save data", message="Data save success")
        except:
            messagebox.showerror(title="Error!", message="JSON File could not be read or empty.")
