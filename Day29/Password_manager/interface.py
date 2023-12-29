from tkinter import messagebox
from ttkbootstrap import *
from tools import PasswordTools
from data import Data
import pyperclip
import json

THEME = "darkly"


class AppManager:
    def __init__(self, root):
        self.tools = PasswordTools()
        self.data = Data()
        self.selected_item = None
        self.main_window = root
        self.main_window.title("Password Manager")
        self.main_window.geometry("1800x1000")

        self.menubar_main(self.main_window)

        self.sidebar = ttk.Frame(self.main_window, width=200, height=200, borderwidth=10, relief=GROOVE)
        self.welcome = ttk.Frame(self.main_window, width=200, height=200, borderwidth=10, relief=GROOVE)
        self.key_loading = ttk.Frame(self.main_window, width=200, height=200, borderwidth=10, relief=GROOVE)
        self.password_manager = ttk.Frame(self.main_window, width=200, height=200, borderwidth=10, relief=GROOVE)
        self.password_generator = ttk.Frame(self.main_window, width=200, height=200, borderwidth=10, relief=GROOVE)

        self.welcome_screen_button = ttk.Button(self.sidebar, text="Welcome", command=lambda: self.welcome_screen(self.welcome), width=30)
        self.welcome_screen_button.pack(side="top")
        self.key_loading_screen_button = ttk.Button(self.sidebar, text="Key Manager", command=lambda: self.key_loading_screen(self.key_loading), width=30)
        self.key_loading_screen_button.pack(side="top")

        self.sidebar.pack(side="left", fill="y")
        self.welcome_screen(self.welcome)
        self.apply_theme()

    def welcome_screen(self, frame):
        self.key_loading.pack_forget()
        self.password_manager.pack_forget()
        self.password_generator.pack_forget()
        self.welcome.pack(side="left", fill="both", expand=True)

        self.canvas = Canvas(frame, width=200, height=200, highlightthickness=0)
        self.picture_png = PhotoImage(file="logo.png")
        self.canvas.create_image(100, 100, image=self.picture_png)
        self.canvas.place(relx=0.44, rely=0.4)

        self.label_welcome = ttk.Label(frame, text="Welcome to MyPass", font=("Arial", 30))
        self.label_welcome.place(relx=0.38, rely=0.3)

    def key_loading_screen(self, frame):
        self.welcome.pack_forget()
        self.password_manager.pack_forget()
        self.password_generator.pack_forget()
        self.key_loading.pack(side="left", fill="both", expand=True)

        self.label_title = ttk.Label(frame, text="Key Manager")
        self.label_title.place(relx=0.27, rely=0.05, relwidth=0.5, relheight=0.1, anchor="center")
        self.label_title["style"] = "label_title.TLabel"

        self.label_info = ttk.Label(frame, text="This is where you create or load your key to decrypt your saved "
                                                 "passwords.\nImportant: Do not lose the key file, otherwise you will "
                                                 "no longer be able to access your passwords.")
        self.label_info.place(relx=0.5, rely=0.2, relwidth=0.5, relheight=0.1, anchor="center")

        self.label_no_key = ttk.Label(frame, text="No Keyfile: ")
        self.label_no_key.place(relx=0.5, rely=0.3, relwidth=0.5, relheight=0.1, anchor="center")

        self.label_load_key = ttk.Label(frame, text="Load Keyfile: ")
        self.label_load_key.place(relx=0.5, rely=0.4, relwidth=0.5, relheight=0.1, anchor="center")

        self.label_filepath = ttk.Label(frame, text="Filepath: ")
        self.label_filepath.place(relx=0.5, rely=0.5, relwidth=0.5, relheight=0.1, anchor="center")

        self.create_button = ttk.Button(frame, text="Create Keyfile", command=self.button_pushed_create_key_file, width=40)
        self.create_button.place(relx=0.52, rely=0.3, anchor="center")

        self.load_button = ttk.Button(frame, text="Load", command=self.button_pushed_load_key, width=40)
        self.load_button.place(relx=0.52, rely=0.4, anchor="center")

        self.pathfile_entry = ttk.Entry(frame, width=75)
        self.pathfile_entry.place(relx=0.52, rely=0.5, anchor="center")

    def password_manager_screen(self, frame):
        self.welcome.pack_forget()
        self.key_loading.pack_forget()
        self.password_generator.pack_forget()
        self.password_manager.pack(side="left", fill="both", expand=True)

        self.label_title = ttk.Label(frame, text="Password Manager")
        self.label_title.place(relx=0.27, rely=0.05, relwidth=0.5, relheight=0.1, anchor="center")
        self.label_title["style"] = "label_title.TLabel"

        self.label_website = ttk.Label(frame, text="Website/URL: ", width=18)
        self.label_website.grid(row=2, column=2, sticky="e")

        self.entry_website = ttk.Entry(frame, width=58)
        self.entry_website.grid(row=2, column=3, columnspan=2, sticky="w")
        self.entry_website.focus()

        self.label_user = ttk.Label(frame, text="Login: ", width=18)
        self.label_user.grid(row=3, column=2, sticky="e")

        self.entry_user = ttk.Entry(frame, width=58)
        self.entry_user.grid(row=3, column=3, columnspan=2, sticky="w")

        self.label_pw = ttk.Label(frame, text="Password: ", width=18)
        self.label_pw.grid(row=4, column=2, sticky="e")

        self.entry_pw = ttk.Entry(frame, width=58)
        self.entry_pw.grid(row=4, column=3, columnspan=2, sticky="w")

        self.label_secure = ttk.Label(frame, text="Password secure? ", width=18)
        self.label_secure.grid(row=5, column=2, sticky="e")

        self.button_copy_website = ttk.Button(frame, text="Copy", command=lambda: pyperclip.copy(self.entry_website.get()), width=6)
        self.button_copy_website.grid(row=2, column=5, sticky="w")

        self.button_copy_user = ttk.Button(frame, text="Copy", command=lambda: pyperclip.copy(self.entry_user.get()), width=6)
        self.button_copy_user.grid(row=3, column=5, sticky="w")

        self.button_copy_pw = ttk.Button(frame, text="Copy", command=lambda: pyperclip.copy(self.entry_pw.get()), width=6)
        self.button_copy_pw.grid(row=4, column=5, sticky="w")

        self.button_gen_pw = ttk.Button(frame, width=22, text="Generate Password", command=lambda: self.entry_pw.insert(END, string=self.insert_generated_password_entry_pw()))
        self.button_gen_pw.grid(row=6, column=3, sticky="w")

        self.button_add = ttk.Button(frame, text="Save Password", command=lambda: self.button_pushed_save_data(self.entry_website.get(), self.entry_user.get(), self.entry_pw.get()), width=22)
        self.button_add.grid(row=6, column=4, sticky="w")

        self.combobox = ttk.Combobox(frame, width=55, postcommand=self.combobox_load_options)
        self.combobox.grid(row=1, column=3, columnspan=2, sticky="w")
        self.combobox.bind("<<ComboboxSelected>>", self.on_combobox_select)

        self.label_load_item = ttk.Label(frame, text="Saved Passwords: ", width=18)
        self.label_load_item.grid(row=1, column=2, sticky="e")

        self.label_security_step = ttk.Label(frame)
        self.label_security_step.grid(row=5, column=3, sticky="w")

        self.label_error = ttk.Label(frame, width=120)
        self.label_error.grid(row=7, column=0, columnspan=5)

        self.check_security_status()

    def password_generator_screen(self, frame):
        self.welcome.pack_forget()
        self.key_loading.pack_forget()
        self.password_manager.pack_forget()
        self.password_generator.pack(side="left", fill="both", expand=True)

        self.label_title = ttk.Label(frame, text="Key Generator")
        self.label_title.place(relx=0.27, rely=0.05, relwidth=0.5, relheight=0.1, anchor="center")
        self.label_title["style"] = "label_title.TLabel"

    def menubar_main(self, root):
        self.data_menu = Menu(root)

        self.menu = Menu(self.data_menu, tearoff=0)
        self.menu.add_command(label="Load File", command=self.button_pushed_load_file)
        self.menu.add_command(label="Load Key", command=self.button_pushed_load_key)
        self.menu.add_command(label="Exit", command=self.exit_program)
        self.data_menu.add_cascade(label="File", menu=self.menu)

        self.item = Menu(self.data_menu, tearoff=0)
        self.item.add_command(label="Clean Fields", command=self.clear_all_entries)
        self.item.add_command(label="Delete Password", command=self.delete_data_from_file)
        self.data_menu.add_cascade(label="Data", menu=self.item)

        self.key = Menu(self.data_menu, tearoff=0)
        self.key.add_command(label="Load Keyfile", command=self.button_pushed_load_key)
        self.key.add_command(label="Create Keyfile", command=self.button_pushed_create_key_file)
        self.data_menu.add_cascade(label="Key Management", menu=self.key)
        self.main_window.config(menu=self.data_menu)

    def apply_theme(self):
        try:
            style = Style()
            style.theme_use(THEME)
            frame_style = style.lookup('TFrame', 'background')
            label_style = style.lookup('TLabel', 'background')
            style.configure('label_title.TLabel', font=('Arial', 30))
            style.configure('TButton', font=('Arial', 15))
            style.configure('TLabel', font=('Arial', 15))
            style.configure('TEntry', font=('Arial', 15))
            self.main_window.config(bg=frame_style)
            self.canvas.config(bg=label_style)
        except Exception as error:
            messagebox.showinfo(title="Error!", message=f"An error occurred: {error}")

    def sidebar_show_buttons(self):
        if len(self.data.key_path) > 0:
            if not hasattr(self, 'password_manager_screen_button') or not isinstance(self.password_manager_screen_button, ttk.Button):
                self.password_manager_screen_button = ttk.Button(self.sidebar, text="Password Manager", command=lambda: self.password_manager_screen(self.password_manager), width=30)
                self.password_manager_screen_button.pack(side="top")
                self.password_generator_screen_button = ttk.Button(self.sidebar, text="Password Generator", command=lambda: self.password_generator_screen(self.password_generator), width=30)
                self.password_generator_screen_button.pack(side="top")

    def check_security_status(self):
        try:
            self.main_window.after(500, self.check_security_status)
            self.security_light_update(self.tools.password_check(self.entry_pw.get()))
        except Exception as error:
            messagebox.showinfo(title="Error!", message=f"An error occurred: {error}")

    def no_file_found(self):
        try:
            file_not_found = messagebox.askokcancel(title="No file found!", message="Do you want to create a file "
                                                                                    "press Ok or load a file "
                                                                                    "press Cancel")
            if file_not_found:
                self.data.create_file()
            else:
                self.button_pushed_load_file()
        except Exception as error:
            self.label_error.config(text=f"An error occurred {error}")
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

    def button_pushed_save_data(self, website, user, password):
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

    def button_pushed_load_file(self):
        try:
            self.data.open_json_file()
        except FileNotFoundError:
            messagebox.showinfo(title="Error!", message="File not found.")
        except json.JSONDecodeError:
            messagebox.showinfo(title="Error!", message="Could not decode JSON.")
        except Exception as error:
            messagebox.showinfo(title="Error!", message=f"An error occurred: {error}")

    def on_combobox_select(self, event):
        try:
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
        except Exception as error:
            messagebox.showinfo(title="Error!", message=f"An error occurred: {error}")

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
        try:
            self.entry_pw.delete(0, END)
            pw = self.tools.generate_password()
            if len(pw) != 0:
                return pw
        except Exception as error:
            messagebox.showinfo(title="Error!", message=f"An error occurred: {error}")

    def security_light_update(self, light_status):
        try:
            if light_status in ("strong", "medium", "weak"):
                self.label_security_step.config(text=light_status)
        except Exception as error:
            messagebox.showinfo(title="Error!", message=f"An error occurred: {error}")

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

    def key_handling(self):
        try:
            file_key = messagebox.askokcancel(title="Load file key.", message="Load key or create new key.")
            if file_key:
                self.button_pushed_load_key()
            else:
                self.button_pushed_create_key_file()
        except Exception as error:
            messagebox.showinfo(title="Error!", message=f"An error occurred: {error}")

    def button_pushed_load_key(self):
        try:
            key_value = self.data.load_key_file()
            status = self.tools.insert_security_key(key_value)
            self.pathfile_entry.insert(END, string=self.data.key_path)
            self.sidebar_show_buttons()
            if status:
                return True
        except Exception as error:
            return None
            # messagebox.showinfo(title="Error!", message=f"An error occurred: {error}")

    def button_pushed_create_key_file(self):
        try:
            create_key = self.tools.generate_security_key()
            self.data.create_key_file(create_key)
            status = self.tools.insert_security_key(create_key)
            self.pathfile_entry.insert(END, string=self.data.key_path)
            self.sidebar_show_buttons()
            if status:
                return True
        except Exception as error:
            # return None
            messagebox.showinfo(title="Error!", message=f"An error occurred: {error}")
