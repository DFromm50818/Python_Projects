from random import randint, choice, shuffle
import pyperclip
from cryptography.fernet import Fernet
import string

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
        conditions = [
            len(digits) >= 3 and len(symbols) >= 3 and len(letter_upper) >= 4 and len(letter_lower) >= 4,
            len(digits) >= 2 and len(symbols) >= 2 and len(letter_upper) >= 3 and len(letter_lower) >= 3
        ]
        self.light = "green" if any(conditions) else "yellow" if password else "red"
        return self.light

    def generate_password(self):
        pw_categories = [
            (string.ascii_uppercase, randint(4, 8)),
            (string.ascii_lowercase, randint(4, 8)),
            (string.digits, randint(3, 6)),
            (string.punctuation, randint(3, 6))
        ]
        pw_new = [choice(category) for category, count in pw_categories for _ in range(count)]
        shuffle(pw_new)
        pw = "".join(pw_new)
        pyperclip.copy(pw)
        self.encrypt_password(pw)
        self.pw_user = pw

    def encrypt_password(self, password):
        self.encrypted_pw = self.cipher_suite.encrypt(password.encode())
        return self.encrypted_pw

    def decrypt_password(self, encrypt_pw):
        return self.cipher_suite.decrypt(encrypt_pw)


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