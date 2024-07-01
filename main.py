from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import random
import pyperclip

# ---------------------------- CONSTANTS ------------------------------- #
WHITE = "#FFFFFF"


# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v',
               'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q',
               'R',
               'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = []

    password_list += [random.choice(letters) for char in range(nr_letters)]
    password_list += [random.choice(symbols) for char in range(nr_symbols)]
    password_list += [random.choice(numbers) for char in range(nr_numbers)]
    shuffle(password_list)

    password = "".join(password_list)

    password_input.insert(0, password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    password = password_input.get()
    email = email_input.get()
    website = website_input.get()

    if len(website) == 0 or len(password) == 0:
        messagebox.showwarning(title="Warning", message="Please don't leave any fields empty")
    else:
        is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered: \nEmail: {email} "

                                                              f"\nPassword: {password} \nIs it ok to save?")
    if is_ok:
        data = open("data.txt", "a")
        data.write(f"{password} {email} {website}\n")
        data.close()

        # Clear the entry fields
        password_input.delete(0, END)
        email_input.delete(0, END)
        website_input.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)

canvas = Canvas(window, width=200, height=200, bg=WHITE, highlightthickness=0)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=0, columnspan=3)

# Label for "Website"
website_label = Label(text="Website:")
website_label.grid(column=0, row=1)

# Entry widget for website input
website_input = Entry(width=35)
website_input.grid(column=1, row=1, columnspan=2)

# Label for "Email"
email_label = Label(text="Email:")
email_label.grid(column=0, row=2)

# Entry widget for email input
email_input = Entry(width=35)
email_input.grid(column=1, row=2, columnspan=2)

# Label for "Password"
password_label = Label(text="Password:")
password_label.grid(column=0, row=3)

# Entry widget for password
password_input = Entry(width=20)
password_input.grid(column=1, row=3, sticky="W")

# Button to generate the password
generatepass_button = Button(text="Generate Password", width=15, command=generate_password)
generatepass_button.grid(column=2, row=3, sticky="E")

# Button to add the information
add_button = Button(text="Add", width=36, command=save)
add_button.grid(column=1, row=4, columnspan=2)

window.mainloop()
