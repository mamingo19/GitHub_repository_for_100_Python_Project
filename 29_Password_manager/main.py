from tkinter import *
from tkinter import messagebox
import random
import pyperclip


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
#Password Generator Project
def generate_password_func():
    password_entry.delete(0, END)
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [random.choice(letters) for _ in range(random.randint(8, 10))]
    password_symbols = [random.choice(symbols) for _ in range(random.randint(2, 4))]
    password_numbers = [random.choice(numbers) for _ in range(random.randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers
    random.shuffle(password_list)

    password = "".join(password_list)
    password_entry.insert(0, password)
    pyperclip.copy(password)
# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Alert", message="missing some info")
    else:
        is_okay = messagebox.askokcancel(title="Notification", message = f"This is your new account info\n"
                                                           f"Email: {email}\nPassword: {password}\nIs it okay to save?")
        if is_okay:
            with open("my_password.txt", "a") as data_file:
                data_file.write(f"The website: {website} | Email used: {email} | password: {password}\n")
                website_entry.delete(0, END)
                password_entry.delete(0, END)

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Generator")
window.config(padx = 20, pady = 20)

canvas = Canvas(width = 200, height = 200)
logo = PhotoImage(file = "logo.png")
canvas.create_image(100,100, image = logo)
canvas.grid(column = 1, row = 0)

#Labels
website_label = Label(text = "Website:")
website_label.grid(column = 0, row = 1)
email_label = Label(text = "Email/Username:")
email_label.grid(column = 0, row = 2)
password_label = Label(text = "Password:")
password_label.grid(column = 0, row = 3)

#Entries
website_entry = Entry(width = 50)
website_entry.grid(column = 1,columnspan = 2, row = 1)
website_entry.focus()
email_entry = Entry(width = 50)
email_entry.grid(column = 1,columnspan = 2, row = 2)
email_entry.insert(0,"example@gmail")
password_entry = Entry(width = 32)
password_entry.grid(column = 1, row = 3)

#Buttons
generate_password_button = Button(text="Generate password", command = generate_password_func)
generate_password_button.grid(column = 2, row = 3)
add_button = Button(text = "Add", width = 42, command = save)
add_button.grid(column = 1, columnspan = 2, row = 4)

window.mainloop()