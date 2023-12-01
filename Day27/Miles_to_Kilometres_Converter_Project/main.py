from tkinter import *

def calculate_km():
    if radio_state.get() == 0:
        km = round(float(input.get()) * 1.60934, 2)
        label_result.config(text=f"{km}")
    elif radio_state.get() == 1:
        mile = round(float(input.get()) / 1.60934, 2)
        label_result.config(text=f"{mile}")

def radio_used():
    radio_var = radio_state.get()
    if radio_var == 1:
        label_01 = Label(text="Km", font=("Arial", 13))
        label_01.grid(column=2, row=0)
        label_01.config(padx=10, pady=0)
        label_03 = Label(text="Miles", font=("Arial", 13))
        label_03.grid(column=2, row=1)
        label_03.config(padx=10, pady=0)
    else:
        label_01 = Label(text="Miles", font=("Arial", 13))
        label_01.grid(column=2, row=0)
        label_01.config(padx=10, pady=0)
        label_03 = Label(text="Km", font=("Arial", 13))
        label_03.grid(column=2, row=1)
        label_03.config(padx=10, pady=0)

window = Tk()
window.title("Mile to Km Converter")
window.minsize(width=400, height=200)
window.config(padx=50, pady= 50)

label_01 = Label(text="Miles", font=("Arial", 13))
label_01.grid(column=2, row=0)
label_01.config(padx=10, pady= 0)

label_02 = Label(text="is equal to", font=("Arial", 13))
label_02.grid(column=0, row=1)
label_02.config(padx=10, pady= 0)

label_03 = Label(text="Km", font=("Arial", 13))
label_03.grid(column=2, row=1)
label_03.config(padx=10, pady=0)

label_result = Label(text="0", font=("Arial", 13))
label_result.grid(column= 1, row= 1)

input = StringVar()
input = Entry(window, textvariable= input)
input.grid(column= 1, row=0)

button = Button(window, text="Calculate", command=calculate_km)
button.grid(column=1, row=2)

radio_state = IntVar()
radiobutton1 = Radiobutton(text="mile to km", value=0, variable=radio_state, command=radio_used)
radiobutton2 = Radiobutton(text="km to mile", value=1, variable=radio_state, command=radio_used)
radiobutton1.grid(column=0, row=3)
radiobutton2.grid(column=0, row=4)
radio_state.set(0)

window.mainloop()
