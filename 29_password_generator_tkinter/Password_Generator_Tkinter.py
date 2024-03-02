from tkinter import *
from tkinter import messagebox
from random import randint, shuffle, choice
import pyperclip
# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def generate_password():
    field_password.delete(0, END)
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    random_letters_list = [choice(letters) for _ in range(randint(8, 10))]
    random_symbols_list = [choice(symbols) for _ in range(randint(2, 4))]
    random_numbers_list = [choice(numbers) for _ in range(randint(2, 4))]
    password_list = random_letters_list + random_symbols_list + random_numbers_list

    shuffle(password_list)
    new_password = "".join(password_list)
    field_password.insert(0, new_password)
    pyperclip.copy(new_password)
    messagebox.showinfo(title="Info", message="Password copied to clipboard!")
# ---------------------------- SAVE PASSWORD ------------------------------- #


def save():
    website = field_website.get()
    email = field_email.get()
    password = field_password.get()
    if len(website) == 0 or len(password) == 0:
        messagebox.showwarning(title="Oops", message="Please don't leave any fields empty!")
    else:
        its_ok = messagebox.askokcancel(title=field_website.get(), message=f"Details entered: \nEmail:"
                                        f" {field_email.get()}\nPassword: {field_password.get()}\nSave this?")
        if its_ok:
            with open("data.txt", "a") as f:
                f.write(f"{website} | ")
                field_website.delete(0, END)
                f.write(f"{email} | ")
                f.write(f"{password}\n")
                field_password.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)
canvas = Canvas(width=200, height=200)
image = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=image)
canvas.grid(column=1, row=0, sticky=EW)

website_label = Label(text="Website:")
website_label.grid(column=0, row=1)
field_website = Entry(width=35)
field_website.focus()
field_website.grid(column=1, row=1, columnspan=2, sticky=EW)

email_label = Label(text="Email/Username:")
email_label.grid(column=0, row=2)
field_email = Entry(width=35)
field_email.insert(0, "jacobzak11@gmail.com")
field_email.grid(column=1, row=2, columnspan=2, sticky=EW)

password_label = Label(text="Password:")
password_label.grid(column=0, row=3, sticky=EW)
field_password = Entry(width=21)
field_password.grid(column=1, row=3, sticky=EW)

button_generator = Button(text="Generate Password", highlightthickness=0, command=generate_password)
button_generator.grid(column=2, row=3, sticky=EW)

button_add = Button(text="Add", width=36, highlightthickness=0, command=save)
button_add.grid(column=1, row=4, columnspan=2, sticky=EW)
window.mainloop()
