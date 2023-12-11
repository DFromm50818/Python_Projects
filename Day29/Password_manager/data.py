from tkinter import filedialog
from tkinter import messagebox
import json


class Data:
    def __init__(self):
        self.load_status = False
        self.json_data_path = ""
        self.read_file = []
        self.website_option = []
        self.rdy_to_save = False

    def open_json_file(self):
        self.json_data_path = filedialog.askopenfilename(filetypes=[("JSON files", "*.json")])
        try:
            with open(self.json_data_path, "r") as file:
                self.read_file = json.load(file)
            self.load_data_options()
            self.load_status = True
            if len(self.json_data_path) == 0:
                messagebox.showinfo(title="Error!", message="Could not be read.")
        except:
            return None

    def save_data(self, website, user, password):
        password = f"{password}"
        try:
            new_entry = {"Website": website, "Email/Username": user, "Password": password}
            if len(self.json_data_path) == 0:
                self.open_json_file()
            self.read_file.append(new_entry)
            with open(self.json_data_path, "w") as read_data:
                json.dump(self.read_file, read_data, indent=4, ensure_ascii=False)
                messagebox.showinfo(title="Save data", message="Data save success")
        except:
            messagebox.showinfo(title="Error!", message="JSON Data not loaded.")

    def load_data_options(self):
        key = "Website"
        for item in self.read_file:
            if key in item:
                self.website_option.append(item[key])

