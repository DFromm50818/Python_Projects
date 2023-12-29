import tkinter as tk
from tkinter import ttk

window =tk.Tk()
window.title("Layout Test")
window.geometry("600x400")

frame = ttk.Frame(window, width=200, height=200, borderwidth=10, relief=tk.GROOVE)
frame.pack_propagate(False)
frame.pack(side="left")

# parenting /master setting
label = ttk.Label(frame, text="Label in frame")
label.pack()

button = ttk.Button(frame, text="button in frame")
button.pack()

# example
label2 = ttk.Label(window, text="Label outside frame")
label2.pack(side="right")

# exercise

frame1 = ttk.Frame(window, width=200, height=200, borderwidth=10, relief=tk.GROOVE)
frame1.pack_propagate(False)
frame1.pack(side="left")

# parenting /master setting
label1 = ttk.Label(frame1, text="Label in frame")
label1.grid(row=0, column=0)

button1 = ttk.Button(frame1, text="button in frame")
button1.grid(row=1, column=0)

entry1 = ttk.Entry(frame1, width=30)
entry1.grid(row=2, column=0)
# label1 = ttk.Label(text="Label1", background="red")
# label2 = ttk.Label(text="Label2", background="blue")

#pack
# label1.pack(side="left", expand=True, fill= "both")
# label2.pack(side="left", expand=True, fill="both")

#grid
# window.columnconfigure(0, weight=1)
# window.columnconfigure(1, weight=1)
# window.columnconfigure(2, weight=2)
# window.rowconfigure(0, weight=1)
# window.rowconfigure(1, weight=1)
#
# label1.grid(row=0, column=1, sticky="nesw")
# label2.grid(row=1, column=1, columnspan=2, sticky="nesw")

#place
# label1.place(x=100, y=200, width=200, height=100)
# label2.place(relx=0.5,rely=0.5, relwidth=1, anchor="center")

#run
window.mainloop()
