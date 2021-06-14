from tkinter import *
BACKGROUND = "#FAF1E6"
first_key_press = 0
user_can_type = True
clock = None
time = 7


# --------START COUNTDOWN--------

def start_timer(t):
    global user_can_type, first_key_press

    if first_key_press >= 1:
        if t >= 0:
            timer.config(text=f"Time: {t} sec")
            global clock
            clock = window.after(1000, start_timer, t - 1)
        else:
            user_can_type = False
            text.config(state="disable")
            text.unbind('<Key>')


# ---------CHECK USER INPUT KEY--------

def key_press(event):
    global first_key_press, user_can_type, time, clock

    if first_key_press == 0:
        first_key_press += 1
        start_timer(time)
    else:
        if time <= 7:
            window.after_cancel(clock)
            time = 7
            start_timer(time)


# --------UI SET-UP --------

window = Tk()
window.title("Typing Speed Test")
window.config(padx=100, pady=100, bg=BACKGROUND)
window.geometry("1500x1000")

title = Label(text="---Dangerous Typing Prompt---", font="Times 40", bg=BACKGROUND)
title.grid(row=0, column=0)

text = Text(font="Times 22", bg="#FDFAF6", height=20, padx=20, pady=3)
text.grid(row=1, column=0, padx=20, pady=20)

timer = Label(text="Time: 7 sec", font="Times 30", bg=BACKGROUND)
timer.grid(row=4, column=0)

# --------BINDING FUNCTIONS--------
text.bind('<Key>', key_press)

window.mainloop()
