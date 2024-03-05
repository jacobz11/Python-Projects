from tkinter import *
import pandas
from random import choice
BACKGROUND_COLOR = "#B1DDC6"
current_card = {}
list_dict = {}

try:
    data = pandas.read_csv("./data/words_to_learn.csv")
except FileNotFoundError:
    original_data = pandas.read_csv("./data/french_words.csv")
    list_dict = original_data.to_dict(orient="records")
else:
    list_dict = data.to_dict(orient="records")


def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = choice(list_dict)
    canvas.itemconfig(title, text="French", fill="black")
    canvas.itemconfig(word, text=current_card["French"], fill="black")
    canvas.itemconfig(card_background, image=image_card_front)
    flip_timer = window.after(3000, func=flip_card)


def flip_card():
    canvas.itemconfig(title, text="English", fill="white")
    canvas.itemconfig(word, text=current_card["English"], fill="white")
    canvas.itemconfig(card_background, image=image_card_back)


def is_known():
    list_dict.remove(current_card)
    next_card()
    data_known = pandas.DataFrame(list_dict)
    data_known.to_csv("./data/words_to_learn.csv", index=False)


window = Tk()
window.title("Flash Card")
window.config(padx=50, pady=50)
window.config(bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, func=flip_card)

canvas = Canvas(width=800, height=526)
image_card_front = PhotoImage(file="./images/card_front.png")
card_background = canvas.create_image(400, 263, image=image_card_front)
image_card_back = PhotoImage(file="./images/card_back.png")
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row=0, column=0, columnspan=2)

image_right = PhotoImage(file="./images/right.png")
image_right_button = Button(image=image_right, highlightthickness=0, command=is_known)
image_right_button.grid(row=1, column=1)

image_wrong = PhotoImage(file="./images/wrong.png")
image_wrong_button = Button(image=image_wrong, highlightthickness=0, command=next_card)
image_wrong_button.grid(row=1, column=0)


title = canvas.create_text(400, 150, text="", fill="black", font=("Arial", 40, "italic"))
word = canvas.create_text(400, 265, text="", fill="black", font=("Arial", 60, "bold"))

next_card()
window.mainloop()
