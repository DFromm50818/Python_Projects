import tkinter as tk
from tkinter import ttk, messagebox
from tkinter import *
from tools import PasswordTools
from data import Data
import pyperclip
import json

BLACK = "black"
WHITE = "white"


class WindowGUI(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.website_show = ""
        self.user_show = ""
        self.pw_show = ""
        self.encrypted_pw = None
        self.selected_item = None
        self.parent = parent
        self.parent.title("Password Manager")
        self.parent.config(padx=50, pady=50, bg=BLACK)

        self.websites = tk.StringVar()
        self.tools = PasswordTools()
        self.data = Data()
        self.main_window()
        self.check_status()

    def main_window(self):
        self.canvas = Canvas(self.parent, width=200, height=200, highlightthickness=0, bg=BLACK)
        self.picture_png = PhotoImage(file="logo.png")
        self.canvas.create_image(100, 100, image=self.picture_png)
        self.canvas.grid(row=1, column=0, rowspan=7, sticky="w")

        self.label_website = Label(self.parent, text="Website/URL: ", width=20, bg=BLACK, fg=WHITE)
        self.label_website.config(padx=0, pady=3)
        self.label_website.grid(row=2, column=2, sticky="e")

        self.entry_website = tk.Entry(self.parent, width=58)
        self.entry_website.grid(row=2, column=3, columnspan=2, sticky="w")
        self.entry_website.focus()

        self.label_user = Label(self.parent, text="Email/Username: ", width=20, bg=BLACK, fg=WHITE)
        self.label_user.grid(row=3, column=2, sticky="e")
        self.label_user.config(padx=0, pady=3)

        self.entry_user = tk.Entry(self.parent, width=58)
        self.entry_user.grid(row=3, column=3, columnspan=2, sticky="w")
        self.entry_user.insert(END, string="fromm_daniel@yahoo.de")

        self.label_pw = Label(self.parent, text="Password: ", width=20, bg=BLACK, fg=WHITE)
        self.label_pw.config(padx=0, pady=3)
        self.label_pw.grid(row=4, column=2, sticky="e")

        self.entry_pw = Entry(self.parent, width=58)
        self.entry_pw.grid(row=4, column=3, columnspan=2, sticky="w")

        self.label_secure = Label(self.parent, text="Password secure? ", bg=BLACK, fg=WHITE)
        self.label_secure.grid(row=5, column=2, sticky="")
        self.label_secure.config(padx=0, pady=3)

        self.button_copy_website = Button(self.parent, text="Copy", command=self.copy_pw, width=4, bg=BLACK, fg=WHITE)
        self.button_copy_website.grid(row=2, column=5, sticky="e")

        self.button_copy_user = Button(self.parent, text="Copy", command=self.copy_user, width=4, bg=BLACK, fg=WHITE)
        self.button_copy_user.grid(row=3, column=5, sticky="e")

        self.button_copy_pw = Button(self.parent, text="Copy", command=self.copy_pw, width=4, bg=BLACK, fg=WHITE)
        self.button_copy_pw.grid(row=4, column=5, sticky="w")

        self.button_gen_pw = Button(self.parent, width=22, text="Generate Password", command=self.insert_pw_entry, bg=BLACK, fg=WHITE)
        self.button_gen_pw.grid(row=5, column=3, sticky="w")

        self.button_add = Button(self.parent, text="Save Item", command=self.save_entries, width=22, bg=BLACK, fg=WHITE)
        self.button_add.grid(row=5, column=4, sticky="w")

        self.button_load_file = Button(self.parent, text="Load File", command=self.open_json, width=15, bg=BLACK, fg=WHITE)
        self.button_load_file.grid(row=1, column=1, sticky="e")

        self.combobox = ttk.Combobox(self.parent, width=55, values=self.data.website_option)
        self.combobox.grid(row=1, column=3, columnspan=2, sticky="w")
        self.combobox.bind("<<ComboboxSelected>>", self.on_combobox_select)

        self.data_load_delete_item = Button(self.parent, text="Delete Item", command=self.delete_data, width=15, bg=BLACK, fg=WHITE)
        self.data_load_delete_item.grid(row=5, column=1, sticky="e")

        self.clear_entries = Button(self.parent, text="Clear Entries", command=self.clear_all_entries, width=15, bg=BLACK, fg=WHITE)
        self.clear_entries.grid(row=3 ,column=1, sticky="e")

        self.label_load_item = Label(self.parent, text="Load Entry in Save ", bg=BLACK, fg=WHITE)
        self.label_load_item.grid(row=1, column=2)

        self.canvas.lower(self.parent)

    def update_combobox(self):
        self.data.load_website_options()
        new_websites = self.data.website_option
        self.combobox["values"] = new_websites

    def save_entries(self):
        try:
            website = self.entry_website.get()
            user = self.entry_user.get()
            password = self.entry_pw.get()
            password_encrypt = self.tools.encrypted_pw
            if not all([website, user, password, password_encrypt]):
                messagebox.showerror(title="Error!",
                                     message="The data could not be saved. Please fill out all entries.")
                return
            response = messagebox.askokcancel(title="Are you sure you want to save?",
                                              message=f"These are the details you entered: \n\nWebsite/URL: "
                                                      f"{website} \nEmail/Username: {user} "
                                                      f"\nPassword: {password} \n\nIs it ok to save?")
            if response:
                json_encrypt_pw = password_encrypt.decode('utf-8')
                new_entry = {"Website/URL": website, "Email/Username": user, "Password": json_encrypt_pw}
                self.data.save_data(new_entry, self.data.read_file)
                messagebox.showinfo(title="Success!", message="Data saved successfully.")
                self.update_combobox()
                self.entry_website.delete(0, END)
                self.entry_pw.delete(0, END)
        except Exception as error:
            messagebox.showinfo(title="Error!", message=f"An error occurred: {error}")

    def open_json(self):
            try:
                self.data.open_json_file()
                if self.data.read_file:
                    messagebox.showinfo(title="Success!", message="File loaded successfully.")
                    self.update_combobox()
            except FileNotFoundError:
                messagebox.showinfo(title="Error!", message="File not found.")
            except json.JSONDecodeError:
                messagebox.showinfo(title="Error!", message="Could not decode JSON.")
            except Exception as error:
                messagebox.showinfo(title="Error!", message=f"An error occurred: {error}")

    def on_combobox_select(self, event):
        selected_value = event.widget.get()
        for item in self.data.read_file:
            for key, value in item.items():
                if key == "Website/URL" and selected_value in value:
                    self.website_show = item["Website/URL"]
                    self.user_show = item["Email/Username"]
                    self.pw_show = item["Password"]
                    self.selected_item = item
                    self.encrypted_pw = self.tools.decrypt_password(self.pw_show)
                    self.insert_text(self.website_show, self.user_show, self.encrypted_pw)

    def copy_pw(self):
        pyperclip.copy(self.entry_pw.get())

    def copy_user(self):
        pyperclip.copy(self.entry_user.get())

    def insert_pw_entry(self):
        self.entry_pw.delete(0, END)
        self.tools.generate_password()
        pw = self.tools.pw_user
        if len(pw) != 0:
            self.entry_pw.insert(END, string=pw)

    def canvas_light_update(self, light_status):
        if light_status == "green":
            self.label_secure.config(padx=0, pady=3, bg="green", fg=WHITE)
            # self.canvas_oval.create_oval(1, 1, 19, 19, outline="black", fill="green")
        elif light_status == "yellow":
            self.label_secure.config(padx=0, pady=3, bg="yellow", fg=WHITE)
            # self.canvas_oval.create_oval(1, 1, 19, 19, outline="black", fill="yellow")
        else:
            self.label_secure.config(padx=0, pady=3, bg="red", fg=WHITE)
            # self.canvas_oval.create_oval(1, 1, 19, 19, outline="black", fill="red")

    def check_status(self):
        password = self.entry_pw.get()
        light_status = self.tools.password_check(password)
        self.canvas_light_update(light_status)
        self.parent.after(500, self.check_status)

    def delete_data(self):
        self.data.delete_item(self.selected_item)
        self.update_combobox()

    def insert_text(self, website, user, password):
        if len(self.entry_website.get()) or len(self.entry_user.get()) or len(self.entry_pw.get()) != 0:
            self.entry_website.delete(0, END)
            self.entry_user.delete(0, END)
            self.entry_pw.delete(0, END)
        self.entry_website.insert(END, string=website)
        self.entry_user.insert(END, string=user)
        self.entry_pw.insert(END, string=password)

    def clear_all_entries(self):
        self.entry_website.delete(0, END)
        self.entry_user.delete(0, END)
        self.entry_pw.delete(0, END)

