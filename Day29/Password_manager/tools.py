from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
from random import randint, choice, shuffle
import pyperclip
from cryptography.fernet import Fernet
import json
from tkinter import ttk

class PasswordTools:
    def __init__(self):
        self.light = "grey"
        self.pw_user = ""

    def password_check(self, password):
        print(password)
        digits = ''.join(filter(str.isdigit, password))
        letter_lower = ''.join(filter(str.islower, password))
        letter_upper = ''.join(filter(str.isupper, password))
        symbols = ''.join(filter(lambda x: not x.isalnum(), password))
        if len(digits) >= 3 and len(symbols) >= 3 and len(letter_upper) >= 4 and len(letter_lower) >= 4:
            self.light = "green"
        elif len(digits) >= 2 and len(symbols) >= 2 and len(letter_upper) >= 3 and len(letter_lower) >= 3:
            self.light = "yellow"
        else:
            self.light = "red"

    def generate_password(self):
        letters_upper = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
                         'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
        letters_lower = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's',
                         't', 'u',
                         'v', 'w', 'x', 'y', 'z']
        numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

        pw_new = [choice(letters_upper) for _ in range(randint(4, 5))] + \
                 [choice(letters_lower) for _ in range(randint(4, 5))] + \
                 [choice(symbols) for _ in range(randint(3, 4))] + \
                 [choice(numbers) for _ in range(randint(3, 4))]

        shuffle(pw_new)
        self.pw_user = "".join(pw_new)
        # Gui. .insert(0, string=f"{pw_user}")
        # entry_pw.insert(END, string=PasswordTools.generate_password)
        pyperclip.copy(self.pw_user)
        # return self.pw_user