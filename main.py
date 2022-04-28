import tkinter as tk
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from tkinter.messagebox import askyesno
from PIL import ImageTk, Image
import csv
from tkinter.scrolledtext import ScrolledText
import random

ws = Tk()
ws.title('Bake O\'Clock')
ws.geometry('1350x700+0+0')
ws.config(bg='lightblue')

welcomeframe = Frame(ws, height = 650, width = 1300, bg = "lightblue", relief=RIDGE, bd=5)
loginframe = Frame(ws, height = 650, width = 1300, bg = "lightblue", relief=RIDGE, bd=5)
signupframe = Frame(ws, height = 650, width = 1300, bg = "lightblue", relief=RIDGE, bd=5)
menuframe = Frame(ws, height = 650, width = 1300, bg = "lightblue", relief=RIDGE, bd=5)
cartframe = Frame(ws, height = 650, width = 1300, bg = "lightblue", relief=RIDGE, bd=5)
billframe = Frame(ws, height = 650, width = 1300, bg = "lightblue", relief=RIDGE, bd=5)
#title for welcome page
header = Label(welcomeframe, text="WELCOME TO", fg="black",
                font=("Times New Roman",32,"bold"),
                background="lightblue")
header.place(x=510, y=180) #placing title
#name of bakery
name = Label(welcomeframe, text="BAKE O\'CLOCK", fg="red",
                font=("Times New Roman",52, "bold"),
                background="lightblue",relief="groove")
name.place(x=390,y=250) #placing name
#slogan/motto
motto = Label(welcomeframe, text="WE SERVE YOU", fg="black",
                font=("Times New Roman",12,"italic"),
                background="lightblue")
motto.place(x=610,y=350)

#logo image
img = Image.open('./images/logo.png')

#canvas for logo
canvas= Canvas(welcomeframe, width= 100, height= 100,bg="lightblue")
canvas.place(x=620, y=50)
#resizing image
resized_image= img.resize((90,100), Image.ANTIALIAS)
new_image= ImageTk.PhotoImage(resized_image)
#placing image on canvas
canvas.create_image(10,10, anchor=NW ,image=new_image)
def login():
    import login

def signup():
    import signup
loginbtn = Button(welcomeframe, text="Sign In", font = ("Arial",12), fg="lightblue",
                  command=lambda: login(),height=1,width=7,bg="blue", relief=RIDGE,cursor="hand2")
loginbtn.place(x=630,y=400)
signupbtn = Button(welcomeframe, text="Sign Up", fg="lightblue",
                   command=lambda: signup(),font = ("Arial",12),height=1,width=7,bg="blue", relief=RIDGE,cursor="hand2")
signupbtn.place(x=630,y=450)

#############LOGIN###############


img = Image.open('./images/logo.png')

canvas= Canvas(loginframe, width= 80, height= 80,bg="lightblue")
canvas.grid(sticky="news")
resized_image= img.resize((70,70), Image.ANTIALIAS)
new_image= ImageTk.PhotoImage(resized_image)

#Add image to the Canvas Items
canvas.create_image(10,10, anchor=NW ,image=new_image)
title = Label(loginframe, text="BAKE O'CLOCK", fg="red",font=("Arial",12,'bold'),bg="lightblue")
title.place(x=20,y=100)

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
    loginframe, 
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

#############SIGNUP###############

img = Image.open('./images/logo.png')
canvas= Canvas(signupframe, width= 65, height= 65,bg="lightblue")
canvas.place(x=50, y=10)
resized_image= img.resize((50,50), Image.ANTIALIAS)
new_image= ImageTk.PhotoImage(resized_image)

#Add image to the Canvas Items
canvas.create_image(10,10, anchor=NW ,image=new_image)
title = Label(signupframe, text="BAKE O'CLOCK", fg="red",font=("Arial",10,'bold'),bg="lightblue")
title.place(x=32,y=80)
f = ("Times",14)
right_frame = Frame(
    signupframe, 
    bd=2, 
    bg='#CCCCCC',
    relief=SOLID, 
    padx=10, 
    pady=10
    )

Label(
    right_frame, 
    text="Enter Name", 
    bg='#CCCCCC',
    font=f
    ).grid(row=0, column=0, sticky=W, pady=10)

Label(
    right_frame, 
    text="Enter Email", 
    bg='#CCCCCC',
    font=f
    ).grid(row=1, column=0, sticky=W, pady=10)

Label(
    right_frame, 
    text="Contact Number", 
    bg='#CCCCCC',
    font=f
    ).grid(row=2, column=0, sticky=W, pady=10)


Label(
    right_frame, 
    text="Enter Address", 
    bg='#CCCCCC',
    font=f
    ).grid(row=4, column=0, sticky=W, pady=10)

Label(
    right_frame, 
    text="Enter Password", 
    bg='#CCCCCC',
    font=f
    ).grid(row=5, column=0, sticky=W, pady=10)

Label(
    right_frame, 
    text="Re-Enter Password", 
    bg='#CCCCCC',
    font=f
    ).grid(row=6, column=0, sticky=W, pady=10)


register_name = Entry(
    right_frame, 
    font=f
    )

register_email = Entry(
    right_frame, 
    font=f
    )

register_mobile = Entry(
    right_frame, 
    font=f
    )

register_address = Entry(
    right_frame, 
    font=f
    )


#register_country = OptionMenu(
#    right_frame, 
#    variable, 
#    *countries)
"""
register_country.config(
    width=15, 
    font=('Times', 12)
)
"""
register_pwd = Entry(
    right_frame, 
    font=f,
    show='*'
)
pwd_again = Entry(
    right_frame, 
    font=f,
    show='*'
)

register_btn = Button(
    right_frame, 
    width=15, 
    text='Register', 
    font=f, 
    relief=SOLID,
    cursor='hand2',
)
register_name.grid(row=0, column=1, pady=10, padx=20)
register_email.grid(row=1, column=1, pady=10, padx=20) 
register_mobile.grid(row=2, column=1, pady=10, padx=20)
register_address.grid(row=4, column=1, pady=10, padx=20)
register_pwd.grid(row=5, column=1, pady=10, padx=20)
pwd_again.grid(row=6, column=1, pady=10, padx=20)
register_btn.grid(row=7, column=1, pady=10, padx=20)
right_frame.place(x=500, y=50)

def insert():
    
    check_counter=0
    warn = ""
    if register_name.get() == "":
        warn = "Name can't be empty"
    else:
        check_counter += 1
        
    if register_email.get() == "":
        warn = "Email can't be empty"
    else:
        check_counter += 1

    if register_mobile.get() == "":
        warn = "Contact can't be empty"
    else:
        check_counter += 1

    if variable.get() == "":
        warn = "Address can't be empty"
    else:
        check_counter += 1

    if register_pwd.get() == "":
        warn = "Password can't be empty"
    else:
        check_counter += 1

    if pwd_again.get() == "":
        warn = "Re-enter password can't be empty"
    else:
        check_counter += 1

    if register_pwd.get() != pwd_again.get():
        warn = "Passwords didn't match!"
    else:
        check_counter += 1
    if check_counter==6:
        file = open("csvs/LOGIN FORM.csv",'w')
        writer = csv.writer(f)
        if register_pwd==pwd_again:
            row = [register_name,register_mobile,register_email,register_address,register_pwd]
            writer.writerow(row)
            f.close()
        messagebox.showinfo('confirmation', 'Record Saved')
#############MENU################

img = Image.open('./images/logo.png')

canvas= Canvas(menuframe, width= 65, height= 65,bg="lightblue")
canvas.place(x=50, y=10)
resized_image= img.resize((50,50), Image.ANTIALIAS)
new_image= ImageTk.PhotoImage(resized_image)

#Add image to the Canvas Items
canvas.create_image(10,10, anchor=NW ,image=new_image)
title = Label(menuframe, text="BAKE O'CLOCK", fg="red",font=("Arial",10,'bold'),bg="lightblue")
title.place(x=32,y=80)



file = open("csvs/MENU.csv")
csvreader = csv.reader(file)
header = next(csvreader)
menu = {"CAKES":[],"BROWNIES":[],"CUPCAKES":[],"COOKIES":[],"SAVOURIES":[],"BREADS":[]}
for row in csvreader:
    menu[row[0]].append(row[1:])
    
cat = Label(menuframe, text="MENU", fg="black",font=("Times",32,'bold'),bg="lightblue")
cat.place(x=575,y=30)

frame = Frame(menuframe, height="500", width="1200",bg="lightblue",relief="ridge",bd=2)
frame.place(x=50,y=100)
ck = Image.open('./images/cake.png')
resized= ck.resize((50,50), Image.ANTIALIAS)
new= ImageTk.PhotoImage(resized)

cake = Label(frame,text="CAKES", foreground="pink",background="blue",
             borderwidth=2, justify=tk.CENTER,width=350, font=("Times",22,"bold"),
             relief="ridge",image=new,compound="right")
cake.place(x=20,y=10)
text = ScrolledText(frame, width=42, height=10)
text.place(x=20,y=70)
text.insert("end", "\n")

for i in menu["CAKES"]:
    var = IntVar()
    var.set(0)
    
    checkbutton = Checkbutton(text, text=i[0]+"\tRs. "+i[1], variable=var,cursor="arrow",
                              bg='pink', fg='black',height=2,anchor='w',font=("Arial",12),padx=20)
    text.window_create("end", window=checkbutton)
    text.insert("end", "\n\n")
    i[2]=var.get()
text['state']='disabled'

br = Image.open('./images/brownie.png')
resized= br.resize((50,50), Image.ANTIALIAS)
new1= ImageTk.PhotoImage(resized)
brownie = Label(frame,text="BROWNIES", foreground="pink",
                background="blue", borderwidth=2, justify=tk.CENTER,width=350,
                font=("Times",22,"bold"), relief="ridge",image=new1,compound="right")
brownie.place(x=420,y=10)
text = ScrolledText(frame, width=42, height=10,bd=2)
text.place(x=420,y=70)
text.insert("end", "\n")

for i in menu["BROWNIES"]:
    var = IntVar()
    var.set(0)
    
    checkbutton = Checkbutton(text, text=i[0]+"\tRs. "+i[1], variable=var,cursor="arrow",
                              bg='pink', fg='black',height=2,anchor='w',font=("Arial",12),padx=20)
    text.window_create("end", window=checkbutton)
    text.insert("end", "\n\n")
    i[2]=var.get()
# disable the widget so users can't insert text into it
text['state']='disabled'

cup = Image.open('./images/cupcake.png')
resized= cup.resize((50,50), Image.ANTIALIAS)
new2= ImageTk.PhotoImage(resized)
brownie = Label(frame,text="CUPCAKES", foreground="pink",background="blue",
                borderwidth=2, justify=tk.CENTER,width=350, font=("Times",22,"bold"),
                relief="ridge",image=new2,compound="right")
brownie.place(x=820,y=10)
text = ScrolledText(frame, width=42, height=10)
text.place(x=820,y=70)
text.insert("end", "\n")

for i in menu["CUPCAKES"]:
    var = IntVar()
    var.set(0)
    
    checkbutton = Checkbutton(text, text=i[0]+"\tRs. "+i[1], variable=var,cursor="arrow",
                              bg='pink', fg='black',height=2,anchor='w',font=("Arial",12),padx=20)
    text.window_create("end", window=checkbutton)
    text.insert("end", "\n\n")
    i[2]=var.get()
# disable the widget so users can't insert text into it
text['state']='disabled'

coo = Image.open('./images/cookies.png')
resized= coo.resize((50,50), Image.ANTIALIAS)
new3= ImageTk.PhotoImage(resized)
brownie = Label(frame,text="COOKIES", foreground="pink",background="blue",
                borderwidth=2, justify=tk.CENTER,width=350, font=("Times",22,"bold"),
                relief="ridge",image=new3,compound="right")
brownie.place(x=20,y=260)
text = ScrolledText(frame, width=42, height=10)
text.place(x=20,y=320)
text.insert("end", "\n")

for i in menu["COOKIES"]:
    var = IntVar()
    var.set(0)
    
    checkbutton = Checkbutton(text, text=i[0]+"\tRs. "+i[1],
                              variable=var,cursor="arrow",bg='pink', fg='black',
                              height=2,anchor='w',font=("Arial",12),padx=20)
    text.window_create("end", window=checkbutton)
    text.insert("end", "\n\n")
    i[2]=var.get()
# disable the widget so users can't insert text into it
text['state']='disabled'

sav = Image.open('./images/pastry.png')
resized= sav.resize((50,50), Image.ANTIALIAS)
new4= ImageTk.PhotoImage(resized)
brownie = Label(frame,text="SAVOURIES", foreground="pink",background="blue",
                borderwidth=2, justify=tk.CENTER,width=350, font=("Times",22,"bold"),
                relief="ridge",image=new4,compound="right")
brownie.place(x=420,y=260)
text = ScrolledText(frame, width=42, height=10)
text.place(x=420,y=320)
text.insert("end", "\n")

for i in menu["SAVOURIES"]:
    var = IntVar()
    var.set(0)
    
    checkbutton = Checkbutton(text, text=i[0]+"\tRs. "+i[1],
                              variable=var,cursor="arrow",bg='pink', fg='black',
                              height=2,anchor='w',font=("Arial",12),padx=20)
    text.window_create("end", window=checkbutton)
    text.insert("end", "\n\n")
    i[2]=var.get()
# disable the widget so users can't insert text into it
text['state']='disabled'

brd = Image.open('./images/bread.png')
resized= brd.resize((50,50), Image.ANTIALIAS)
new5= ImageTk.PhotoImage(resized)
brownie = Label(frame,text="BREADS", foreground="pink",
                background="blue", borderwidth=2, justify=tk.CENTER,width=350,
                font=("Times",22,"bold"), relief="ridge",image=new5,compound="right")
brownie.place(x=820,y=260)
text = ScrolledText(frame, width=42, height=10)
text.place(x=820,y=320)
text.insert("end", "\n")

for i in menu["BREADS"]:
    var = IntVar()
    var.set(0)
    
    checkbutton = Checkbutton(text, text=i[0]+"\tRs. "+i[1], variable=var,cursor="arrow",
                              bg='pink', fg='black',height=2,anchor='w',font=("Arial",12),padx=20)
    text.window_create("end", window=checkbutton)
    text.insert("end", "\n\n")
    i[2]=var.get()
# disable the widget so users can't insert text into it
text['state']='disabled'
def checkout():
    bill = []
    for i in menu.keys():
        for j in menu[i]:
            if j[2]>0:
                temp = [j[0],j[1],j[2], int(j[1]*int(j[2]))]
                bill.append(temp)
    
    return bill
bill = checkout()
checkout = Button(menuframe, text="CHECKOUT", font = ("Arial",12, "bold"),
                  fg="pink",command=lambda: checkout(),height=2,width=10,bg="red",
                  relief=RIDGE,cursor="hand2")



title= Label(cartframe, text="CHECKOUT", fg="black",font=("Times",32,'bold'),bg="lightblue")
title.place(x=520,y=30) 

text = ScrolledText(cartframe, width=42, height=20)
text.place(x=470,y=150)
for i in bill:
    lbl = Label(text, text=str(i[0])+"\t"+str(i[1])+"\t"+str(i[2])+"\t"+str(i[3]))
    text.window_create("end", window=lbl)
    text.insert("end", "\n")
    
checkout.place(x=1140, y=40)
menuframe.place(x=25,y=25)
ws.mainloop()
