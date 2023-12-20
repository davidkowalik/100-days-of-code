from tkinter import *
from tkinter import messagebox
import random
import pyperclip

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
def add_password():
    website =webside_ent.get()
    email = email_ent.get()
    password = pass_ent.get()

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Something is wrong?", message="You left some box(es) empty, please check.")
    else:
        is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered: \n\nEmail: {email} \nPassword: {password} \n\nIs it ok to save?")
        
        if is_ok:
            with open("data.txt", "a") as data_file:
                data_file.write(f"{website} | {email} | {password}\n")

            webside_ent.delete(0, END)
            pass_ent.delete(0, END)
            webside_ent.focus()
        else:
            pass

# ---------------------------- UI SETUP ------------------------------- #
# widow setup
window = Tk()
window.title("Password Manager")
window.config(padx=25, pady=25)

# canvas set up - canvcas widget to show tomato image and timer text 
canvas = Canvas(width=200, height=200, highlightthickness=0)
logo_image = PhotoImage(file ="logo.png")
canvas.create_image(100, 100, image=logo_image)
canvas.grid(column=1, row=0)


# labels setup
webside_lb = Label( text="Website:")
webside_lb.grid(column=0, row=1)

email_lb = Label( text="Email/Username:")
email_lb.grid(column=0, row=2)

pass_lb = Label( text="Password:")
pass_lb.grid(column=0, row=3)

# buttons setup
add = Button(text="Add", width=58, command=add_password)
add.grid(column=1, row=4, columnspan=2)

gen_pass =  Button(text="Generate Password", command=generate_password)
gen_pass.grid(column=2, row=3)

# entry setup
webside_ent = Entry(width=46, font=("consolas"))
webside_ent.grid(column=1, row=1, columnspan=2)
webside_ent.focus() # cursor ready in first entry after starting program

email_ent = Entry(width=46, font=("consolas"))
email_ent.grid(column=1, row=2, columnspan=2)
email_ent.insert(END, '@gmail.com')

pass_ent = Entry(width=33, font=("consolas"))
pass_ent.grid(column=1, row=3)

window.mainloop()