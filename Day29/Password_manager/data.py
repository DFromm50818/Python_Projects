import base64
from tkinter import filedialog
import json
import os
# from cryptography.fernet import Fernet

class Data:
    def __init__(self):
        self.load_items = []
        self.json_data_path = ""
        self.key_path = None
        self.key = None
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

    # def open_file_key(self):
    #     self.key_path = filedialog.askopenfilename(filetypes=[("BIN files", "*.bin")])
    #     if self.key_path:
    #         with open(self.key_path, "r") as file:
    #             passkey = os.path.abspath(self.key_path)
    #             byte_format_password = passkey.encode('utf-8')
    #         # if len(byte_format_password) == 32:
    #             print(byte_format_password)
    #             return byte_format_password
    #         # else:
    #         #     raise ValueError("Ungültiger Schlüssel")
    #
    # def save_key(self, key_encrypt):
    #     if key_encrypt is not None:
    #         encrypt_key = key_encrypt.decode('utf-8')
    #         with open(self.key_path, "w") as file:
    #             file.write(encrypt_key)

    # def save_key_to_file(self, file_path, key):
    #     if key:
    #         with open(file_path, 'wb') as file:
    #             file.write(key)
    #         print("Key has been saved successfully.")
    #     else:
    #         print("No key to save.")
    #
    # def load_key_from_file(self):
    #     try:
    #         self.key_path = filedialog.askopenfilename(filetypes=[("BIN files", "*.bin")])
    #         with open(self.key_path, 'rb') as file:
    #             self.key = file.read()
    #             if len(self.key) == 32 and base64.urlsafe_b64encode(self.key) == self.key:
    #                 print("Key has been loaded successfully.")
    #                 self.cipher_suite = Fernet(self.key)
    #                 return self.key
    #             else:
    #                 print("Loaded key is not in the correct format.")
    #     except FileNotFoundError:
    #         print("File not found.")
    #     except Exception as error:
    #         print(f"An error occurred while loading the key: {error}")

# # Beispiel der Verwendung
#
# key_manager.generate_key()
#
# # Speichern des Schlüssels
# key_manager.save_key_to_file("my_key.bin")
#
# # Laden des Schlüssels
# key_manager.load_key_from_file("my_key.bin")