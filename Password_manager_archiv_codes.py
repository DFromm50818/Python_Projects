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


    # def insert_key(self, key):
    #     self.cipher_suite = Fernet(key)
    #
    # def generate_key(self):
    #     key = Fernet.generate_key()
    #     print(key)
    #     return key


    # self.button_load_key = Button(self.parent, text="Load Key", command=self.messagebox_open_key, bg=BLACK, fg=WHITE, width=15)
    # self.button_load_key.grid(row=0, column=0)
    #
    # self.button_save_key = Button(self.parent, text="Save Key", command=lambda: self.data.save_key(self.tools.key), bg=BLACK, fg=WHITE, width=15)
    # self.button_save_key.grid(row=0, column=2)
    #
    # self.button_generate_key = Button(self.parent, text="Generate Key", command=lambda: self.generate_key_button, bg=BLACK, fg=WHITE, width=15)
    # self.button_generate_key.grid(row=0, column=1)


    # def messagebox_open_key(self):
    #     encrypt_key = self.data.open_file_key()
    #     if encrypt_key:
    #         try:
    #             # byte_format_password = encrypt_key.encode('utf-8')
    #             self.tools.insert_key(encrypt_key)
    #             print(encrypt_key)
    #         except Exception as e:
    #             print("Fehler beim Laden des Schlüssels:", e)
    #             return None
    #
    # # def messagebox_save_key(self):
    # def generate_key_button(self):
    #     key = self.tools.insert_key(self.tools.generate_key())
    #     self.data.save_key(key)