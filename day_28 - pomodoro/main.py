import tkinter
import time
import math

def update_done_pomodoros_lb(n):
    done_pomodoros_lb.config(text="🍅" * n)

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
TOMATO = "🍅"
reps = 0
completed_work = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    global reps
    global completed_work
    reps = 0
    completed_work = 0
    window.after_cancel(timer)
    done_pomodoros_lb.config(text="")
    timer_lb.config(text="Timer")
    canvas.itemconfig(timer_text, text=f"00:00")

# ---------------------------- TIMER MECHANISM ------------------------------- # 

def start_timer():
    global reps
    global completed_work
    reps += 1

    if reps % 8 == 0:
        timer_lb.config(text="Break", bg = YELLOW, fg=RED, font=(FONT_NAME, 35, "bold"))
        count_down(LONG_BREAK_MIN * 60)
    elif reps % 2 == 0:
        timer_lb.config(text="Break", bg = YELLOW, fg=PINK, font=(FONT_NAME, 35, "bold"))
        count_down(SHORT_BREAK_MIN * 60)
    else:
        timer_lb.config(text="Work", bg = YELLOW, fg=GREEN, font=(FONT_NAME, 35, "bold"))
        count_down(WORK_MIN * 60)
        completed_work += 1 
    
    

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60
    
    if count_min < 10:
        count_min = f"0{count_min}"

    if count_sec < 10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        update_done_pomodoros_lb(completed_work)

# ---------------------------- UI SETUP ------------------------------- #

# widow setup
window = tkinter.Tk()
window.title("Pomoidoro 🍅")
window.config(padx=100, pady=50, bg=YELLOW)

# window.minsize(height=500, width=500)

# canvas set up - canvcas widget to show tomato image and timer text 
canvas = tkinter.Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = tkinter.PhotoImage(file ="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

# labels setup -------------------------------
timer_lb = tkinter.Label(text="Timer", bg = YELLOW, fg=GREEN, font=(FONT_NAME, 35, "bold"))
timer_lb.grid(column=1, row=0)

done_pomodoros_lb = tkinter.Label(text=" ", bg = YELLOW, fg=GREEN, font=(FONT_NAME, 35, "bold"))
done_pomodoros_lb.grid(column=1, row=3)

# buttons setup -------------------------------
start_btn = tkinter.Button(text="Start", padx=20, pady=5, highlightthickness=0, command=start_timer)
start_btn.grid(column=0, row=2)

reset_btn = tkinter.Button(text="Reset", padx=20, pady=5, highlightthickness=0, command=reset_timer)
reset_btn.grid(column=2, row=2)



window.mainloop()