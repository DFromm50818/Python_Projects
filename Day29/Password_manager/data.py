from tkinter import filedialog, messagebox
import json
import os

class Data:
    def __init__(self):
        self.load_items = []

        self.json_data_path = ""
        self.read_file = []
        self.website_option = []
        self.rdy_to_save = False

    def open_json_file(self):
        file_path = filedialog.askopenfilename(filetypes=[("JSON files", "*.json")])
        if file_path:
            with open(file_path, "r") as file:
                self.json_data_path = os.path.abspath(file_path)
                self.read_file = json.load(file)
            self.load_website_options()
            if self.read_file:
                

            # try:
            #     messagebox.showinfo(title="Success!", message="File loaded successfully.")
            # except FileNotFoundError:
            #     messagebox.showinfo(title="Error!", message="File not found.")
            # except json.JSONDecodeError:
            #     messagebox.showinfo(title="Error!", message="Could not decode JSON.")
            # except Exception as e:
            #     messagebox.showinfo(title="Error!", message=f"An error occurred: {e}")

    def save_data(self, new_item, file):
        if not self.json_data_path:
            self.open_json_file()
        if new_item is not None:
            self.read_file.append(new_item)
        with open(self.json_data_path, "w") as read_data:
            json.dump(file, read_data, indent=4, ensure_ascii=False)

    def load_website_options(self):
        key = "Website/URL"
        self.website_option = [item[key] for item in self.read_file if key in item]

    def delete_item(self, item_to_delete):
        self.read_file = [item for item in self.read_file if item != item_to_delete]
        self.save_data(None, self.read_file)