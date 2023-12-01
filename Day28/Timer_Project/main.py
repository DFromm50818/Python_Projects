from tkinter import *
import math

PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = ""

def timer_reset():
    global reps
    window.after_cancel(timer)
    label_title.config(text="Timer")
    label_checkmark.config(text="")
    canvas.itemconfig(timer_text, text="00:00")
    reps = 0

def timer_start():
    global reps
    reps += 1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps == 1 or reps == 3 or reps == 5 or reps == 7:
        countdown(work_sec)
        label_title.config(text="Work", fg=GREEN)
    elif reps == 2 or reps == 4 or reps == 6:
        countdown(short_break_sec)
        label_title.config(text="Break", fg=PINK)
    elif reps == 8:
        countdown(long_break_sec)
        label_title.config(text="Break", fg=RED)

def countdown(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"
    if count_min < 10:
        count_min = f"0{count_min}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, countdown, count -1)
    else:
        timer_start()
        print(reps)
        if reps == 2 or reps == 4 or reps == 6 or reps == 8:
            checkmark = "✔"
            current_text = label_checkmark.cget("text")
            combined_text = current_text + checkmark
            label_checkmark.config(text=combined_text)

window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(103, 130, text=f"00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

label_title = Label(text="Timer", font=(FONT_NAME, 30, "bold"), fg=GREEN, bg=YELLOW)
label_title.grid(column=1, row=0)

label_checkmark = Label(fg=GREEN, bg=YELLOW, highlightthickness=0)
label_checkmark.grid(column=1, row= 3)

button_start = Button(window, text="Start", command=timer_start, highlightthickness=0)
button_start.grid(column=0, row=2)

button_reset = Button(window, text="Reset", command=timer_reset, highlightthickness=0)
button_reset.grid(column=2, row=2)

window.mainloop()