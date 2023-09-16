from tkinter import *
import time
import math

timer = None


def start_timer():

    seconds = 60
    count_down(seconds)


def count_down(count):

    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec == 0 or (count_sec < 10 and count_min == 0):
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)


window = Tk()
window.title("Typing Speed Test App")
window.minsize(width=600, height=500)
window.config(padx=50, pady=20)

# Insert title label
# Insert function for

title_label = Label(text="Test your typing speed: ", font=("Ariel", 20, "bold"))
title_label.pack()
title_label.config(justify="left", anchor="s")

test_entry = Text(width=50, height=15)
test_entry.pack()
test_entry.focus()

canvas = Canvas(width=200, height=120, highlightthickness=0)
timer_title = canvas.create_text(100, 50, text="Timer", font=("Courier", 24, "bold"))
timer_text = canvas.create_text(100, 100, text="00:00", font=("Courier", 35, "bold"))
canvas.pack()

start_btn = Button(text="Start", font=("Courier", 24, "bold"), command=start_timer)
start_btn.pack()
# Insert speed result below timer

window.mainloop()
