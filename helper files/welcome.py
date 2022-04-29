import tkinter as tk
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from tkinter.messagebox import askyesno
from PIL import ImageTk, Image


ws = Tk()
ws.title('Bake O\'Clock')
ws.geometry('1350x700+0+0')
ws.config(bg='lightblue')

header = Label(ws, text="WELCOME TO", fg="black",
               font=("Times New Roman",32,"bold"),
               background="lightblue")
header.place(x=510, y=180)
name = Label(ws, text="BAKE O\'CLOCK", fg="red",
               font=("Times New Roman",52, "bold"),
               background="lightblue",relief="groove")
name.place(x=390,y=250)
motto = Label(ws, text="WE SERVE YOU", fg="black",
               font=("Times New Roman",12,"italic"),
               background="lightblue")
motto.place(x=610,y=350)

photo = tk.PhotoImage(file='./images/logo.png')
img = Image.open('./images/logo.png')

ws.iconphoto(True, photo)

canvas= Canvas(ws, width= 100, height= 100,bg="lightblue")
canvas.place(x=620, y=50)

resized_image= img.resize((90,100), Image.ANTIALIAS)
new_image= ImageTk.PhotoImage(resized_image)
canvas.create_image(10,10, anchor=NW ,image=new_image)
def login():
    import login

def signup():
    import signup
loginbtn = Button(ws, text="Sign In", font = ("Arial",12), fg="lightblue",command=lambda: login(),height=1,width=7,bg="blue", relief=RIDGE,cursor="hand2")
loginbtn.place(x=630,y=400)
signupbtn = Button(ws, text="Sign Up", fg="lightblue",command=lambda: signup(),font = ("Arial",12),height=1,width=7,bg="blue", relief=RIDGE,cursor="hand2")
signupbtn.place(x=630,y=450)
ws.mainloop()
