from tkinter import filedialog, messagebox
import json
import os

class Data:
    def __init__(self):
        self.load_items = []
        self.load_status = False
        self.json_data_path = ""
        self.read_file = []
        self.website_option = []
        self.rdy_to_save = False

    def open_json_file(self):
        file_path = filedialog.askopenfilename(filetypes=[("JSON files", "*.json")])
        if file_path:
            try:
                with open(file_path, "r") as file:
                    self.json_data_path = os.path.abspath(file_path)
                    self.read_file = json.load(file)
                self.load_website_options()
                self.load_status = True
                messagebox.showinfo(title="Success!", message="File loaded successfully.")
            except FileNotFoundError:
                messagebox.showinfo(title="Error!", message="File not found.")
            except json.JSONDecodeError:
                messagebox.showinfo(title="Error!", message="Could not decode JSON.")
            except Exception as e:
                messagebox.showinfo(title="Error!", message=f"An error occurred: {e}")

    def save_data(self, website, user, password, password_encrypt):
        if not all([website, user, password, password_encrypt]):
            messagebox.showerror(title="Error!",
                                 message="The data could not be saved. Please fill out all entries.")
            return
        response = messagebox.askokcancel(title="Are you sure you want to save?",
                                          message=f"These are the details you entered: \n\nWebsite/URL: "
                                                  f"{website} \nEmail/Username: {user} "
                                                  f"\nPassword: {password} \n\nIs it ok to save?")
        if response:
            try:
                json_encrypt_pw = password_encrypt.decode("'utf-8")
                new_entry = {"Website/URL": website, "Email/Username": user, "Password": json_encrypt_pw}
                if not self.json_data_path:
                    self.open_json_file()
                self.read_file.append(new_entry)
                with open(self.json_data_path, "w") as read_data:
                    json.dump(self.read_file, read_data, indent=4, ensure_ascii=False)
                messagebox.showinfo(title="Success!", message="Data saved successfully.")
            except Exception as e:
                messagebox.showinfo(title="Error!", message=f"An error occurred: {e}")

    def load_website_options(self):
        key = "Website/URL"
        for item in self.read_file:
            if key in item:
                self.website_option.append(item[key])