import tkinter as tk
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from tkinter.messagebox import askyesno
from PIL import ImageTk, Image
import csv


ws = Tk()
ws.title('Bake O\'Clock')
ws.geometry('1350x700+0+0')
ws.config(bg='lightblue')

photo = tk.PhotoImage(file='./images/logo.png')
img = Image.open('./images/logo.png')

ws.iconphoto(True, photo)


canvas= Canvas(ws, width= 65, height= 65,bg="lightblue")
canvas.place(x=50, y=10)
resized_image= img.resize((50,50), Image.ANTIALIAS)
new_image= ImageTk.PhotoImage(resized_image)

#Add image to the Canvas Items
canvas.create_image(10,10, anchor=NW ,image=new_image)
title = Label(ws, text="BAKE O'CLOCK", fg="red",font=("Arial",10,'bold'),bg="lightblue")
title.place(x=32,y=80)

file= open("csvs/LOGIN FORM.csv")
csvreader = csv.reader(file)
header = next(csvreader)

details = []

for row in csvreader:
    details.append(row)

usernames = []
passwords = []

for i in details:
    usernames.append(i[2])
    passwords.append(i[4])
def signin():
    uname = email.get()
    upwd = pasw.get()
    check_counter=0
    if uname == "":
       warn = "Username can't be empty"
    else:
        check_counter += 1
    if upwd == "":
        warn = "Password can't be empty"
    else:
        check_counter += 1
    if check_counter == 2:
        if uname in usernames:
            ind = usernames.index(uname)
            if upwd==passwords[ind]:
                messagebox.showinfo('Login Status', 'Logged in Successfully!')
            else:
                messagebox.showerror('Login Status', 'invalid password')
        
        else:
            messagebox.showerror('Login Status', 'invalid username')
    else:
        messagebox.showerror('', warn)
f = ("Times",14)
left_frame = Frame(
    ws, 
    bd=2, 
    bg='#CCCCCC',   
    relief=SOLID, 
    padx=10, 
    pady=10
    )
left_frame.place(x=500, y=200)
Label(
    left_frame, 
    text="Enter Email", 
    bg='#CCCCCC',
    font=f).grid(row=0, column=0, sticky=W, pady=10)

Label(
    left_frame, 
    text="Enter Password", 
    bg='#CCCCCC',
    font=f
    ).grid(row=1, column=0, pady=0,padx=0)

email = Entry(
    left_frame, 
    font=f
    )
pasw = Entry(
    left_frame, 
    font=f,
    show='*'
    )
login_btn = Button(
    left_frame, 
    width=15, 
    text='Login', 
    font=f, 
    relief=SOLID,
    cursor='hand2',
    command=lambda:signin,
    bg = "blue",
    fg="lightblue"
    )
Label(left_frame, text="OR", bg= '#CCCCCC',
    font=f).grid(row=5, column=1, sticky=W, pady=10)
email.grid(row=0, column=1, pady=10, padx=20)
pasw.grid(row=1, column=1, pady=10, padx=20)
login_btn.grid(row=2, column=0, pady=10, padx=20)
ws.mainloop()
