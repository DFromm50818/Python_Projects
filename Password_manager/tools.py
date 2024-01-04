from random import randint, choice, shuffle
from cryptography.fernet import Fernet
import string


class PasswordTools:
    def __init__(self):
        self.light = "grey"
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
        print(pw_categories)
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
        return self.cipher_suite.decrypt(byte_format_data)

    def generate_security_key(self):
        key = Fernet.generate_key()
        return key

    def insert_security_key(self, key):
        try:
            self.cipher_suite = Fernet(key)
            return True
        except:
            return None
