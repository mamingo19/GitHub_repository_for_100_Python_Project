from tabnanny import check
from tkinter import *
import random
import csv
import pandas
from streamlit import image

BG_COLOR = "#B1DDC6"
#-----------------------read data---------------------------#
'''There much be words_to_learn.csv or french_words.csv or else the code will not compile'''
try:
    data = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    data2 = pandas.read_csv("data/french_words.csv")
    words = data2.to_dict(orient="records")
else:
    words = data.to_dict(orient="records")
current_card = {}


#--------------------------Function-------------------------#
def check_word():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(words)
    canvas.itemconfig(card_bg, image = french_logo)
    canvas.itemconfig(card_title, text = "French", fill = "black")
    canvas.itemconfig(card_word, text=current_card["French"], fill = "black")
    flip_timer = window.after(3500, func=flip_card)

def flip_card():
    canvas.itemconfig(card_bg, image = english_logo)
    canvas.itemconfig(card_title, text = "English", fill = "white")
    canvas.itemconfig(card_word, text = current_card["English"], fill = "white")

def already_checked():
    words.remove(current_card)
    words_to_learn = pandas.DataFrame(words)
    words_to_learn.to_csv("data/words_to_learn", index = False)

    check_word()

#-----------------------------UI----------------------------#
window = Tk()
window.title("Flash Card")
window.config(padx = 50, pady = 50, bg = BG_COLOR)

flip_timer = window.after(3500, func = flip_card)

#import the images
canvas = Canvas(width=800, height = 526, bg = BG_COLOR, highlightthickness=0)
french_logo = PhotoImage(file = "images/card_front.png")
english_logo = PhotoImage(file = "images/card_back.png")
right_logo = PhotoImage(file = "images/right.png")
wrong_logo = PhotoImage(file = "images/wrong.png")

#Canvas
card_bg = canvas.create_image(400,263, image = french_logo)
canvas.grid(column = 0, columnspan = 2, row = 0)
card_title = canvas.create_text(400,150,text = "", font = ("Ariel", 40, "italic"))
card_word = canvas.create_text(400,263,text = "", font = ("Ariel", 60, "bold"))

right_button = Button(image = right_logo, highlightthickness=0, command=check_word)
right_button.grid(column = 1, row = 1)
wrong_button = Button(image = wrong_logo, highlightthickness=0, command=already_checked)
wrong_button.grid(column = 0, row = 1)

check_word()

window.mainloop()
