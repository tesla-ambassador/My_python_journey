from tkinter import *
from tkinter import messagebox
from random import randint, choice, shuffle
import pyperclip
import json

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def gen_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]

    password_list = password_letters + password_numbers + password_symbols

    shuffle(password_list)

    password = ('').join(password_list)
    password_entry.insert(0, password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_data():
    saved_website = website_input.get()
    saved_email = email_input.get()
    saved_password = password_entry.get()
    
    new_data = {
        saved_website: {
            "email": saved_email,
            "password": saved_password
        }
    }
    
    if len(saved_website) == 0 or len(saved_email) == 0 or len(saved_password )== 0:
        messagebox.showinfo(message="Hey!\nYou can't have empty fields")
    else:
        try:
            with open(file='password_manager/data.json', mode='r') as file:
                data = json.load(file)
                data.update(new_data)
                
        except FileNotFoundError:
            with open(file='password_manager/data.json', mode='w') as file:
                json.dump(new_data, file, indent=4)
                
        else:
            with open(file='password_manager/data.json', mode='w') as file:
                json.dump(data, file, indent=4)
            
        website_input.delete(0, END)
        password_entry.delete(0, END)
        

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title('Password Generator')
window.config(padx=20, pady=20, bg='white')

logo = PhotoImage(file='password_manager/logo.png')
canvas = Canvas(width=200, height=200, bg='white', highlightthickness=0)
canvas.create_image(100, 100, image=logo)
canvas.grid(column=2, row=2)

# Website label and entry
website_label = Label(text='Webiste:', bg='white', fg='black', font=('Arial', 18))
website_label.grid(column=1, row=3)

website_input = Entry(width=38, bg='white', fg='black', highlightthickness=0)
website_input.grid(column=2, row=3, columnspan=2)

# email label and entry
email_label = Label(text='Email/Username: ', bg='white', fg='black', font=('Arial', 18))
email_label.grid(column=1, row=4)

email_input = Entry(width=38, bg='white', fg='black', highlightthickness=0)
email_input.insert(0, 'kevindan641@gmail.com')
email_input.grid(column=2, row=4, columnspan=2)

# Password label and entry
password_label = Label(text='Password: ', bg='white', fg='black', font=('Arial', 18))
password_label.grid(column=1, row=5)

password_entry = Entry(bg='white', fg='black', highlightthickness=0, width=21)
password_entry.grid(column=2, row=5)

# Generate password button
gen_password_button = Button(text='Generate Password', highlightthickness=0, highlightbackground='white', command=gen_password)
gen_password_button.grid(column=3, row=5)

# Add button
add_btn = Button(text='Add', width=36, borderwidth=1, highlightbackground='white', command=save_data)
add_btn.grid(column=2, row=6, columnspan=2)


window.mainloop()