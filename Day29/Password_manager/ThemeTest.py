import tkinter as tk
from tkinter import ttk
from ttkthemes import ThemedStyle

def change_theme():
    selected_theme = theme_combobox.get()
    style.set_theme(selected_theme)

root = tk.Tk()
root.title("Theme Changer")

style = ThemedStyle(root)
style.set_theme("arc")  # Default theme

theme_label = ttk.Label(root, text="Select Theme:")
theme_label.pack()

themes = style.theme_names()
theme_combobox = ttk.Combobox(root, values=themes)
theme_combobox.pack()

apply_button = ttk.Button(root, text="Apply", command=change_theme)
apply_button.pack()

root.mainloop()
