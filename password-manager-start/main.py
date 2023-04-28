import json
from tkinter import *
from tkinter import messagebox
import password_generator as pg
import clipboard
import pandas as pd


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def password_generator():
    password_input.delete(0, END)
    pw = pg.password_generator()
    password_input.insert(0, pw)
    clipboard.copy(pw)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    new_data = {
        website_input.get(): {
            "email": email_input.get(),
            "password": password_input.get(),
        }
    }
    if not website_input.get() or not email_input.get() or not password_input.get():
        messagebox.showerror(message="No Website")
    else:
        is_ok = messagebox.askokcancel(title=website_input.get(), message="abc")
        if is_ok:
            try:
                with open("data.json", "r") as data_file:
                    # read old data
                    data = json.load(data_file)
            except FileNotFoundError:
                with open("data.json", "w") as data_file:
                    json.dump(new_data, data_file, indent=4)
            else:
                # Updating data with new data
                data.update(new_data)
                with open("data.json", "w") as data_file:
                    # Saving updated data
                    json.dump(data, data_file, indent=4)
            finally:
                website_input.delete(0, END)
                # email_input.delete(0, END)
                password_input.delete(0, END)


# ---------------------------- SEARCH ----------------------------------#
def search():
    website = website_input.get()
    with open("data.json", "r") as data_file:
        data = json.load(data_file)
        if website in data:
            email = data[website]["email"]
            password = data[website]["password"]
            messagebox.showinfo(title=website, message=f"email:{email}\n password:{password}")

        pass


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=1, row=0)

# Labels
website_label = Label(text="Website:")
website_label.grid(column=0, row=1)
email_label = Label(text="Email/Username:")
email_label.grid(column=0, row=2)
password_label = Label(text="Password:")
password_label.grid(column=0, row=3)

# Entries
website_input = Entry(width=32)
website_input.grid(column=1, row=1)
website_input.focus()
email_input = Entry(width=50)
email_input.grid(column=1, row=2, columnspan=2)
email_input.insert(0, "abc@gmail.com")
password_input = Entry(width=32)
password_input.grid(column=1, row=3)

# Buttons
search_button = Button(text="Search", width=14, command=search)
search_button.grid(column=2, row=1)
generate_button = Button(text="Generate Password", width=14, command=password_generator)
generate_button.grid(column=2, row=3)
add_button = Button(text="Add", width=43, command=save)
add_button.grid(column=1, row=4, columnspan=2)

mainloop()
