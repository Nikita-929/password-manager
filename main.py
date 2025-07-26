from tkinter import *
from tkinter import messagebox
from random import choice,shuffle, randint
import pyperclip
import json




# ---------------------------- PASSWORD GENERATOR ------------------------------- #
#Password Generator Project
def generate_password():

    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_list=[choice(letters) for _ in range(randint(8, 10))]
    password_list+=[choice(symbols) for _ in range(randint(2, 4))]
    password_list+=[choice(numbers) for _ in range(randint(2, 4))]

    shuffle(password_list)

    password="".join(password_list)
    password_entry.insert(0,password)

    pyperclip.copy(password)

# print(f"Your password is: {password}")
# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website=website_entry.get()
    email=email_entry.get()
    password=password_entry.get()
    new_data = {
        website:{
            "email": email,
            "password": password
        }
    }
    if len(website)==0 or len(password)==0:
        messagebox.showinfo(title="Oops!",message="Please do not leave any of the fields empty.")
    else:
        try:
            with open("data.json", mode="r") as data_file:
                # Reading old data
                data = json.load(data_file)
        except FileNotFoundError:
            with open("data.json", mode="w") as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
            #Updating old data with new data
            data.update(new_data)
            with open("data.json",mode="w") as data_file:
                #writing updated data to the file
                json.dump(data, data_file, indent=4)
        finally:
            website_entry.delete(0, END)
            password_entry.delete(0,END)

#---------------------------- FIND PASSWORD -------------------------------#
def find_password():
    website=website_entry.get()
    try:
        with open("data.json", mode="r") as data_file:
            data = json.load(data_file)
            email = data[website]["email"]
            password = data[website]["password"]
    except FileNotFoundError:
         messagebox.showinfo(title="Error",message="No Data File Found")
    except KeyError:
        messagebox.showinfo(title="Error", message="No details for the website exists.")
    else:
        messagebox.showinfo(title=website, message=f"Email: {email}\nPassword: {password}")
# ---------------------------- UI SETUP ------------------------------- #
window=Tk()
window.title("Password Manager")
window.config(padx=50,pady=50)
logo_img=PhotoImage(file="logo.png")
print(logo_img)
canvas = Canvas(width=200,height=200)
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0,column=1)
website_label=Label(text="Website:")
website_label.grid(row=1,column=0)

website_entry=Entry(width=35)
website_entry.focus()
website_entry.grid(row=1,column=1,columnspan=2,sticky="w")



email_label=Label(text="Email/Username:")
email_label.grid(row=2, column=0)

email_entry=Entry(width=35)
email_entry.insert(0,"mahatonikita00@gmail.com")
email_entry.grid(row=2,column=1,columnspan=2,sticky="w")

password_label=Label(text="Password")
password_label.grid(row=3,column=0)
password_entry=Entry(width=21)
password_entry.grid(row=3,column=1,sticky="w")

#Buttons
search_button = Button(text="Search",width=11,command=find_password)
search_button.grid(row = 1, column = 2)
generate_password_button=Button(text="Generate Password", command=generate_password)
generate_password_button.grid(row=3,column=2,sticky="w")
add_button=Button(text="Add", width=36, command=save)
add_button.grid(row=4,column=1,columnspan=2,sticky="w")

window.mainloop()