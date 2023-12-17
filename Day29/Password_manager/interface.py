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
        self.parent.config(padx=50, pady=50)

        self.websites = tk.StringVar()
        self.tools = PasswordTools()
        self.data = Data()

        self.frame_manager()
        self.primary_window()

    def frame_manager(self):
        self.parent_frame = tk.Frame(self.parent)
        self.parent_frame.pack()
        self.frame1 = tk.Frame(self.parent_frame)
        self.frame1.pack(side="top")
        self.frame0 = tk.Frame(self.parent_frame)
        self.frame0.pack(side="top")
        self.frame2 = tk.Frame(self.parent_frame)
        self.frame2.pack(side="top")
        self.frame3 = tk.Frame(self.parent_frame)
        self.frame3.pack(side="top")
        self.frame4 = tk.Frame(self.parent_frame)
        self.frame4.pack(side="top")
        self.frame5 = tk.Frame(self.parent_frame)
        self.frame5.pack(side="top")
        self.frame6 = tk.Frame(self.parent_frame)
        self.frame6.pack(side="top")

    def primary_window(self):
        self.canvas = Canvas(self.frame0, width=200, height=200, highlightthickness=0)
        self.picture_png = PhotoImage(file="logo.png")
        self.canvas.create_image(100, 100, image=self.picture_png)
        self.canvas.pack(side="left")

        self.label_website = Label(self.frame2, text="Website/URL: ", width=20)
        self.label_website.config(padx=0, pady=3)
        self.label_website.pack(side="left")

        self.entry_website = tk.Entry(self.frame2, width=52, highlightthickness=0)
        self.entry_website.pack(side="left")
        self.entry_website.focus()

        self.label_user = Label(self.frame3, text="Email/Username: ", width=20)
        self.label_user.config(padx=0, pady=3)
        self.label_user.pack(side="left")

        self.entry_user = tk.Entry(self.frame3, width=52)
        self.entry_user.pack(side="left")
        self.entry_user.insert(END, string="fromm_daniel@yahoo.de")

        self.label_pw = Label(self.frame4, text="Password: ", width=20)
        self.label_pw.config(padx=0, pady=3)
        self.label_pw.pack(side="left")

        self.entry_pw = Entry(self.frame4, width=52)
        self.entry_pw.pack(side="left")

        self.label_secure = Label(self.frame5, text="Password\nsecure?")
        self.label_secure.pack(side="left")

        self.canvas_oval = Canvas(self.frame5, width=20, height=20, highlightthickness=0)
        self.canvas_oval.create_oval(1, 1, 19, 19, outline="black", fill="grey")
        self.canvas_oval.pack(side="left")
        self.check_status()

        self.button_copy_website = Button(self.frame2, text="Copy", command=self.copy_pw, width=4)
        self.button_copy_website.pack(side="left")

        self.button_copy_user = Button(self.frame3, text="Copy", command=self.copy_user, width=4)
        self.button_copy_user.pack(side="left")

        self.button_copy_pw = Button(self.frame4, text="Copy", command=self.copy_pw, width=4)
        self.button_copy_pw.pack(side="left")

        self.button_gen_pw = Button(self.frame5, width=44, text="Generate Password", command=self.insert_pw_entry)
        self.button_gen_pw.pack(side="left", fill="x")

        self.label_save_all = Label(self.frame6, text="Save all entries?")
        self.label_save_all.pack(side="left", fill="x")

        self.button_add = Button(self.frame6, width=44, text="Add Entries", command=self.collect_entries)
        self.button_add.pack(side="left", fill='x')

        self.button_load_file = Button(self.frame1, text="Load File", command=self.messagebox_open_json, width=15)
        self.button_load_file.pack(side="left", fill='x')

        self.button_show_item_in_file = Button(self.frame1, text="Show Items in File", command=self.check_open_file, width=15)
        self.button_show_item_in_file.pack(side="left", fill='x')

    def secondary_window(self):
        self.show_window = Tk()
        self.show_window.title("Load Item Data")
        self.show_window.config(padx=50, pady=50, bg=BLACK)

        self.text_website = Text(self.show_window, wrap="word", height=1, width=52)
        self.text_website.pack(side='top', fill='x')

        self.text_user = Text(self.show_window, wrap="word", height=1, width=52)
        self.text_user.pack(side='top', fill='x')

        self.text_pw = Text(self.show_window, wrap="word", height=1, width=52)
        self.text_pw.pack(side='top', fill='x')

        self.combobox = ttk.Combobox(self.show_window, width=48, values=self.data.website_option)
        self.combobox.pack(side='top', fill='y')
        self.combobox.bind("<<ComboboxSelected>>", self.on_combobox_select)

        self.label_load_filedata = tk.Label(self.show_window, text="Load Filedata: ", bg="black", fg="white")
        self.label_load_filedata.pack(side='bottom')

        self.label_text_website = Label(self.show_window, text="Website/URL: ", bg=BLACK, fg=WHITE)
        self.label_text_website.pack(side='left')

        self.label_text_user = Label(self.show_window, text="Email/Username: ", bg=BLACK, fg=WHITE)
        self.label_text_user.pack(side='left')

        self.label_text_pw = Label(self.show_window, text="Password: ", bg=BLACK, fg=WHITE)
        self.label_text_pw.pack(side='left')

        self.data_load_copy_user = Button(self.show_window, text="Copy", command=self.copy_text_user, bg=BLACK, fg=WHITE, width=4)
        self.data_load_copy_user.pack(side='left')

        self.data_load_copy_pw = Button(self.show_window, text="Copy", command=self.copy_text_pw, bg=BLACK, fg=WHITE, width=4)
        self.data_load_copy_pw.pack(side='left')

        self.data_load_copy_pw = Button(self.show_window, text="Copy", command=self.copy_text_website, bg=BLACK, fg=WHITE, width=4)
        self.data_load_copy_pw.pack(side='left')

        self.data_load_delete_item = Button(self.show_window, text="Delete Item", command=self.delete_data, bg=BLACK, fg=WHITE, width=4)
        self.data_load_delete_item.pack(side='left')

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
                    self.insert_text()

    def check_open_file(self):
        if len(self.data.json_data_path) == 0:
            self.data.open_json_file()
        self.secondary_window()

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

    def copy_text_website(self):
        pyperclip.copy(self.text_website.get("1.0", "end-1c"))

    def copy_text_user(self):
        pyperclip.copy(self.text_user.get("1.0", "end-1c"))

    def copy_text_pw(self):
        pyperclip.copy(self.text_pw.get("1.0", "end-1c"))

    def delete_data(self):
        self.data.delete_item(self.selected_item)

    def insert_text(self):
        self.text_website.configure(state="normal")
        self.text_user.configure(state="normal")
        self.text_pw.configure(state="normal")

        if len(self.text_website.get("1.0", "end-1c")) > 0:
            self.text_website.delete("1.0", END)
            self.text_user.delete("1.0", END)
            self.text_pw.delete("1.0", END)

        self.text_website.insert(END, self.website_show)
        self.text_user.insert(END, self.user_show)
        self.text_pw.insert(END, self.encrypted_pw)

        self.text_website.configure(state="disabled")
        self.text_user.configure(state="disabled")
        self.text_pw.configure(state="disabled")