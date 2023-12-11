from tkinter import *
import interface


BLACK = "black"
WHITE = "white"

if __name__ == "__main__":
    root = Tk()
    interface.WindowGUI(root)
    root.mainloop()



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
