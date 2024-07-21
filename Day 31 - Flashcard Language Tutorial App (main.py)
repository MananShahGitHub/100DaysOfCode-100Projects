import tkinter as tk
from tkinter import PhotoImage, Canvas, Button
import pandas as pd
import random
import os

# Create the main window
window = tk.Tk()
window.title("Flash Card App")
window.config(padx=50, pady=50, bg="#B1DDC6")

BACKGROUND_COLOR = "#B1DDC6"

# Load images
card_back_img = PhotoImage(file="images/card_back.png")
right_img = PhotoImage(file="images/right.png")
card_front_img = PhotoImage(file="images/card_front.png")
wrong_img = PhotoImage(file="images/wrong.png")

# Original approach: Check if the words_to_learn.csv file exists
# if os.path.exists("data/words_to_learn.csv"):
#     data = pd.read_csv("data/words_to_learn.csv")
# else:
#     data = pd.read_csv("data/french_words.csv")
#
# to_learn = data.to_dict(orient="records")

# Try to load words_to_learn.csv, fall back to french_words.csv if not found
try:
    data = pd.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    original_data = pd.read_csv("data/french_words.csv")
    print(original_data)
    to_learn = original_data.to_dict(orient="records")
else:
    to_learn = data.to_dict(orient="records")

# Function to pick a new random word
current_card = {}
flip_timer = None


def next_card():
    global current_card, flip_timer
    if flip_timer is not None:
        window.after_cancel(flip_timer)  # Cancel the previous timer if it exists
    current_card = random.choice(to_learn)  # Pick a new random word
    canvas.itemconfig(card_title, text="French", fill="black")
    canvas.itemconfig(card_word, text=current_card["French"], fill="black")
    canvas.itemconfig(flash_card, image=card_front_img)
    flip_timer = window.after(3000, flip_card)  # Set a new timer


def flip_card():
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=current_card["English"], fill="white")
    canvas.itemconfig(flash_card, image=card_back_img)


def save():
    global to_learn
    to_learn.remove(current_card)  # Remove the current word from the list
    new_data = pd.DataFrame(to_learn)  # Convert the list of dictionaries to a DataFrame
    new_data.to_csv('data/words_to_learn.csv', index=False)  # Save to a new CSV file
    next_card()  # Show the next card


# Create a Canvas for the flash card
canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
flash_card = canvas.create_image(400, 263, image=card_front_img)
card_title = canvas.create_text(400, 150, text="Title", font=("Ariel", 40, "italic"))
card_word = canvas.create_text(400, 263, text="Word", font=("Ariel", 60, "bold"))
canvas.grid(row=0, column=0, columnspan=2)

# Create buttons
wrong_button = Button(image=wrong_img, highlightthickness=0, command=next_card)
wrong_button.grid(row=1, column=0)

right_button = Button(image=right_img, highlightthickness=0, command=save)
right_button.grid(row=1, column=1)

# Initialize the first card
next_card()

# Run the window's main loop
window.mainloop()
