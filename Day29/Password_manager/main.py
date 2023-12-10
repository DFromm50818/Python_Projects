from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
from random import randint, choice, shuffle
import pyperclip
from cryptography.fernet import Fernet
import json
from tkinter import ttk
import data
import interface
import tools

BLACK = "black"
WHITE = "white"

if __name__ == "__main__":
    root = Tk()
    interface.WindowGUI(root)
    root.mainloop()








# gui = interface.WindowGui()



# password_tools = tools.PasswordTools()

# key = Fernet.generate_key()
# cipher_suite = Fernet(b'o5mH4zyX11wzn-dtIYaV1SmHcDLsN-ClpelY9WD3uP8=')


# def open_file_key():
#     try:
#         key_file = filedialog.askopenfilename(filetypes=[("DAT files", "*.dat")])
#         with open(key_file, "rb") as file:
#             passkey = file.read()
#         return passkey
#     except:
#         return None
# cipher_suite = Fernet(open_file())
# print(cipher_suite)

# def open_file_key():
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

# def encrypt_password(password):
#     encrypted_password = cipher_suite.encrypt(password)
#     return encrypted_password

# def pw_signal_check():
#     password = entry_pw.get()
#     digits = ''.join(filter(str.isdigit, password))
#     letter_lower = ''.join(filter(str.islower, password))
#     letter_upper = ''.join(filter(str.isupper, password))
# #     symbols = ''.join(filter(lambda x: not x.isalnum(), password))
#     if len(digits) >= 3 and len(symbols) >= 3 and len(letter_upper) >= 4 and len(letter_lower) >= 4:
#
#     elif len(digits) >= 2 and len(symbols) >= 2 and len(letter_upper) >= 3 and len(letter_lower) >= 3:
#         canvas_oval.create_oval(1, 1, 19, 19, outline="black", fill=password_tools.light)
#     else:
#         canvas_oval.create_oval(1, 1, 19, 19, outline="black", fill=password_tools.light)
#     canvas.after(250, password_check)

# def generate_password():
#     entry_pw.delete(0, END)
#
#     letters_upper = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
#                'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
#     letters_lower = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
#                'v', 'w', 'x', 'y', 'z']
#     numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
#     symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
#
#     pw_new = [choice(letters_upper) for _ in range(randint(4, 5))] + \
#              [choice(letters_lower) for _ in range(randint(4, 5))] + \
#              [choice(symbols) for _ in range(randint(3, 4))] + \
#              [choice(numbers) for _ in range(randint(3, 4))]
#
#     shuffle(pw_new)
#     pw_user = "".join(pw_new)
#     entry_pw.insert(0, string=f"{pw_user}")
#     pyperclip.copy(pw_user)

# def check_save():
#     if len(entry_website.get()) == 0 or len(entry_user.get()) == 0 or len(entry_pw.get()) == 0:
#         messagebox.showerror(title="Error!", message="The data could not be saved. Please fill out all entries.")
#
#     else:
#         rdy_to_save = messagebox.askokcancel(title="Are you sure you want to save?",
#                                              message=f"These are the details you entered: \n\nWebsite: "
#                                                      f"{entry_website.get()} \nEmail: {entry_user.get()} "
#                                                      f"\nPassword: {entry_pw.get()} \n\nIs it ok to save?")
#         if rdy_to_save == True:
#             data.save_data(entry_website.get(), entry_user.get(), entry_pw.get())
#             entry_website.delete(0, END)
#
#             entry_pw.delete(0, END)

            # encrypted_pw = encrypt_password(entry_pw.get().encode())
            # loaded_encrypted = encrypted_pw #load_encrypted_password_from_file()
            # decrypted_password = cipher_suite.decrypt(loaded_encrypted).decode()
            # print(decrypted_password)







# def combobox_option_selected(event):
#     selected_option = option_website.get()
#     entry_website.delete(0, END)
#     entry_website.insert(0, string=selected_option)
# option_website = StringVar(window)
# def check_password():
#     password_tools.password_check(password=entry_pw.get())
#     canvas.config(bg=password_tools.light)
# password_tools.password_check(gui.)
# canvas_oval.after(250, password_tools.password_check(password=entry_pw.get()))

# combobox = ttk.Combobox(window, textvariable=option_website, values=options)
# combobox.bind("<<ComboboxSelected>>", on_option_selected)
# combobox.grid(row=0, column=0)

# loaded_key = open_file()
#
# if loaded_key:
#     cipher_suite = Fernet(loaded_key)
#     print(cipher_suite)

# window.mainloop()
