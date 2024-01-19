from tkinter import messagebox
from ttkbootstrap import *
import data
import pyperclip
import json

THEME = "darkly"


class AppManager:
    def __init__(self, root):
        self.website_cache = ""
        self.user_cache = ""
        self.pw_cache = ""
        self.key_path_cache = ""
        self.pw_options_list = [1, 1, 1, 1]

        self.int_number = 8
        self.var_capital = IntVar(value=1)
        self.var_lowercase = IntVar(value=1)
        self.var_numbers = IntVar(value=1)
        self.var_special = IntVar(value=1)
        self.entry_pw_var = StringVar()
        self.password_length_scale_var = tk.DoubleVar()
        self.tools = data.PasswordTools()
        self.data = data.Data()
        self.selected_item = None
        self.main_window = root
        self.main_window.title("NightWardenKey")
        self.main_window.geometry("1600x770")
        self.main_window.minsize(1600, 770)

        self.menubar_main(self.main_window)
        self.app_window_frames(self.main_window)
        self.error_screen_frame(self.error_screen)
        self.sidebar_menu(self.sidebar)
        self.welcome_screen(self.welcome)
        self.apply_theme()

    def app_window_frames(self, frame):
        self.sidebar = ttk.Frame(frame, width=200, height=770, borderwidth=0, relief=GROOVE)
        self.welcome = ttk.Frame(frame, width=1400, height=700, borderwidth=0, relief=GROOVE)
        self.key_loading = ttk.Frame(frame, width=1400, height=700, borderwidth=0, relief=GROOVE)
        self.password_manager = ttk.Frame(frame, width=1400, height=700, borderwidth=0, relief=GROOVE)
        self.password_generator = ttk.Frame(frame, width=1400, height=700, borderwidth=0, relief=GROOVE)
        self.error_screen = ttk.Frame(frame, width=1400, height=33, borderwidth=0, relief=GROOVE)

    def sidebar_menu(self, frame):
        self.sidebar.pack(side="left", fill="y")
        self.welcome_screen_button = ttk.Button(frame, text="Welcome", command=lambda: self.welcome_screen(
            self.welcome), width=30)
        self.welcome_screen_button.pack(side="top")
        self.key_loading_screen_button = ttk.Button(frame, text="Key Manager", command=lambda: self.key_loading_screen(
            self.key_loading), width=30)
        self.key_loading_screen_button.pack(side="top")

    def welcome_screen(self, frame):
        self.key_loading.pack_forget()
        self.password_manager.pack_forget()
        self.password_generator.pack_forget()
        self.welcome.pack(side="top", fill="both", expand=True)

        self.canvas = Canvas(frame, width=331, height=304, highlightthickness=0)
        self.picture_png = PhotoImage(file="logo.png")
        self.canvas.create_image(156, 150, image=self.picture_png)
        self.canvas.place(relx=0.38, rely=0.35)

        self.label_welcome = ttk.Label(frame, text="Welcome to NightWardenKey", font=("Arial", 30))
        self.label_welcome.place(relx=0.29, rely=0.25)

    def key_loading_screen(self, frame):
        self.welcome.pack_forget()
        self.password_manager.pack_forget()
        self.password_generator.pack_forget()
        self.key_loading.pack(side="top", fill="both", expand=True)

        self.label_title = ttk.Label(frame, text="Key Manager")
        self.label_title.place(relx=0.27, rely=0.05, relwidth=0.5, relheight=0.1, anchor="center")
        self.label_title["style"] = "label_title.TLabel"

        self.label_info = ttk.Label(frame, text="This is where you create or load your key to decrypt your saved\n"
                                                "passwords. IMPORTANT: Do not lose the key file, otherwise you will\n"
                                                "no longer be able to access your passwords.")
        self.label_info.place(relx=0.47, rely=0.15, relwidth=0.5, anchor="center")

        self.label_no_key = ttk.Label(frame, text="No Keyfile: ")
        self.label_no_key.place(relx=0.47, rely=0.3, relwidth=0.5, relheight=0.1, anchor="center")

        self.label_load_key = ttk.Label(frame, text="Load Keyfile: ")
        self.label_load_key.place(relx=0.47, rely=0.4, relwidth=0.5, relheight=0.1, anchor="center")

        self.label_filepath = ttk.Label(frame, text="Filepath: ")
        self.label_filepath.place(relx=0.47, rely=0.5, relwidth=0.5, relheight=0.1, anchor="center")

        self.create_button = ttk.Button(frame, text="Create Keyfile", command=self.button_pushed_create_key_file,
                                        width=40)
        self.create_button.place(relx=0.52, rely=0.3, anchor="center")

        self.load_button = ttk.Button(frame, text="Load", command=self.button_pushed_load_key, width=40)
        self.load_button.place(relx=0.52, rely=0.4, anchor="center")

        self.pathfile_entry = ttk.Entry(frame, width=74)
        self.pathfile_entry.place(relx=0.52, rely=0.5, anchor="center")
        self.pathfile_entry.insert(END, string=self.key_path_cache)

        self.pathfile_copy_button = ttk.Button(frame, text="Copy", command=lambda: pyperclip.copy(self.pathfile_entry.
                                                                                                  get()), width=7)
        self.pathfile_copy_button.place(relx=0.755, rely=0.5, anchor="center")

    def password_manager_screen(self, frame):
        self.welcome.pack_forget()
        self.key_loading.pack_forget()
        self.password_generator.pack_forget()
        self.password_manager.pack(side="top", fill="both", expand=True)

        self.label_title = ttk.Label(frame, text="Password Manager")
        self.label_title.place(relx=0.27, rely=0.05, relwidth=0.5, relheight=0.1, anchor="center")
        self.label_title["style"] = "label_title.TLabel"

        self.label_info = ttk.Label(frame, text="Here you can save your new passwords and load existing ones.")
        self.label_info.place(relx=0.47, rely=0.15, relwidth=0.5, anchor="center")

        self.label_load_item = ttk.Label(frame, text="Saved Passwords: ")
        self.label_load_item.place(relx=0.47, rely=0.3, relwidth=0.5, relheight=0.1, anchor="center")

        self.combobox = ttk.Combobox(frame, width=56, postcommand=self.combobox_load_options)
        self.combobox.place(relx=0.52, rely=0.3, anchor="center")
        self.combobox.bind("<<ComboboxSelected>>", self.on_combobox_select)

        self.label_website = ttk.Label(frame, text="Website/URL: ", width=18)
        self.label_website.place(relx=0.47, rely=0.4, relwidth=0.5, relheight=0.1, anchor="center")

        self.entry_website = ttk.Entry(frame, width=58)
        self.entry_website.place(relx=0.52, rely=0.4, anchor="center")
        self.entry_website.insert(END, string=self.website_cache)

        self.label_user = ttk.Label(frame, text="Login: ", width=18)
        self.label_user.place(relx=0.47, rely=0.5, relwidth=0.5, relheight=0.1, anchor="center")

        self.entry_user = ttk.Entry(frame, width=58)
        self.entry_user.place(relx=0.52, rely=0.5, anchor="center")
        self.entry_user.insert(END, string=self.user_cache)

        self.label_pw = ttk.Label(frame, text="Password: ", width=18)
        self.label_pw.place(relx=0.47, rely=0.6, relwidth=0.5, relheight=0.1, anchor="center")

        self.entry_pw = ttk.Entry(frame, width=58, textvariable=self.entry_pw_var)
        self.entry_pw.place(relx=0.52, rely=0.6, anchor="center")
        self.entry_pw.delete(0, END)
        self.entry_pw.insert(END, string=self.pw_cache)
        self.entry_pw_var.trace_add("write", self.check_security_status)

        self.label_secure = ttk.Label(frame, text="Password secure? ", width=18)
        self.label_secure.place(relx=0.47, rely=0.7, relwidth=0.5, relheight=0.1, anchor="center")

        self.label_security_step = ttk.Label(frame)
        self.label_security_step.place(relx=0.65, rely=0.7, relwidth=0.5, relheight=0.1, anchor="center")

        self.button_load_file = ttk.Button(frame, text="Load File", command=self.button_pushed_load_file, width=10)
        self.button_load_file.place(relx=0.735, rely=0.3, anchor="center")

        self.button_copy_website = ttk.Button(frame, text="Copy", command=lambda: pyperclip.copy(self.entry_website.
                                                                                                 get()), width=10)
        self.button_copy_website.place(relx=0.735, rely=0.4, anchor="center")

        self.button_copy_user = ttk.Button(frame, text="Copy", command=lambda: pyperclip.copy(self.entry_user.get()),
                                           width=10)
        self.button_copy_user.place(relx=0.735, rely=0.5, anchor="center")

        self.button_copy_pw = ttk.Button(frame, text="Copy", command=lambda: pyperclip.copy(self.entry_pw.get()),
                                         width=10)
        self.button_copy_pw.place(relx=0.735, rely=0.6, anchor="center")

        self.button_add = ttk.Button(frame, text="Save Password", command=lambda: self.button_pushed_save_data(
        self.entry_website.get(), self.entry_user.get(), self.entry_pw.get()), width=30)
        self.button_add.place(relx=0.52, rely=0.8, anchor="center")

        self.check_pw_cache()

    def password_generator_screen(self, frame):
        self.welcome.pack_forget()
        self.key_loading.pack_forget()
        self.password_manager.pack_forget()
        self.password_generator.pack(side="top", fill="both", expand=True)

        self.label_title = ttk.Label(frame, text="Key Generator")
        self.label_title.place(relx=0.27, rely=0.05, relwidth=0.5, relheight=0.1, anchor="center")
        self.label_title["style"] = "label_title.TLabel"

        self.label_info = ttk.Label(frame, text="You can create your new password here. Once you have created your \n"
                                                "new password, it is automatically sent to the password manager.")
        self.label_info.place(relx=0.47, rely=0.15, relwidth=0.5, anchor="center")

        self.label_pw = ttk.Label(frame, text="New Password: ", width=18)
        self.label_pw.place(relx=0.48, rely=0.3, relwidth=0.5, relheight=0.1, anchor="center")

        self.entry_generate_pw = ttk.Entry(frame, width=58)
        self.entry_generate_pw.place(relx=0.52, rely=0.3, anchor="center")
        self.entry_generate_pw.insert(END, string=self.pw_cache)

        self.check_pw_options_capital = ttk.Checkbutton(frame, command=self.show_selected_checkmark_capital,
                                                        variable=self.var_capital)
        self.check_pw_options_capital.place(relx=0.34, rely=0.4, anchor="center")

        self.check_pw_options_lowercase = ttk.Checkbutton(frame, command=self.show_selected_checkmark_lowercase,
                                                          variable=self.var_lowercase)
        self.check_pw_options_lowercase.place(relx=0.52, rely=0.4, anchor="center")

        self.check_pw_options_numbers = ttk.Checkbutton(frame, command=self.show_selected_checkmark_numbers,
                                                        variable=self.var_numbers)
        self.check_pw_options_numbers.place(relx=0.34, rely=0.5, anchor="center")

        self.check_pw_options_special = ttk.Checkbutton(frame, command=self.show_selected_checkmark_special,
                                                        variable=self.var_special)
        self.check_pw_options_special.place(relx=0.52, rely=0.5, anchor="center")

        self.label_capital = ttk.Label(frame, text="Capital letter", width=15)
        self.label_capital.place(relx=0.44, rely=0.4, anchor="center")

        self.label_lower_case = ttk.Label(frame, text="Lower case letter", width=18)
        self.label_lower_case.place(relx=0.62, rely=0.4, anchor="center")

        self.label_numbers = ttk.Label(frame, text="Numbers", width=15)
        self.label_numbers.place(relx=0.44, rely=0.5, anchor="center")

        self.label_special = ttk.Label(frame, text="Special characters", width=18)
        self.label_special.place(relx=0.62, rely=0.5, anchor="center")

        self.password_length_slider = ttk.Scale(frame, variable=self.password_length_scale_var, from_=8, to=40, command=self.on_scale_change)
        self.password_length_slider.place(relx=0.5, rely=0.6, relwidth=0.3, anchor="center")

        self.label_password_length = ttk.Label(frame, text="Password length: ", width=18)
        self.label_password_length.place(relx=0.5, rely=0.64, anchor="center")

        self.label_password_length_screen = ttk.Label(frame, text="8", width=18)
        self.label_password_length_screen.place(relx=0.63, rely=0.64, anchor="center")

        self.button_gen_pw = ttk.Button(frame, width=30, text="Generate Password", command=self.
                                        insert_generated_password_entry_pw)
        self.button_gen_pw.place(relx=0.5, rely=0.75, anchor="center")

    def error_screen_frame(self, frame):
        self.error_screen.pack(side="bottom", fill="y")
        self.label_show_error = ttk.Label(frame, width=100)
        self.label_show_error.place(relx=0.21)

    def menubar_main(self, root):
        self.data_menu = Menu(root)

        self.menu = Menu(self.data_menu, tearoff=0)
        self.menu.add_command(label="Load File", command=self.button_pushed_load_file)
        self.menu.add_command(label="Exit", command=self.exit_program)
        self.data_menu.add_cascade(label="File", menu=self.menu)

        self.item = Menu(self.data_menu, tearoff=0)
        self.item.add_command(label="Clean Fields", command=self.clear_all_entries)
        self.item.add_command(label="Delete Password", command=self.delete_data_from_file)
        self.data_menu.add_cascade(label="Data", menu=self.item)
        self.main_window.config(menu=self.data_menu)

    # Main Screen Functions

    def apply_theme(self):
        try:
            styles = Style()
            styles.theme_use(THEME)
            styles.configure("My.TFrame", bg="grey")
            styles.configure("label_title.TLabel", font=('Arial', 30))
            styles.configure("TButton", font=('Arial', 15))
            styles.configure("TLabel", font=('Arial', 15))
            styles.configure("TEntry", font=('Arial', 15), padding=[9])
            styles.configure("TCombobox", font=('Arial', 15), padding=[9])
        except Exception as error:
            messagebox.showinfo(title="Error!", message=f"An error occurred: {error}")

    def check_security_status(self, password, *args):
        try:
            password = self.entry_pw.get()
        except:
            pass
        self.security_light_update(self.tools.password_check(password))
        self.label_show_error.config(text="")

    def exit_program(self):
        response = messagebox.askokcancel(title="Quit program? ", message=f"All unsaved Data are lost.")
        if response:
            exit()
        else:
            return None

    # Sidebar Menu Functions

    def sidebar_show_buttons(self):
        if len(self.data.key_path) > 0:
            if not hasattr(self, 'password_manager_screen_button') or not isinstance(self.
                                                                                     password_manager_screen_button,
                                                                                     ttk.Button):
                self.password_manager_screen_button = ttk.Button(self.sidebar, text="Password Manager",
                                                                 command=lambda: self.
                                                                 password_manager_screen(self.password_manager),
                                                                 width=30)
                self.password_manager_screen_button.pack(side="top")
                self.password_generator_screen_button = ttk.Button(self.sidebar, text="Password Generator",
                                                                   command=lambda: self.password_generator_screen(
                                                                       self.password_generator), width=30)
                self.password_generator_screen_button.pack(side="top")

    # Key Manager Loading Screen Functions

    def button_pushed_load_key(self):
        # try:
            key_value = self.data.load_key_file()
            status = self.tools.insert_security_key(key_value)
            self.pathfile_entry.insert(END, string=self.data.key_path)
            self.key_path_cache = self.pathfile_entry.get()
            self.sidebar_show_buttons()
            if status:
                return True
        # except PermissionError:
        #     error = "Error! Please check if you have the rights for the file."
        #     self.show_error_area(error)
        # except ValueError:
        #     error = "Error! Key could not be loaded or is invalid. Please load the right the Keyfile."
        #     self.show_error_area(error)

    def button_pushed_create_key_file(self):
        # try:
            create_key = self.tools.generate_security_key()
            self.data.create_key_file(create_key)
            status = self.tools.insert_security_key(create_key)
            self.pathfile_entry.insert(END, string=self.data.key_path)
            self.key_path_cache = self.pathfile_entry.get()
            self.sidebar_show_buttons()
            if status:
                return True
        # except Exception:
        #     error = "Error! An error has occurred. Please try again to create a file."
        #     self.show_error_area(error)

    # Password Manager Screen Functions

    def button_pushed_load_file(self):
        try:
            self.data.open_json_file()
        except json.JSONDecodeError:
            error = "Error! Could not decode JSON. File is invalid or compromised."
            self.show_error_area_label(error)
        except Exception:
            error = "Error! Data could not be loaded."
            self.show_error_area_label(error)

    def check_pw_cache(self):
        if len(self.pw_cache) > 0:
            self.check_security_status(self.pw_cache)

    def check_entry_focus(self):
        entry_filed_focus = self.password_manager.focus_get()
        if entry_filed_focus != self.entry_website:
            self.website_cache = self.entry_website.get()
            self.user_cache = self.entry_user.get()
            self.pw_cache = self.entry_pw.get()

    def save_entry_cache(self):
        if self.password_manager.winfo_exists():
            self.website_cache = self.entry_website.get()
            self.user_cache = self.entry_user.get()
            self.pw_cache = self.entry_pw.get()

    def no_file_found(self):
        # try:
            file_not_found = messagebox.askokcancel(title="No file found!", message="Do you want to create a file "
                                                                                    "press Ok or load a file "
                                                                                    "press Cancel")
            if file_not_found:
                self.data.create_file()
            else:
                self.button_pushed_load_file()
        # except Exception:
        #     error = "Error! An error has occurred. Please try again."
        #     self.show_error_area(error)


    def combobox_load_options(self):
        try:
            websites = self.data.load_website_options()
            self.combobox["values"] = websites
        except Exception:
            error = "Error! An error has occurred. Loaded file is corrupt."
            self.show_error_area_label(error)

    def button_pushed_save_data(self, website, user, password):
        # try:
            user_encrypt = self.tools.encrypt_data(user)
            password_encrypt = self.tools.encrypt_data(password)
            if not all([website, user, password, password]):
                error = f"Error! The data could not be saved. Please fill out all entries."
                return self.show_error_area_label(error)
            if self.data.json_data_path is False:
                self.no_file_found()
            self.data.save_new_data(website, user_encrypt, password_encrypt)
            save_success = f"Success! Website/URL: {website}, Login: {user}, Password: {password}, saved successfully."
            self.clear_all_entries()
            return self.show_error_area_label(save_success)
        # # except PermissionError:
        # #     error = "Error! Please check if you have the rights for the file."
        # #     self.show_error_area(error)
        # except ValueError:
        #     error = "Error! Key could not be loaded or is invalid. Please load the right the Keyfile."
        #     self.show_error_area(error)
        # except Exception as error:
        #     error = "Error! Data could not be saved. Please check your entries."
        #     self.show_error_area(error)

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
                        encrypted_user = self.tools.decrypt_data(user_show)
                        encrypted_pw = self.tools.decrypt_data(pw_show)
                        self.insert_text_to_entries(website_show, encrypted_user, encrypted_pw)
        except Exception:
            error = "Error! Stored password cannot be loaded with your key or is corrupt."
            self.show_error_area_label(error)

    def insert_text_to_entries(self, website, decrypted_user, decrypted_password):
        if len(self.entry_website.get()) or len(self.entry_user.get()) or len(self.entry_user.get()) != 0:
            self.clear_all_entries()
        self.entry_website.delete(0, END)
        self.entry_user.delete(0, END)
        self.entry_pw.delete(0, END)
        self.entry_website.insert(END, string=website)
        self.entry_user.insert(END, string=decrypted_user)
        self.entry_pw.insert(END, string=decrypted_password)
        self.show_selected_checkmark_capital()

    def security_light_update(self, light_status):
        if light_status in ("strong", "medium", "weak"):
            self.label_security_step.config(text=light_status)

    # Password Generator Screen Functions

    def on_scale_change(self, value):
        self.int_number = 0
        self.int_number = int(float(value))
        self.label_password_length_screen.config(text=f"{self.int_number}")
        return self.int_number

    def show_selected_checkmark_capital(self):
        selection = self.var_capital.get()
        self.pw_options_list[0] = selection

    def show_selected_checkmark_lowercase(self):
        selection = self.var_lowercase.get()
        self.pw_options_list[1] = selection

    def show_selected_checkmark_numbers(self):
        selection = self.var_numbers.get()
        self.pw_options_list[2] = selection

    def show_selected_checkmark_special(self):
        selection = self.var_special.get()
        self.pw_options_list[3] = selection

    def insert_generated_password_entry_pw(self):
        self.entry_generate_pw.delete(0, END)
        self.pw_length = self.on_scale_change(self.int_number)
        pw_options = self.pw_options_list
        self.pw_cache = self.tools.generate_password(self.pw_length, pw_options)
        if len(self.pw_cache) != 0:
            self.entry_generate_pw.insert(tk.END, self.pw_cache)

    # Error Screen Functions

    def show_error_area_label(self, error):
        self.label_show_error.config(text=f"{error}")

    def delete_error_label_after_time(self):
        self.label_show_error.config(text="")

    # Menubar

    def delete_data_from_file(self):
        check_delete_error = None
        try:
            if self.selected_item is None:
                error = "Error! No password available to delete."
                self.show_error_area_label(error)
                check_delete_error = True
            self.data.delete_item(self.selected_item)
            self.data.save_new_data()
            self.clear_all_entries()
        except Exception as error:
            if check_delete_error is not True:
                error = f"Error! Password cannot be deleted. {error}."
                self.show_error_area_label(error)

    def clear_all_entries(self):
        self.entry_website.delete(0, END)
        self.entry_user.delete(0, END)
        self.entry_pw.delete(0, END)
        self.website_cache = ""
        self.user_cache = ""
        self.pw_cache = ""
