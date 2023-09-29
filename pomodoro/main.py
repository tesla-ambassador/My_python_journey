from tkinter import *
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    global reps
    window.after_cancel(timer)
    canvas.itemconfig(self_timer, text='00:00')
    check.config(text='')
    text_label.config(text='TIMER', fg=GREEN)
    reps = 0

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    reps += 1
    if reps % 8 == 0:
        countdown(LONG_BREAK_MIN * 60)
        text_label.config(text='BREAK', fg=RED)
    elif reps % 2 == 0:
        countdown(SHORT_BREAK_MIN * 60)
        text_label.config(text='BREAK', fg=PINK)
    else:
        countdown(WORK_MIN * 60)
        text_label.config(text='WORK', fg=GREEN)
        

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def countdown(count):
    global reps
    global timer
    count_min = math.floor(count/60)
    count_sec = count % 60
    if count_sec < 10:
    #  count_sec = "0"+str(count_sec)
        count_sec = f"0{count_sec}"
        canvas.itemconfig(self_timer, text=f"{count_min}:{count_sec}")
    if count > 0:
        timer = window.after(1000, countdown, count - 1)
    else:
        start_timer()
        mark = ''
        for _ in range(math.floor(reps/2)):
             mark += '✔'
        check.config(text=mark)

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro App")
window.config(padx=100, pady=50, background=YELLOW)

photo_image = PhotoImage(file='pomodoro/tomato.png')
canvas = Canvas(width=200, height=224, background=YELLOW, highlightthickness=0)
canvas.create_image(100, 112, image=photo_image)
self_timer = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=2, row=2)

text_label = Label(text='TIMER', fg=GREEN, bg=YELLOW, font=(FONT_NAME, 45, 'bold'))
text_label.grid(column=2, row=1)

check = Label(text='✔', fg=GREEN, bg=YELLOW, font=(FONT_NAME, 35, 'bold'))
check.grid(column=2, row=4)

start_button = Button(text='Start', highlightthickness=0, command=start_timer)
start_button.grid(column=1, row=3)

reset_button = Button(text='Reset', highlightthickness=0, command=reset_timer)
reset_button.grid(column=3, row=3)


window.mainloop()