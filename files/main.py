from tkinter import *
from tkinter import messagebox
import random as rd
import json

# from requests import JSONDecodeError
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

def gen_pass():
    nr_letters = rd.randint(8,10)
    nr_symbols = rd.randint(2,4)
    nr_numbers = rd.randint(2,4)
    letter_passward = [rd.choice(letters) for i in range(0,nr_letters)]
    symbol_passward = [rd.choice(symbols) for i in range(0,nr_symbols)]
    number_passward = [rd.choice(numbers) for i in range(0,nr_numbers)]

    passward = letter_passward+symbol_passward+number_passward
    rd.shuffle(passward)
    rdpassw = "".join(passward)
    pass_entry.delete(0,END)
    pass_entry.insert(0,rdpassw)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def add():
    web = web_entry.get().title()
    uname = name_entry.get()
    passw = pass_entry.get()

    new_item = {web: {
        "Email": uname,
        "Password": passw
    }}
    if len(web)!=0 and len(uname)!=0 and len(passw)!=0:
        sure = messagebox.askyesno(title=web,message=(f"Are You Sure?\nEmail/Username: {uname}\n Password: {passw}"))
        if sure == True:
            web_entry.delete(0,END)
            name_entry.delete(0,END)
            pass_entry.delete(0,END)
            web_entry.focus()


            try:
                with open("data.json","r") as file:
                    data = json.load(file)
            except FileNotFoundError or json.decoder.JSONDecodeError:
                with open("data.json","w") as dt:
                    json.dump(new_item,dt, indent=4)
            except json.decoder.JSONDecodeError:
                with open("data.json","w") as dt:
                    json.dump(new_item,dt, indent=4)
            else:
                data.update(new_item)
                with open("data.json","w") as dt:
                    json.dump(data,dt, indent=4)
    else:
        messagebox.showwarning(title="Blanks", message="Please don't leave any field blank.")


#---------Search Password-----------#

def search_pass():
    search_bu.config(bg="blue")
    web = web_entry.get().title()
    try:
        with open("data.json") as saved:
            data = json.load(saved)
    
    except FileNotFoundError:
        messagebox.showinfo(title=web,message="There are no saved passwords.")

    else:
        if web in data:
            username = data[web]["Email"]
            password = data[web]["Password"]
            messagebox.showinfo(title=web,message=f"Email/Username: {username}\nPassword: {password}")
        else:
            messagebox.showinfo(title=web,message=f"There is no data associated with {web}.")
            
    search_bu.config(bg="white")
# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Passwork Manager")
window.config(padx=50,pady=50)


canvas = Canvas(height=200,width=200)
img = PhotoImage(file="logo.png")
canvas.create_image(100,100,image=img)
canvas.grid(row=0,column=1)

web_text = Label(text="Website",font=("Comic Sans MS", 10, "italic"))
web_text.grid(row=1,column=0)


web_entry = Entry(width=32)
web_entry.focus()
web_entry.grid(row=1,column=1)

search_bu = Button(text="Search",width=14,command=search_pass)
search_bu.grid(row=1,column=2)

name_text = Label(text="Email/Username",font=("Comic Sans MS", 10, "italic"))
name_text.grid(row=2,column=0)


name_entry = Entry(width=50)
name_entry.grid(row=2,column=1,columnspan=2)

pass_text = Label(text="Password",font=("Comic Sans MS", 10, "italic"))
pass_text.grid(row=3,column=0)


pass_entry = Entry(width=32)
pass_entry.grid(row=3,column=1)



gen_pass_bu = Button(text="Generate Password",width=14,command=gen_pass)
gen_pass_bu.grid(row=3,column=2)

add_bu = Button(text="Add",width=36,command=add)
add_bu.grid(row=4,column=1,columnspan=2)


window.mainloop()