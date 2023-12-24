import tkinter as tk
from tkinter import ttk, messagebox
from tkinter import *
from ttkthemes import *
from tools import PasswordTools
from data import Data
import pyperclip
import json

THEME = "keramik"


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
        self.parent.config(padx=50, pady=50)

        self.data_menu = Menu(self.parent)
        self.data = Menu(self.data_menu, tearoff=0)
        self.data.add_command(label="Open File", command=self.open_json)
        self.data.add_command(label="Exit", command=self.exit_program)
        self.data_menu.add_cascade(label="File", menu=self.data)
        self.item = Menu(self.data_menu, tearoff=0)
        self.item.add_command(label="Clean Fields", command=self.clear_all_entries)
        self.item.add_command(label="Delete Password", command=self.delete_data)
        self.data_menu.add_cascade(label="Data", menu=self.item)
        self.parent.config(menu=self.data_menu)

        self.websites_var = tk.StringVar()
        self.tools = PasswordTools()
        self.data = Data()
        self.main_window()
        self.check_status()
        self.apply_theme()

    def main_window(self):
        self.canvas = Canvas(self.parent, width=200, height=200, highlightthickness=0)
        self.picture_png = PhotoImage(file="logo.png")
        self.canvas.create_image(100, 100, image=self.picture_png)
        self.canvas.grid(row=1, column=1, rowspan=7, sticky="w")

        self.label_website = ttk.Label(self.parent, text="Website/URL: ", width=20)
        self.label_website.grid(row=2, column=2, sticky="e")

        self.entry_website = ttk.Entry(self.parent, width=58)
        self.entry_website.grid(row=2, column=3, columnspan=2, sticky="w")
        self.entry_website.focus()

        self.label_user = ttk.Label(self.parent, text="Login: ", width=20)
        self.label_user.grid(row=3, column=2, sticky="e")

        self.entry_user = ttk.Entry(self.parent, width=58)
        self.entry_user.grid(row=3, column=3, columnspan=2, sticky="w")

        self.label_pw = ttk.Label(self.parent, text="Password: ", width=20)
        self.label_pw.grid(row=4, column=2, sticky="e")

        self.entry_pw = ttk.Entry(self.parent, width=58)
        self.entry_pw.grid(row=4, column=3, columnspan=2, sticky="w")

        self.label_secure = ttk.Label(self.parent, text="Password secure? ")
        self.label_secure.grid(row=5, column=2, sticky="w")

        self.button_copy_website = ttk.Button(self.parent, text="Copy", command=self.copy_website, width=6)
        self.button_copy_website.grid(row=2, column=5, sticky="e")

        self.button_copy_user = ttk.Button(self.parent, text="Copy", command=self.copy_user, width=6)
        self.button_copy_user.grid(row=3, column=5, sticky="e")

        self.button_copy_pw = ttk.Button(self.parent, text="Copy", command=self.copy_pw, width=6)
        self.button_copy_pw.grid(row=4, column=5, sticky="w")

        self.button_gen_pw = ttk.Button(self.parent, width=22, text="Generate Password", command=self.insert_pw_entry)
        self.button_gen_pw.grid(row=6, column=3, sticky="w")

        self.button_add = ttk.Button(self.parent, text="Save Password", command=self.save_entries, width=22)
        self.button_add.grid(row=6, column=4, sticky="w")

        self.combobox = ttk.Combobox(self.parent, width=55, values=self.data.website_option)
        self.combobox.grid(row=1, column=3, columnspan=2, sticky="w")
        self.combobox.bind("<<ComboboxSelected>>", self.on_combobox_select)

        self.label_load_item = ttk.Label(self.parent, text="Saved Passwords: ")
        self.label_load_item.grid(row=1, column=2, sticky="w")

        self.label_color = ttk.Label(self.parent)
        self.label_color.grid(row=5, column=3, sticky="w")

        self.canvas.lower(self.parent)

    def create_file_window(self):
        self.enter_filenname_window = tk.Toplevel(self.parent)
        self.enter_filenname_window.title("Create File")
        self.enter_filenname_window.config(padx=50, pady=50)

        self.label_enter_name = ttk.Label(self.enter_filenname_window, text="Enter Filename: ")
        self.label_enter_name.grid(row=0, column=0)

        self.entry_name = ttk.Entry(self.enter_filenname_window, width=58)
        self.entry_name.grid(row=0, column=1, columnspan=2)

        self.button_ok = ttk.Button(self.enter_filenname_window, text="Ok", command=self.new_file, width=12)
        self.button_ok.grid(row=2, column=1)

        self.button_cancel = ttk.Button(self.enter_filenname_window, text="Cancel", command=self.name_window, width=12)
        self.button_cancel.grid(row=2, column=2)

        # self.create_file_window().protocol("WM_DELETE_WINDOW", self.new_file)

    def new_file(self):
        self.data.create_file(self.entry_name.get())
        # self.name_window()

    def apply_theme(self):
        style = ThemedStyle(self.parent)
        style.set_theme(THEME)
        self.parent.config(bg=style.lookup('TFrame', 'background'))
        self.canvas.config(bg=style.lookup('TLabel', 'background'))

    def no_file_found(self):
        file_not_found = messagebox.askokcancel(title="No file found!", message="Do you want to create a file "
                                                                                "press Ok or load a file "
                                                                                "press Cancel")
        if file_not_found:
            self.create_file_window()
            # self.data.create_file(self.entry_name.get())
            if self.data.check_file_exists(self.entry_name.get()):
                self.enter_filenname_window.destroy()
        else:
            self.open_json()

    def name_window(self):
        if self.enter_filenname_window.winfo_exists():
            self.enter_filenname_window.destroy()

    def exit_program(self):
        if len(self.entry_website.get()) or len(self.entry_user.get()) or len(self.entry_pw.get()):
            response = messagebox.askokcancel(title="Quit program? ",
                                              message=f"You have entered some details. Are your sure you want to quit?")
            if response:
                exit()
            else:
                return None

    def update_combobox(self):
        self.data.load_website_options()
        new_websites = self.data.website_option
        self.combobox["values"] = new_websites

    def save_entries(self):
        try:
            website = self.entry_website.get()
            user = self.entry_user.get()
            password = self.entry_pw.get()
            password_encrypt = self.tools.encrypt_password(self.entry_pw.get())
            if not all([website, user, password, password_encrypt]):
                return messagebox.showerror(title="Error!", message="The data could not be saved. "
                                                                    "Please fill out all entries.")
            if self.data.json_data_path is False:
                self.no_file_found()
            response = messagebox.askokcancel(title="Are you sure you want to save?",
                                                    message=f"These are the details you entered: \n\nWebsite/URL: "
                                                    f"{website} \nLogin: {user} "
                                                    f"\nPassword: {password} \n\nIs it ok to save?")
            if response:
                self.data.save_new_data(website, user, password_encrypt)
                self.update_combobox()
                self.entry_website.delete(0, END)
                self.entry_user.delete(0, END)
                self.entry_pw.delete(0, END)
                messagebox.showinfo(title="Success!", message="Data saved successfully.")
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
                    self.user_show = item["Login"]
                    self.pw_show = item["Password"]
                    self.selected_item = item
                    self.encrypted_pw = self.tools.decrypt_password(self.pw_show)
                    self.insert_text(self.website_show, self.user_show, self.encrypted_pw)

    def copy_website(self):
        pyperclip.copy(self.entry_website.get())

    def copy_pw(self):
        pyperclip.copy(self.entry_pw.get())

    def copy_user(self):
        pyperclip.copy(self.entry_user.get())

    def insert_pw_entry(self):
        self.entry_pw.delete(0, END)
        pw = self.tools.generate_password()
        if len(pw) != 0:
            self.entry_pw.insert(END, string=pw)

    def security_light_update(self, light_status):
        if light_status == "strong":
            self.label_color.config(text="STRONG")
        elif light_status == "medium":
            self.label_color.config(text="MEDIUM")
        else:
            self.label_color.config(text="WEAK")

    def check_status(self):
        self.security_light_update(self.tools.password_check(self.entry_pw.get()))
        self.parent.after(500, self.check_status)

    def delete_data(self):
        check_delete_error = None
        try:
            if self.selected_item is None:
                messagebox.showinfo(title="Error!", message="No Password to delete.")
                check_delete_error = True
            self.data.delete_item(self.selected_item)
            self.data.save_new_data()
            self.update_combobox()
            self.entry_website.delete(0, END)
            self.entry_user.delete(0, END)
            self.entry_pw.delete(0, END)
            self.combobox.set("")
        except Exception as error:
            if check_delete_error is not True:
                messagebox.showinfo(title="Error!", message=f"An error occurred: {error}")

    def insert_text(self, website, user, password):
        try:
            if len(self.entry_website.get()) or len(self.entry_user.get()) or len(self.entry_pw.get()) != 0:
                self.entry_website.delete(0, END)
                self.entry_user.delete(0, END)
                self.entry_pw.delete(0, END)
            self.entry_website.insert(END, string=website)
            self.entry_user.insert(END, string=user)
            self.entry_pw.insert(END, string=password)
        except Exception as error:
            messagebox.showinfo(title="Error!", message=f"An error occurred: {error}")

    def clear_all_entries(self):
        try:
            self.entry_website.delete(0, END)
            self.entry_user.delete(0, END)
            self.entry_pw.delete(0, END)
        except Exception as error:
            messagebox.showinfo(title="Error!", message=f"An error occurred: {error}")
