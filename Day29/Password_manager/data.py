from tkinter import filedialog
import json
import os


class Data:
    def __init__(self):
        self.file_path = ""
        self.json_data_path = False
        self.key_path = None
        self.read_file = []
        self.website_option = []

    def open_json_file(self):
        self.file_path = filedialog.askopenfilename(filetypes=[("JSON files", "*.json")])
        if self.file_path:
            with open(self.file_path, "r") as file:
                self.json_data_path = os.path.abspath(self.file_path)
                self.read_file = json.load(file)

    def save_new_data(self, website = None, user = None, password_encrypt = None):
        if all((website, user, password_encrypt)):
            new_entry = {"Website/URL": website, "Login": user, "Password": password_encrypt}
            self.read_file.append(new_entry)
        with open(self.json_data_path, "w") as wright_data:
            json.dump(self.read_file, wright_data, indent=4, ensure_ascii=False)

    def load_website_options(self):
        key = "Website/URL"
        self.website_option = [item[key] for item in self.read_file if key in item]
        return self.website_option

    def delete_item(self, item_to_delete):
        self.read_file = [item for item in self.read_file if item != item_to_delete]
        return self.read_file

    def create_file(self):
        filepath = filedialog.asksaveasfilename(defaultextension=".json", filetypes=[("JSON files", "*.json")])
        self.json_data_path = os.path.abspath(filepath)
        with open(self.json_data_path, "w") as new_file:
            pass
        return self.json_data_path

    def check_file_exists(self, filename):
        return os.path.exists(filename)
