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
        # self.parent.protocol("WM_DELETE_WINDOW", self.on_closing_main_window)

        self.websites = tk.StringVar()
        self.tools = PasswordTools()
        self.data = Data()

        self.canvas = Canvas(width=200, height=200, bg=BLACK, highlightthickness=0)
        self.picture_png = PhotoImage(file="logo.png")
        self.canvas.create_image(100, 100, image=self.picture_png)
        self.canvas.grid(row=0, column=1)

        self.entry_website = tk.Entry(self.parent, width=52)
        self.entry_website.grid(row=2, column=1, columnspan=2)
        self.entry_website.focus()

        self.entry_user = tk.Entry(self.parent, width=52)
        self.entry_user.grid(row=3, column=1, columnspan=2)
        self.entry_user.insert(END, string="fromm_daniel@yahoo.de")

        self.entry_pw = Entry(self.parent, width=52)
        self.entry_pw.grid(row=4, column=1, columnspan=2)

        self.label_website = Label(text="Website/URL: ", bg=BLACK, fg=WHITE)
        self.label_website.grid(row=2, column=0)
        self.label_website.config(padx=0, pady=3)

        self.label_user = Label(text="Email/Username: ", bg=BLACK, fg=WHITE)
        self.label_user.grid(row=3, column=0)
        self.label_user.config(padx=0, pady=3)

        self.label_pw = Label(text="Password: ", bg=BLACK, fg=WHITE)
        self.label_pw.grid(row=4, column=0)
        self.label_pw.config(padx=0, pady=3)

        self.button_gen_pw = Button(self.parent, width=44, text="Generate Password", command=self.insert_pw_entry,
                               bg=BLACK, fg=WHITE)
        self.button_gen_pw.grid(row=5, column=1, columnspan=2)

        self.button_add = Button(self.parent, width=44, text="Add Entries", command=self.collect_entries, bg=BLACK, fg=WHITE)
        self.button_add.grid(row=6, column=1, columnspan=2)

        self.button_copy_user = Button(self.parent, text="Copy", command=self.copy_user, bg=BLACK, fg=WHITE, width=4)
        self.button_copy_user.grid(row=3, column=4)

        self.button_copy_pw = Button(self.parent, text="Copy", command=self.copy_pw, bg=BLACK, fg=WHITE, width=4)
        self.button_copy_pw.grid(row=4, column=4)

        self.canvas_oval = Canvas(width=20, height=20, bg=BLACK, highlightthickness=0)
        self.canvas_oval.create_oval(1, 1, 19, 19, outline="black", fill="grey")
        self.canvas_oval.grid(row=7, column=0)
        self.check_status()

        self.label_secure = Label(text="Password\nsecure?", bg=BLACK, fg=WHITE)
        self.label_secure.grid(row=5, column=0)

        self.button_load_file = Button(self.parent, text="Load File", command=self.messagebox_open_json, bg=BLACK, fg=WHITE, width=15)
        self.button_load_file.grid(row=1, column=1)

        self.button_show_item_in_file = Button(self.parent, text="Show Item in File", command=self.check_open_file, bg=BLACK, fg=WHITE, width=15)
        self.button_show_item_in_file.grid(row=1, column=2)

    # def close_slave_window(self):
    #     self.show_window.destroy()
    #
    # def on_closing_main_window(self):
    #     if self.show_window.winfo_exists():
    #         self.show_window.destroy()
    #     self.parent.destroy()

    def check_open_file(self):
        if len(self.data.json_data_path) == 0:
            self.data.open_json_file()
        self.show_data_window()

    def copy_pw(self):
        pyperclip.copy(self.entry_pw.get())

    def copy_user(self):
        pyperclip.copy(self.entry_user.get())

    def collect_entries(self):
        website = self.entry_website.get()
        user = self.entry_user.get()
        pw = self.entry_pw.get()
        self.messagebox_save_file(website, user, pw, self.tools.encrypted_pw)
        self.entry_website.delete(0, END)
        self.entry_pw.delete(0, END)

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

    def show_data_window(self):
        def delete_data():
            self.data.delete_item(self.selected_item)

        def insert_text():
            text_website.configure(state="normal")
            text_user.configure(state="normal")
            text_pw.configure(state="normal")

            if len(text_website.get("1.0", "end-1c")) > 0:
                text_website.delete("1.0", END)
                text_user.delete("1.0", END)
                text_pw.delete("1.0", END)

            text_website.insert(END, self.website_show)
            text_user.insert(END, self.user_show)
            text_pw.insert(END, self.encrypted_pw)

            text_website.configure(state="disabled")
            text_user.configure(state="disabled")
            text_pw.configure(state="disabled")

        def copy_text_website():
            pyperclip.copy(text_website.get("1.0", "end-1c"))
        def copy_text_user():
            pyperclip.copy(text_user.get("1.0", "end-1c"))
        def copy_text_pw():
            pyperclip.copy(text_pw.get("1.0", "end-1c"))

        self.show_window = Tk()
        self.show_window.title("Load Item Data")
        self.show_window.config(padx=50, pady=50, bg=BLACK)

        text_website = Text(self.show_window, wrap="word", height=1, width=52)
        text_website.grid(row=1, column=1, rowspan=2)

        text_user = Text(self.show_window, wrap="word", height=1, width=52)
        text_user.grid(row=2, column=1, rowspan=2)

        text_pw = Text(self.show_window, wrap="word", height=1, width=52)
        text_pw.grid(row=3, column=1, rowspan=2)

        def on_combobox_select(event):
            selected_value = event.widget.get()
            for item in self.data.read_file:
                for key, value in item.items():
                    if key == "Website/URL" and selected_value in value:
                        self.website_show = item["Website/URL"]
                        self.user_show = item["Email/Username"]
                        self.pw_show = item["Password"]
                        self.selected_item = item
                        self.encrypted_pw = self.tools.decrypt_password(self.pw_show)
                        insert_text()

        combobox = ttk.Combobox(self.show_window, width=48, values=self.data.website_option)
        combobox.grid(row=0, column=1, rowspan=2)
        combobox.bind("<<ComboboxSelected>>", on_combobox_select)

        label_load_filedata = tk.Label(self.show_window, text="Load Filedata: ", bg="black", fg="white")
        label_load_filedata.grid(row=0, column=0)

        label_text_website = Label(self.show_window, text="Website/URL: ", bg=BLACK, fg=WHITE)
        label_text_website.grid(row=1, column=0)

        label_text_user = Label(self.show_window, text="Email/Username: ", bg=BLACK, fg=WHITE)
        label_text_user.grid(row=2, column=0)

        label_text_pw = Label(self.show_window, text="Password: ", bg=BLACK, fg=WHITE)
        label_text_pw.grid(row=3, column=0)

        data_load_copy_user = Button(self.show_window, text="Copy", command=copy_text_user, bg=BLACK, fg=WHITE, width=4)
        data_load_copy_user.grid(row=2, column=3)

        data_load_copy_pw = Button(self.show_window, text="Copy", command=copy_text_pw, bg=BLACK, fg=WHITE, width=4)
        data_load_copy_pw.grid(row=3, column=3)

        data_load_copy_pw = Button(self.show_window, text="Copy", command=copy_text_website, bg=BLACK, fg=WHITE, width=4)
        data_load_copy_pw.grid(row=1, column=3)

        data_load_delete_item = Button(self.show_window, text="Delete Item", command=delete_data, bg=BLACK, fg=WHITE, width=4)
        data_load_delete_item.grid(row=4, column=2)

        self.show_window.mainloop()

    def messagebox_save_file(self, website, user, password, password_encrypt):
        try:
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
        except Exception as e:
            messagebox.showinfo(title="Error!", message=f"An error occurred: {e}")

    def messagebox_open_json(self):
            try:
                self.data.open_json_file()
                if self.data.read_file:
                    messagebox.showinfo(title="Success!", message="File loaded successfully.")
            except FileNotFoundError:
                messagebox.showinfo(title="Error!", message="File not found.")
            except json.JSONDecodeError:
                messagebox.showinfo(title="Error!", message="Could not decode JSON.")
            except Exception as error:
                messagebox.showinfo(title="Error!", message=f"An error occurred: {error}")






