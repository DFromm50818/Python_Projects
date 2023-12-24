from random import randint, choice, shuffle
from cryptography.fernet import Fernet
import string


class PasswordTools:
    def __init__(self):
        self.light = "grey"
        self.key = Fernet.generate_key()
        self.cipher_suite = Fernet(b'L7CRVk_CnF40i9exhmYzS397F-XGYvNh0QJ2fi5O4GU=')

    def password_check(self, password):
        digits = ''.join(filter(str.isdigit, password))
        letter_lower = ''.join(filter(str.islower, password))
        letter_upper = ''.join(filter(str.isupper, password))
        symbols = ''.join(filter(lambda x: not x.isalnum(), password))
        conditions = [
            len(digits) >= 3 and len(symbols) >= 3 and len(letter_upper) >= 4 and len(letter_lower) >= 4,
            len(digits) >= 2 and len(symbols) >= 2 and len(letter_upper) >= 3 and len(letter_lower) >= 3
        ]
        self.light = "strong" if any(conditions) else "medium" if password else "weak"
        return self.light

    def generate_password(self):
        pw_categories = [
            (string.ascii_uppercase, randint(5, 10)),
            (string.ascii_lowercase, randint(5, 10)),
            (string.digits, randint(4, 8)),
            (string.punctuation, randint(4, 8))
        ]
        pw_new = [choice(category) for category, count in pw_categories for _ in range(count)]
        shuffle(pw_new)
        pw_user = "".join(pw_new)
        return pw_user

    def encrypt_password(self, password):
        encrypted_pw = self.cipher_suite.encrypt(password.encode())
        json_encrypt_pw = encrypted_pw.decode('utf-8')
        return json_encrypt_pw

    def decrypt_password(self, encrypt_pw):
        byte_format_password = encrypt_pw.encode('utf-8')
        return self.cipher_suite.decrypt(byte_format_password)
