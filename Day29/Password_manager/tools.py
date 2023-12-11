from random import randint, choice, shuffle
import pyperclip
from cryptography.fernet import Fernet



class PasswordTools:
    def __init__(self):
        self.light = "grey"
        self.pw_user = ""
        self.encrypted_pw = b""
        self.key = Fernet.generate_key()
        self.cipher_suite = Fernet(b'o5mH4zyX11wzn-dtIYaV1SmHcDLsN-ClpelY9WD3uP8=')

    def password_check(self, password):
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
        return self.light

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
        pyperclip.copy(self.pw_user)
        self.encrypt_password()


    def encrypt_password(self):
        self.encrypted_pw = self.cipher_suite.encrypt(self.pw_user.encode())
        return self.encrypted_pw

    def decrypt_password(self, encrypt_pw):
        self.pw_user = self.cipher_suite.decrypt(encrypt_pw)
        return self.pw_user



    # loaded_encrypted = encrypted_pw  # load_encrypted_password_from_file()
    # decrypted_password = cipher_suite.decrypt(loaded_encrypted).decode()
    # print(decrypted_password)

    # cipher_suite = Fernet(self.open_file_key())
    # def open_file_key(self):
    #     try:
    #         key_file = filedialog.askopenfilename(filetypes=[("DAT files", "*.dat")])
    #         with open(key_file, "rb") as file:
    #             passkey = file.read()
    #         if len(passkey) == 32:  # Stelle sicher, dass der Schlüssel die richtige Länge hat
    #             return passkey
    #         else:
    #             raise ValueError("Ungültiger Schlüssel")
    #     except Exception as e:
    #         print("Fehler beim Laden des Schlüssels:", e)
    #         return None