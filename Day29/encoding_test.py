from cryptography.fernet import Fernet

# Generiere einen 128-Bit-Schlüssel für die Verschlüsselung
key = Fernet.generate_key()
cipher_suite = Fernet(key)

def encrypt_password(password):
    # Verschlüssele das Passwort mit dem generierten Schlüssel
    encrypted_password = cipher_suite.encrypt(password)
    return encrypted_password

def save_encrypted_password_to_file(encrypted_password):
    with open('encrypted_password.bin', 'wb') as file:
        file.write(encrypted_password)

def load_encrypted_password_from_file():
    with open('encrypted_password.bin', 'rb') as file:
        return file.read()

# Beispiel: Passwort verschlüsseln und in Datei speichern
password = b"geheimes_passwort"  # Als Bytes, um es zu verschlüsseln
encrypted = encrypt_password(password)
save_encrypted_password_to_file(encrypted)

# Beispiel: Aus Datei laden und entschlüsseln
loaded_encrypted = load_encrypted_password_from_file()
decrypted_password = cipher_suite.decrypt(loaded_encrypted).decode()
print(encrypted)
print("Entschlüsseltes Passwort:", decrypted_password)