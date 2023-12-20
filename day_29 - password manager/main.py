from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json

# ---------------------------- SEARCH PASSWORD ------------------------------- #
def search():
    website = webside_ent.get()

    if len(website) == 0:
        messagebox.showinfo(title="Something is wrong?", message="Check webside You trying to search")
    else:
        try:
            with open("data.json", "r") as json_data_file:
                # read json data
                data = json.load(json_data_file)
        except FileNotFoundError:
            messagebox.showinfo(title="Error?", message="JSON file missing, check this")
        else:
            if website in data:
                messagebox.showinfo(title=website, message=f"Email: {data[website]['email']}\nPassword: {data[website]['password']}")
            else:
                messagebox.showinfo(title="Something is wrong?", message=f"You do not have password for {website}")


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    pass_ent.delete(0, END)

    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_list = []

    [password_list.append(random.choice(letters)) for char in range(random.randint(8,8))]
    [password_list.append(random.choice(symbols)) for char in range(random.randint(2,2))]
    [password_list.append(random.choice(numbers)) for char in range(random.randint(2,2))]

    random.shuffle(password_list)

    password = "".join(password_list)
    pyperclip.copy(password) # copeing Your password to clipboard
    pass_ent.insert(END, password)
    

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website =webside_ent.get()
    email = email_ent.get()
    password = pass_ent.get()
    new_data = {
        website : {
            "email" : email,
            "password" : password,
        }
    }

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Something is wrong?", message="You left some box(es) empty, please check.")
    else:
        try:
            with open("data.json", "r") as json_data_file:
                # read json data
                data = json.load(json_data_file)
        except FileNotFoundError:
            with open("data.json", "w") as json_data_file:
                # save updated json data
                json.dump(new_data, json_data_file, indent=4)
        else:
            # update json data
            data.update(new_data)

            with open("data.json", "w") as json_data_file:
                # save updated json data
                json.dump(data, json_data_file, indent=4)
        finally:    
            webside_ent.delete(0, END)
            pass_ent.delete(0, END)
            webside_ent.focus()


# ---------------------------- UI SETUP ------------------------------- #
# widow setup ---------------------
window = Tk()
window.title("Password Manager")
window.config(padx=25, pady=25)

# canvas set up - canvcas widget to show tomato image and timer text 
canvas = Canvas(width=200, height=200, highlightthickness=0)
logo_image = PhotoImage(file ="logo.png")
canvas.create_image(100, 100, image=logo_image)
canvas.grid(column=1, row=0)


# labels setup ---------------------
webside_lb = Label( text="Website:")
webside_lb.grid(column=0, row=1)

email_lb = Label( text="Email/Username:")
email_lb.grid(column=0, row=2)

pass_lb = Label( text="Password:")
pass_lb.grid(column=0, row=3)

# buttons setup ---------------------
add = Button(text="Add", width=58, command=save)
add.grid(column=1, row=4, columnspan=2)

gen_pass =  Button(text="Generate Password", width=15, command=generate_password)
gen_pass.grid(column=2, row=3)

search =  Button(text="Search", width=15, command=search)
search.grid(column=2, row=1, columnspan=1)

# entry setup ---------------------
webside_ent = Entry(width=33, font=("consolas"))
webside_ent.grid(column=1, row=1)
webside_ent.focus() # cursor ready in first entry after starting program

email_ent = Entry(width=46, font=("consolas"))
email_ent.grid(column=1, row=2, columnspan=2)
email_ent.insert(END, '@gmail.com')

pass_ent = Entry(width=33, font=("consolas"))
pass_ent.grid(column=1, row=3)

window.mainloop()