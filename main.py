from tkinter import *
import pandas
import random
BACKGROUND_COLOR = "#B1DDC6"

# Create New Flash Cards
try:
    data = pandas.read_csv("data/word_to_learn.csv")
except FileNotFoundError:
    data = pandas.read_csv("data/french_words.csv")

to_learn = data.to_dict(orient="records")
current_word = {}


def word_generator():
    global current_word, flip_timer
    window.after_cancel(flip_timer)
    current_word = random.choice(to_learn)
    french_word = current_word["French"]
    canvas.itemconfig(title, text="French", fill="black")
    canvas.itemconfig(word, text=french_word, fill="black")
    canvas.itemconfig(canvas_image, image=front_img)
    flip_timer = window.after(3000, flip)


def check():
    to_learn.remove(current_word)
    updated_data = pandas.DataFrame(to_learn)
    updated_data.to_csv("data/word_to_learn.csv", index=False)
    word_generator()


def flip():
    canvas.itemconfig(canvas_image, image=back_img)
    canvas.itemconfig(title, text="English", fill="white")
    english_word = current_word["English"]
    canvas.itemconfig(word, text=english_word, fill="white")


# User Interface (UI)
window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
flip_timer = window.after(3000, flip)

canvas = Canvas(width=800, height=526, highlightthickness=0)
front_img = PhotoImage(file="images/card_front.png")
back_img = PhotoImage(file="images/card_back.png")
canvas_image = canvas.create_image(400, 263, image=front_img)
canvas.grid(row=0, column=0, columnspan=2)
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)


title = canvas.create_text(400, 150, text="", font=("Ariel", 40, "italic"))
word = canvas.create_text(400, 263, text="", font=("Ariel", 60, "bold"))


right_img = PhotoImage(file="images/right.png")
wrong_img = PhotoImage(file="images/wrong.png")
right_button = Button(image=right_img, highlightthickness=0, command=check)
wrong_button = Button(image=wrong_img, highlightthickness=0, command=word_generator)
right_button.grid(row=1, column=1)
wrong_button.grid(row=1, column=0)

word_generator()


window.mainloop()


