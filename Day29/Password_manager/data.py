from tkinter import filedialog, messagebox
import json
import os

class Data:
    def __init__(self):
        self.load_items = []
        self.json_data_path = None
        self.key_path = None
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

    def open_file_key(self):
        self.key_path = filedialog.askopenfilename(filetypes=[("BIN files", "*.bin")])
        if self.key_path:
            with open(self.key_path, "r") as file:
                passkey = os.path.abspath(self.key_path)
            if len(passkey) == 32:
                print(passkey)
                return passkey
            else:
                raise ValueError("Ungültiger Schlüssel")

    def save_key(self, key_encrypt):
        # json_encrypt_key = key_encrypt.decode('utf-8')
        with open(self.key_path, "wb") as file:
            file.write(key_encrypt)

