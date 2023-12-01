from tkinter import *

# def calculate_km():
#     if radio_state.get() == 0:
#         km = round(float(input.get()) * 1.60934, 2)
#         label_result.config(text=f"{km}")
#     elif radio_state.get() == 1:
#         mile = round(float(input.get()) / 1.60934, 2)
#         label_result.config(text=f"{mile}")

def listbox_from_used(event):
    from_measure = listbox_from.get(listbox_from.curselection())
    print(from_input_dict)
    return from_measure

def listbox_to_used(event):
    print(listbox_to.get(listbox_to.curselection()))

window = Tk()
window.title("Mile to Km Converter")
window.minsize(width=400, height=200)
window.config(padx=50, pady= 50)

label_01 = Label(text="Miles", font=("Arial", 13))
label_01.grid(column=2, row=0)
label_01.config(padx=10, pady= 0)

label_02 = Label(text="is equal to", font=("Arial", 13))
label_02.grid(column=2, row=0)
label_02.config(padx=10, pady= 0)

label_result = Label(text="0", font=("Arial", 13))
label_result.grid(column= 3, row= 0)

user_input = StringVar()
user_input = Entry(window, textvariable= user_input)
user_input.grid(column= 0, row=0)

button = Button(window, text="Calculate", command=listbox_to_used)
button.grid(column=1, row=2)

listbox_from = Listbox(height=5)
from_measure = ["mm", "cm", "dm", "m", "km"]
for item in from_measure:
    listbox_from.insert(from_measure.index(item), item)
listbox_from.bind("<<ListboxSelect>>", listbox_from_used)
listbox_from.grid(column=1, row=0)

listbox_to = Listbox(height=5)
to_measure = ["mm", "cm", "dm", "m", "km"]
for item in to_measure:
    listbox_to.insert(to_measure.index(item), item)
listbox_to.bind("<<ListboxSelect>>", listbox_to_used)
listbox_to.grid(column=4, row=0)

from_input_dict = {"input": user_input.get(),
                       "measure": listbox_from_used}

window.mainloop()
