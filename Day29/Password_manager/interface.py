import tkinter as tk
from tkinter import ttk, messagebox
from tkinter import *
from ttkthemes import *
from tools import PasswordTools
from data import Data
import pyperclip
import json

THEME = "keramik"


class AppWindow(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.selected_item = None
        self.parent = parent
        self.parent.title("Password Manager")
        self.parent.config(padx=50, pady=50)

        self.data_menu = Menu(self.parent)
        self.menu = Menu(self.data_menu, tearoff=0)
        self.menu.add_command(label="Open File", command=self.button_open_pushed)
        self.menu.add_command(label="Exit", command=self.exit_program)
        self.data_menu.add_cascade(label="File", menu=self.menu)
        self.item = Menu(self.data_menu, tearoff=0)
        self.item.add_command(label="Clean Fields", command=self.clear_all_entries)
        self.item.add_command(label="Delete Password", command=self.delete_data_from_file)
        self.data_menu.add_cascade(label="Data", menu=self.item)
        self.parent.config(menu=self.data_menu)

        self.websites_var = tk.StringVar()
        self.tools = PasswordTools()
        self.data = Data()

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

        self.button_copy_website = ttk.Button(self.parent, text="Copy",
                                              command=lambda: pyperclip.copy(self.entry_website.get()), width=6)
        self.button_copy_website.grid(row=2, column=5, sticky="e")

        self.button_copy_user = ttk.Button(self.parent, text="Copy",
                                           command=lambda: pyperclip.copy(self.entry_user.get()), width=6)
        self.button_copy_user.grid(row=3, column=5, sticky="e")

        self.button_copy_pw = ttk.Button(self.parent, text="Copy",
                                         command=lambda: pyperclip.copy(self.entry_pw.get()), width=6)
        self.button_copy_pw.grid(row=4, column=5, sticky="w")

        self.button_gen_pw = ttk.Button(self.parent, width=22, text="Generate Password", command=lambda: self.entry_pw.
                                        insert(END, string=self.insert_generated_password_entry_pw()))
        self.button_gen_pw.grid(row=6, column=3, sticky="w")

        self.button_add = ttk.Button(self.parent, text="Save Password",
                                     command=lambda: self.button_saved_pushed(
                                         self.entry_website.get(), self.entry_user.get(), self.entry_pw.get()),
                                     width=22)
        self.button_add.grid(row=6, column=4, sticky="w")

        self.combobox = ttk.Combobox(self.parent, width=55, postcommand=self.combobox_load_options)
        self.combobox.grid(row=1, column=3, columnspan=2, sticky="w")
        self.combobox.bind("<<ComboboxSelected>>", self.on_combobox_select)

        self.label_load_item = ttk.Label(self.parent, text="Saved Passwords: ")
        self.label_load_item.grid(row=1, column=2, sticky="w")

        self.label_security_step = ttk.Label(self.parent)
        self.label_security_step.grid(row=5, column=3, sticky="w")

        self.canvas.lower(self.parent)

        self.parent.protocol("WM_DELETE_WINDOW", self.exit_program)

        self.check_status()
        self.apply_theme()

    def apply_theme(self):
        style = ThemedStyle(self.parent)
        style.set_theme(THEME)
        self.parent.config(bg=style.lookup('TFrame', 'background'))
        self.canvas.config(bg=style.lookup('TLabel', 'background'))

    def check_status(self):
        self.parent.after(500, self.check_status)
        self.security_light_update(self.tools.password_check(self.entry_pw.get()))

    def no_file_found(self):
        try:
            file_not_found = messagebox.askokcancel(title="No file found!", message="Do you want to create a file "
                                                                                    "press Ok or load a file "
                                                                                    "press Cancel")
            if file_not_found:
                self.data.create_file()
            else:
                self.button_open_pushed()
        except Exception as error:
            messagebox.showinfo(title="Error!", message=f"An error occurred: {error}")

    def exit_program(self):
        response = messagebox.askokcancel(title="Quit program? ",
                                          message=f"All unsaved Data are lost.")
        if response:
            exit()
        else:
            return None

    def combobox_load_options(self):
        try:
            self.combobox["values"] = self.data.load_website_options()
        except Exception as error:
            messagebox.showinfo(title="Error!", message=f"An error occurred: {error}")

    def button_saved_pushed(self, website, user, password):
        try:
            password_encrypt = self.tools.encrypt_password(password)
            if not all([website, user, password, password_encrypt]):
                return messagebox.showerror(title="Error!", message="The data could not be saved. "
                                                                    "Please fill out all entries.")
            if self.data.json_data_path is False:
                self.no_file_found()
            self.data.save_new_data(website, user, password_encrypt)
            messagebox.showinfo(title="Success!", message=f"Website/URL: {website} \nLogin: {user} \nPassword: "
                                                          f"{password} saved successfully.")
            self.clear_all_entries()
        except Exception as error:
            messagebox.showinfo(title="Error!", message=f"An error occurred: {error}")

    def button_open_pushed(self):
        try:
            self.data.open_json_file()
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
                    website_show = item["Website/URL"]
                    user_show = item["Login"]
                    pw_show = item["Password"]
                    self.selected_item = item
                    encrypted_pw = self.tools.decrypt_password(pw_show)
                    self.insert_text_to_entries(website_show, user_show, encrypted_pw)

    def insert_text_to_entries(self, website, user, password):
        try:
            if len(self.entry_website.get()) or len(self.entry_user.get()) or len(self.entry_user.get()) != 0:
                self.clear_all_entries()
            self.entry_website.insert(END, string=website)
            self.entry_user.insert(END, string=user)
            self.entry_pw.insert(END, string=password)
        except Exception as error:
            messagebox.showinfo(title="Error!", message=f"An error occurred: {error}")

    def insert_generated_password_entry_pw(self):
        self.entry_pw.delete(0, END)
        pw = self.tools.generate_password()
        if len(pw) != 0:
            return pw

    def security_light_update(self, light_status):
        if light_status in ("strong", "medium", "weak"):
            self.label_security_step.config(text=light_status)

    def delete_data_from_file(self):
        check_delete_error = None
        try:
            if self.selected_item is None:
                messagebox.showinfo(title="Error!", message="No Password to delete.")
                check_delete_error = True
            self.data.delete_item(self.selected_item)
            self.data.save_new_data()
            self.clear_all_entries()
        except Exception as error:
            if check_delete_error is not True:
                messagebox.showinfo(title="Error!", message=f"An error occurred: {error}")

    def clear_all_entries(self):
        try:
            self.entry_website.delete(0, END)
            self.entry_user.delete(0, END)
            self.entry_pw.delete(0, END)
        except Exception as error:
            messagebox.showinfo(title="Error!", message=f"An error occurred: {error}")
