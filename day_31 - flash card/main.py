from tkinter import *
import time
import pandas as pd
import random

BACKGROUND_COLOR = "#B1DDC6"
current_card = {}

# --------------------------- Functions ------------------------
def next_card():
    print(len(data_list))
    global current_card, flip_timer
    current_card = random.choice(data_list)
    window.after_cancel(flip_timer)

    canvas.itemconfig(canvas_img, image=card_front)
    canvas.itemconfig(title_text, text=f"French",fill="black")
    canvas.itemconfig(word_text, text=f"{current_card['French']}", fill="black")
    flip_timer = window.after(3000, flip)

    
def flip():
    global current_card    
    canvas.itemconfig(canvas_img, image=card_back)
    canvas.itemconfig(title_text, text=f"English", fill="white")
    canvas.itemconfig(word_text, text=f"{current_card['English']}", fill="white")
    

def known_card():
    global current_card
    next_card()
    data_list.remove(current_card)
    new_dtaframe = pd.DataFrame(data_list)
    new_dtaframe.to_csv("data\\words_to_learn.csv", index=False)


# --------------------------- Read File ------------------------
try:
    data = pd.read_csv("data\\words_to_learn.csv")
except FileNotFoundError:
    data = pd.read_csv("data\\french_words.csv")
finally:
    data_list = data.to_dict(orient="records")


# --------------------------- UI SETUP ------------------------
window = Tk()
window.title("FlashCard")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, flip)

card_back = PhotoImage(file="images\\card_back.png")
card_front = PhotoImage(file="images\\card_front.png")

canvas =  Canvas(height=526, width=800, highlightthickness=0, bg=BACKGROUND_COLOR)
canvas_img = canvas.create_image(400, 263, image=card_front)
title = "French"
title_text = canvas.create_text(400, 150, text=title, font=("Ariel", 40, "italic"))
word = "trouve"
word_text = canvas.create_text(400, 263, text=word, font=("Ariel", 60, "bold"))
canvas.grid(column=0, row=0, columnspan=2)


# Buttons setup
right_image = PhotoImage(file="images\\right.png")
right_button = Button(image=right_image, highlightthickness=0, command=known_card)
right_button.grid(column=1, row=1)

wrong_image = PhotoImage(file="images\\wrong.png")
no_button = Button(image=wrong_image, highlightthickness=0, command=next_card)
no_button.grid(column=0, row=1)


next_card()

mainloop()