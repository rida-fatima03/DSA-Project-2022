import tkinter as tk
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from tkinter.messagebox import askyesno
from PIL import ImageTk, Image
import csv
from tkinter.scrolledtext import ScrolledText


ws = Tk()
ws.title('Bake O\'Clock')
ws.geometry('1350x700+0+0')
ws.config(bg='lightblue')

photo = tk.PhotoImage(file='./images/logo.png')
ws.iconphoto(True, photo)

#############MENU################
img = Image.open('./images/logo.png')

canvas= Canvas(ws, width= 65, height= 65,bg="lightblue")
canvas.place(x=50, y=10)
resized_image= img.resize((50,50), Image.ANTIALIAS)
new_image= ImageTk.PhotoImage(resized_image)

#Add image to the Canvas Items
canvas.create_image(10,10, anchor=NW ,image=new_image)
title = Label(ws, text="BAKE O'CLOCK", fg="red",font=("Arial",10,'bold'),bg="lightblue")
title.place(x=32,y=80)



file = open("csvs/MENU.csv")
csvreader = csv.reader(file)
header = next(csvreader)
menu = {"CAKES":[],"BROWNIES":[],"CUPCAKES":[],"COOKIES":[],"SAVOURIES":[],"BREADS":[]}
for row in csvreader:
    menu[row[0]].append(row[1:])
    
cat = Label(ws, text="MENU", fg="black",font=("Times",32,'bold'),bg="lightblue")
cat.place(x=600,y=30)

frame = Frame(ws, height="550", width="1250",bg="lightblue",relief="ridge",bd=2)
frame.place(x=50,y=100)
ck = Image.open('./images/cake.png')
resized= ck.resize((50,50), Image.ANTIALIAS)
new= ImageTk.PhotoImage(resized)

cake = Label(frame,text="CAKES", foreground="pink",background="blue", borderwidth=2, justify=tk.CENTER,width=350, font=("Times",22,"bold"), relief="ridge",image=new,compound="right")
cake.place(x=10,y=10)
text = ScrolledText(frame, width=42, height=12)
text.place(x=10,y=70)
text.insert("end", "\n")

for i in menu["CAKES"]:
    var = IntVar()
    var.set(0)
    
    checkbutton = Checkbutton(text, text=i[0]+"\tRs."+i[1], variable=var,cursor="arrow",bg='lightblue', fg='black',height=2,anchor='w',font=("Arial",12),padx=20)
    text.window_create("end", window=checkbutton)
    text.insert("end", "\n\n")
    i[2]=var


# disable the widget so users can't insert text into it
text['state']='disabled'


ws.mainloop()
