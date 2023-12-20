from tkinter import filedialog
import json
import os


class Data:
    def __init__(self):
        self.file_path = ""
        self.load_items = []
        self.json_data_path = ""
        self.key_path = None
        self.key = None
        self.read_file = []
        self.website_option = []
        self.rdy_to_save = False

    def open_json_file(self):
        self.file_path = filedialog.askopenfilename(filetypes=[("JSON files", "*.json")])
        if self.file_path:
            with open(self.file_path, "r") as file:
                self.json_data_path = os.path.abspath(self.file_path)
                self.read_file = json.load(file)

    def save_data(self, new_item):
        # if not self.json_data_path:
        #     self.open_json_file()
        if new_item is not None:
            self.read_file.append(new_item)
        with open(self.json_data_path, "w") as wright_data:
            json.dump(self.read_file, wright_data, indent=4, ensure_ascii=False)

    def load_website_options(self):
        key = "Website/URL"
        self.website_option = [item[key] for item in self.read_file if key in item]

    def delete_item(self, item_to_delete):
        self.read_file = [item for item in self.read_file if item != item_to_delete]
        self.save_data(None)
        self.read_file = self.read_file
