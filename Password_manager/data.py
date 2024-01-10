from tkinter import filedialog
import json
import os
from random import choice, shuffle
from cryptography.fernet import Fernet
import string


class Data:
    def __init__(self):
        self.website_option = []
        self.file_path = ""
        self.json_data_path = False
        self.key_path = ""
        self.read_file = []
        self.website_option_encrypted = []

    def open_json_file(self):
        self.file_path = filedialog.askopenfilename(filetypes=[("JSON files", "*.json")])
        if self.file_path:
            with open(self.file_path, "r") as file:
                self.json_data_path = os.path.abspath(self.file_path)
                self.read_file = json.load(file)

    def save_new_data(self, encrypt_website=None, encrypt_user=None, encrypt_password=None):
        if all((encrypt_website, encrypt_user, encrypt_password)):
            new_entry = {"Website/URL": encrypt_website, "Login": encrypt_user, "Password": encrypt_password}
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
        with open(self.json_data_path, "w") as _:
            pass
        return self.json_data_path

    def create_key_file(self, key):
        self.key_path = filedialog.asksaveasfilename(defaultextension=".bin", filetypes=[("BIN files", "*.bin")])
        with open(self.key_path, "wb") as file:
            file.write(key)

    def load_key_file(self):
        self.key_path = filedialog.askopenfilename(filetypes=[("BIN files", "*.bin")])
        if os.path.exists(self.key_path):
            with open(self.key_path, 'rb') as file:
                encrypted_key = file.read()
            return encrypted_key


class PasswordTools:
    def __init__(self):
        self.light = "weak"
        self.cipher_suite = None

    def password_check(self, password):
        digits = "".join(filter(str.isdigit, password))
        letter_lower = "".join(filter(str.islower, password))
        letter_upper = "".join(filter(str.isupper, password))
        symbols = "".join(filter(lambda x: not x.isalnum(), password))
        conditions = [
            len(digits) >= 3 and len(symbols) >= 3 and len(letter_upper) >= 4 and len(letter_lower) >= 4,
            len(digits) >= 2 and len(symbols) >= 2 and len(letter_upper) >= 3 and len(letter_lower) >= 3
        ]
        self.light = "strong" if any(conditions) else "medium" if password else "weak"
        return self.light

    def generate_password(self, length, options):
        character_options = 0
        uppercase = None
        lowercase = None
        number = None
        special = None
        for num in options:
            character_options += num
        remaining_length = length % character_options
        letter_list = [uppercase, lowercase, number, special]
        letter_list[0] = int(float(length / character_options)) * options[0]
        letter_list[1] = int(float(length / character_options)) * options[1]
        letter_list[2] = int(float(length / character_options)) * options[2]
        letter_list[3] = int(float(length / character_options)) * options[3]
        options_index = next(index for index, value in enumerate(letter_list) if value > 0)
        letter_list[options_index] += remaining_length
        pw_categories = [
            (string.ascii_uppercase, letter_list[0]),
            (string.ascii_lowercase, letter_list[1]),
            (string.digits, letter_list[2]),
            (string.punctuation, letter_list[3])
        ]
        pw_new = [choice(category) for category, count in pw_categories for _ in range(count)]
        shuffle(pw_new)
        pw_user = "".join(pw_new)
        return pw_user

    def encrypt_data(self, data):
        encrypted_data = self.cipher_suite.encrypt(data.encode())
        json_encrypt_data = encrypted_data.decode('utf-8')
        return json_encrypt_data

    def decrypt_data(self, encrypt_data):
        byte_format_data = encrypt_data.encode('utf-8')
        if self.cipher_suite is not None:
            return self.cipher_suite.decrypt(byte_format_data)

    def generate_security_key(self):
        key = Fernet.generate_key()
        return key

    def insert_security_key(self, key):
        try:
            self.cipher_suite = Fernet(key)
            return True
        except Exception as error:
            return error
