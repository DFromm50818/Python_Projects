import tkinter as tk
from tkinter import ttk, messagebox
from tkinter import *
from tools import PasswordTools
from data import Data
import pyperclip

BLACK = "black"
WHITE = "white"

class WindowGUI(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)

        self.parent = parent
        self.parent.title("Password Manager")
        self.parent.config(padx=50, pady=50, bg=BLACK)

        self.websites = tk.StringVar()
        self.tools = PasswordTools()
        self.data = Data()

        self.canvas = Canvas(width=200, height=200, bg=BLACK, highlightthickness=0)
        self.picture_png = PhotoImage(file="logo.png")
        self.canvas.create_image(100, 100, image=self.picture_png)
        self.canvas.grid(column=1, row=0)

        self.entry_website = tk.Entry(self.parent, width=52)
        self.entry_website.grid(row=1, column=1, columnspan=2)
        self.entry_website.focus()

        self.entry_user = tk.Entry(self.parent, width=52)
        self.entry_user.grid(row=2, column=1, columnspan=2)
        self.entry_user.insert(END, string="fromm_daniel@yahoo.de")

        self.entry_pw = Entry(self.parent, width=52)
        self.entry_pw.grid(row=3, column=1, columnspan=2)

        self.label_website = Label(text="Website: ", bg=BLACK, fg=WHITE)
        self.label_website.grid(row=1, column=0)
        self.label_website.config(padx=0, pady=3)

        self.label_user = Label(text="Email/Username: ", bg=BLACK, fg=WHITE)
        self.label_user.grid(row=2, column=0)
        self.label_user.config(padx=0, pady=3)

        self.label_pw = Label(text="Password: ", bg=BLACK, fg=WHITE)
        self.label_pw.grid(row=3, column=0)
        self.label_pw.config(padx=0, pady=3)

        self.button_gen_pw = Button(self.parent, width=44, text="Generate Password", command=self.insert_pw_entry,
                               bg=BLACK, fg=WHITE)
        self.button_gen_pw.grid(row=4, column=1, columnspan=2)

        self.button_add = Button(self.parent, width=44, text="Add Entries", command=self.collect_entries, bg=BLACK, fg=WHITE)
        self.button_add.grid(row=5, column=1, columnspan=2)

        self.canvas_oval = Canvas(width=20, height=20, bg=BLACK, highlightthickness=0)
        self.canvas_oval.create_oval(1, 1, 19, 19, outline="black", fill="grey")
        self.canvas_oval.grid(row=5, column=0)
        self.check_status()

        self.label_secure = Label(text="Password\nsecure?", bg=BLACK, fg=WHITE)
        self.label_secure.grid(row=4, column=0)

        self.button_copy_user = Button(self.parent, text="Copy", command=self.copy_user, bg=BLACK, fg=WHITE, width=4)
        self.button_copy_user.grid(row=2, column=4)

        self.button_copy_pw = Button(self.parent, text="Copy", command=self.copy_pw, bg=BLACK, fg=WHITE, width=4)
        self.button_copy_pw.grid(row=3, column=4)

        self.button_load = Button(self.parent, text="Load", command=self.data.open_json_file, bg=BLACK, fg=WHITE, width=4)
        self.button_load.grid(row=1, column=4)

        if self.data.load_status:
            self.combobox = ttk.Combobox(self.parent, textvariable=self.websites)
            self.combobox.bind("<<ComboboxSelected>>", self.on_combobox_select)
            self.combobox.grid(row=0, column=0)
            self.combobox["values"] = self.data.website_option


    def copy_pw(self):
        pyperclip.copy(self.entry_pw.get())

    def copy_user(self):
        pyperclip.copy(self.entry_user.get())

    def collect_entries(self):
        try:
            website = self.entry_website.get()
            user = self.entry_user.get()
            pw = self.entry_pw.get()
            if not all([website, user, pw]):
                messagebox.showerror(title="Error!",
                                     message="The data could not be saved. Please fill out all entries.")
            else:
                response = messagebox.askokcancel(title="Are you sure you want to save?",
                                                  message=f"These are the details you entered: \n\nWebsite: "
                                                          f"{website} \nEmail: {user} "
                                                          f"\nPassword: {pw} \n\nIs it ok to save?")
                if response:
                    self.data.save_data(website, user, self.tools.encrypted_pw)
                    self.entry_website.delete(0, END)
                    self.entry_pw.delete(0, END)
        except Exception as e:
            messagebox.showinfo(title="Canceling operation!", message="User cancelled operation.")

    def insert_pw_entry(self):
        self.entry_pw.delete(0, END)
        self.tools.generate_password()
        pw = self.tools.pw_user
        if len(pw) != 0:
            self.entry_pw.insert(END, string=pw)

    def canvas_light_update(self, light_status):
        if light_status == "green":
            self.canvas_oval.create_oval(1, 1, 19, 19, outline="black", fill="green")
        elif light_status == "yellow":
            self.canvas_oval.create_oval(1, 1, 19, 19, outline="black", fill="yellow")
        else:
            self.canvas_oval.create_oval(1, 1, 19, 19, outline="black", fill="red")

    def check_status(self):
        password = self.entry_pw.get()
        light_status = self.tools.password_check(password)
        self.canvas_light_update(light_status)
        self.parent.after(500, self.check_status)

    def on_combobox_select(self, event):
        selected_value = self.websites.get()
        print("Ausgewählte Option:", selected_value)