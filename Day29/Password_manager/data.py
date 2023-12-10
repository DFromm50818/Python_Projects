from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
from random import randint, choice, shuffle
import pyperclip
from cryptography.fernet import Fernet
import json

from tkinter import ttk

class Data:
    def __init__(self):
        self.json_data_path = filedialog.askopenfilename(filetypes=[("JSON files", "*.json")])
        self.read_file = []

    def open_json_file(self):
        try:
            # self.json_data_path = filedialog.askopenfilename(filetypes=[("JSON files", "*.json")])
            with open(self.json_data_path, "r") as file:
                self.read_file = json.load(file)
        except:
            return None

    def save_data(self, website, user, password):
        new_entry = {"Website": website, "Email/Username": user, "Password": password}
        self.read_file.append(new_entry)
        with open(self.json_data_path, "w") as read_data:
            json.dump(self.read_file, read_data, indent=4, ensure_ascii=False)



