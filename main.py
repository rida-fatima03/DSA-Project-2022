"""
DSA PROJECT
ONLINE BAKERY
MUMINAH KHURRAM
RIDA FATIMA
BATOOL ZEHRA
"""

#Tkinter is a Python interface for the Tk GUI toolkit.
#The tkinter package ("Tk interface") comprises the Python standard interface to the Tcl/Tk GUI toolkit.
import tkinter as tk
from tkinter import *
from tkinter import messagebox

#The tkinter.ttk module allows users to access the Tk themed widget collection.
from tkinter import ttk

#askyesno is a function that displays a dialogue asking for user confirmation. There will be a title, a message, and two buttons in the dialogue (yes and no). 
#The function returns True when you click the Yes button.
from tkinter.messagebox import askyesno

from PIL import ImageTk, Image
import csv

#scrolledtext is a Python package that provides a text widget as well as a scroll bar.
from tkinter.scrolledtext import ScrolledText

import random
import math

#creating tkinter window
window = Tk()

#window title
window.title('Bake O\'Clock')

#window size
window.geometry('1350x700+0+0')

#window background colour
window.config(bg='lightblue')

#window icon
photo = tk.PhotoImage(file='./images/logo.png')
window.iconphoto(True, photo)


#welcome page frame
welcomeframe = Frame(window, height = 650, width = 1300, bg = "lightblue", relief=RIDGE, bd=5)

#login/signin page frame
loginframe = Frame(window, height = 650, width = 1300, bg = "lightblue", relief=RIDGE, bd=5)

#signup page frame
signupframe = Frame(window, height = 650, width = 1300, bg = "lightblue", relief=RIDGE, bd=5)

#menu page frame
menuframe = Frame(window, height = 650, width = 1300, bg = "lightblue", relief=RIDGE, bd=5)

#cart/checkout page frame
cartframe = Frame(window, height = 650, width = 1300, bg = "lightblue", relief=RIDGE, bd=5)

#final bill page frame
billframe = Frame(window, height = 650, width = 1300, bg = "lightblue", relief=RIDGE, bd=5)

#############WELCOME################

#header for welcome page
header = Label(welcomeframe, text="WELCOME TO", fg="black",
                font=("Times New Roman",32,"bold"),
                background="lightblue")
#title placement
header.place(x=470, y=180)
#The next few lines of code are for stating the bakery's name.
name = Label(welcomeframe, text="BAKE O\'CLOCK", fg="red",
                font=("Times New Roman",52, "bold"),
                background="lightblue",relief="groove")
name.place(x=360,y=250) #placing name
#The next few lines of code are for mentioning the bakery's primary motto.
motto = Label(welcomeframe, text="WE SERVE YOU", fg="black",
                font=("Times New Roman",12,"italic"),
                background="lightblue")
motto.place(x=570,y=350)

#logo image
img1 = Image.open('./images/logo.png')

#canvas for logo
canvas= Canvas(welcomeframe, width= 100, height= 100,bg="lightblue")
canvas.place(x=575, y=50)
#The next few lines of code are for image scaling.
resized_image1= img1.resize((90,100), Image.ANTIALIAS)
new_image1= ImageTk.PhotoImage(resized_image1)
#The next lines of code are for displaying an image on canvas.
canvas.create_image(10,10, anchor=NW ,image=new_image1)

orderbtn = Button(welcomeframe, text="ORDER NOW", font = ("Arial",12,"bold"), fg="white",
                  command=lambda: loginframe.place(x=25,y=25),height=2,width=10,bg="red", relief=RIDGE,cursor="hand2")
orderbtn.place(x=570,y=400)

#############LOGIN###############


import sqlite3




con = sqlite3.connect('userdata.db')
cur = con.cursor()
cur.execute('''CREATE TABLE IF NOT EXISTS record(
                    name text, 
                    email text, 
                    contact number,  
                    address text,
                    area text,
                    password text
                )
            ''')
con.commit()


canvas2= Canvas(loginframe, width= 80, height= 80,bg="lightblue")
canvas2.place(x=585,y=10)
resized_image2= img1.resize((70,70), Image.ANTIALIAS)
new_image2= ImageTk.PhotoImage(resized_image2)

#Insert an image into the Canvas Items
canvas2.create_image(10,10, anchor=NW ,image=new_image2)
title1 = Label(loginframe, text="BAKE O'CLOCK", fg="red",font=("Arial",12,'bold'),bg="lightblue")
title1.place(x=565,y=100)




def signin():
    try:
        con = sqlite3.connect('userdata.db')
        c = con.cursor()
        for row in c.execute("Select * from record"):
            uname = row[1]
            pwd = row[5]
        
    except Exception as ep:
        messagebox.showerror('', ep)

    username = email.get()
    password = pasw.get()
    check_counter=0
    if username == "":
        warn = "Please enter your username"
    else:
        check_counter += 1
    if password == "":
        warn = "Please enter your password"
    else:
        check_counter += 1
    if check_counter == 0:
        warn = "Please enter your username and password "
    if check_counter == 2:
        if (uname == username and password == pwd):
            messagebox.showinfo('Login Status', 'Logged in Successfully!')
        
        else:
            messagebox.showerror('Login Status', 'invalid username or password')
    else:
        messagebox.showerror('', warn)
    file.close()
f = ("Times",14)
login = Frame(
    loginframe, 
    bd=2, 
    bg='#CCCCCC',   
    relief=SOLID, 
    padx=10, 
    pady=10
    )
login.place(x=420, y=200)
Label(
    login, 
    text="Enter Email", 
    bg='#CCCCCC',
    font=f).grid(row=0, column=0, sticky=W, pady=10)

Label(
    login, 
    text="Enter Password", 
    bg='#CCCCCC',
    font=f
    ).grid(row=1, column=0, pady=0,padx=0, sticky=W)

email = Entry(
    login, 
    font=f
    )
pasw = Entry(
    login, 
    font=f,
    show='*'
    )
login_btn = Button(
    login, 
    width=15, 
    text='Sign In', 
    font=("Times",14,"bold"), 
    relief=SOLID,
    cursor='hand2',
    command=lambda:[signin(),menuframe.place(x=25,y=25)],
    bg = "blue",
    fg="white"
    )

Label(login, text="Don't Have an Account?", bg= '#CCCCCC',
    font=f).grid(row=5, column=0, pady=10)
signup_btn = Button(
    login, 
    width=15, 
    text='Sign Up', 
    font=("Times",14,"bold"), 
    relief=SOLID,
    cursor='hand2',
    command=lambda:signupframe.place(x=25,y=25),
    bg = "blue",
    fg="white"
    )
email.grid(row=0, column=1, pady=10, padx=20)
pasw.grid(row=1, column=1, pady=10, padx=20)
login_btn.grid(row=3, column=1, pady=10, padx=20)
signup_btn.grid(row=6, column=1, pady=10, padx=20)
#############SIGNUP###############

img3 = Image.open('./images/logo.png')
canvas3= Canvas(signupframe, width= 80, height= 80,bg="lightblue")
canvas3.place(x=585, y=10)
resized_image3= img3.resize((70,70), Image.ANTIALIAS)
new_image3= ImageTk.PhotoImage(resized_image3)

#Insert an image into the Canvas Items
canvas3.create_image(10,10, anchor=NW ,image=new_image3)
title3 = Label(signupframe, text="BAKE O'CLOCK", fg="red",font=("Arial",12,'bold'),bg="lightblue")
title3.place(x=565,y=100)
f = ("Times",14)
signup = Frame(
    signupframe, 
    bd=2, 
    bg='#CCCCCC',
    relief=SOLID, 
    padx=10, 
    pady=10
    )

Label(
    signup, 
    text="Enter Name*", 
    bg='#CCCCCC',
    font=f
    ).grid(row=0, column=0, sticky=W, pady=10)

Label(
    signup, 
    text="Enter Email*", 
    bg='#CCCCCC',
    font=f
    ).grid(row=1, column=0, sticky=W, pady=10)

Label(
    signup, 
    text="Contact Number*", 
    bg='#CCCCCC',
    font=f
    ).grid(row=2, column=0, sticky=W, pady=10)


Label(
    signup, 
    text="Enter Address*", 
    bg='#CCCCCC',
    font=f
    ).grid(row=3, column=0, sticky=W, pady=10)

Label(
    signup, 
    text="Choose Area*", 
    bg='#CCCCCC',
    font=f
    ).grid(row=4, column=0, sticky=W, pady=10)

Label(
    signup, 
    text="Enter Password*", 
    bg='#CCCCCC',
    font=f
    ).grid(row=5, column=0, sticky=W, pady=10)

Label(
    signup, 
    text="Re-Enter Password*", 
    bg='#CCCCCC',
    font=f
    ).grid(row=6, column=0, sticky=W, pady=10)


register_name = Entry(
    signup, 
    font=f
    )

register_email = Entry(
    signup, 
    font=f
    )

register_mobile = Entry(
    signup, 
    font=f
    )

register_address = Entry(
    signup, 
    font=f
    )

variable = StringVar()
areas = [ 'AIRPORT', 'ANCHOLI', 'CHAMAN IQBAL COLONY', 'DALMIA','GULISTAN E JAUHAR', 'GULSHAN E IQBAL', 'MODEL COLONY','MALIR CANT', 'SHAH FAISAL TOWN', 'KARSAZ']
register_area = OptionMenu(
    signup, 
    variable, 
    *areas)

register_area.config(
    width=15, 
    font=('Times', 12)
)

register_pwd = Entry(
    signup, 
    font=f,
    show='*'
)
pwd_again = Entry(
    signup, 
    font=f,
    show='*'
)

def insert():
    
    check_counter=0
    warn = ""
    if register_name.get() == "":
        warn = "Please enter your name"
    else:
        check_counter += 1
        
    if register_email.get() == "":
        warn = "Please enter your email"
    else:
        check_counter += 1

    if register_mobile.get() == "":
        warn = "Please enter your contact "
    else:
        check_counter += 1
    if register_address.get() == "":
        warn = "Please enter your address"
    else:
        check_counter += 1

    if variable.get() == "":
        warn = "Please enter your address"
    else:
        check_counter += 1

    if register_pwd.get() == "":
        warn = "Please enter your password"
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
    if check_counter==8:
        try:
            con = sqlite3.connect('userdata.db')
            cur = con.cursor()
            cur.execute("INSERT INTO record VALUES (:name, :email, :contact, :address, :area, :password)", {
                            'name': register_name.get(),
                            'email': register_email.get(),
                            'contact': register_mobile.get(),
                            'address': register_address.get(),
                            'area': variable.get(),
                            'password': register_pwd.get()

            })
            con.commit()
            messagebox.showinfo('Confirmation', 'Record Saved\nClick OK to proceed with your order')

        except Exception as ep:
            messagebox.showerror('', ep) 
    else:
        messagebox.showerror('Error', warn)

register_btn = Button(
    signup, 
    width=15, 
    text='Register', 
    font=f, 
    relief=SOLID,
    cursor='hand2', command = lambda:[insert(),menuframe.place(x=25,y=25)])
register_name.grid(row=0, column=1, pady=10, padx=20)
register_email.grid(row=1, column=1, pady=10, padx=20) 
register_mobile.grid(row=2, column=1, pady=10, padx=20)
register_address.grid(row=3, column=1, pady=10, padx=20)
register_area.grid(row=4, column=1, pady=10, padx=20)
register_pwd.grid(row=5, column=1, pady=10, padx=20)
pwd_again.grid(row=6, column=1, pady=10, padx=20)
register_btn.grid(row=7, column=1, pady=10, padx=20)
signup.place(x=430, y=170)


#############MENU################

img4 = Image.open('./images/logo.png')

canvas4= Canvas(menuframe, width= 65, height= 65,bg="lightblue")
canvas4.place(x=50, y=10)
resized_image4= img4.resize((50,50), Image.ANTIALIAS)
new_image4= ImageTk.PhotoImage(resized_image4)

#Insert an image into the Canvas Items
canvas4.create_image(10,10, anchor=NW ,image=new_image4)
title4 = Label(menuframe, text="BAKE O'CLOCK", fg="red",font=("Arial",10,'bold'),bg="lightblue")
title4.place(x=32,y=80)



file = open("csvs/MENU.csv")
csvreader = csv.reader(file)
header = next(csvreader)
menu = {"CAKES":[],"BROWNIES":[],"CUPCAKES":[],"COOKIES":[],"SAVOURIES":[],"BREADS":[]}
for row in csvreader:
    menu[row[0]].append(row[1:])
    
title4 = Label(menuframe, text="MENU", fg="black",font=("Times",32,'bold'),bg="lightblue")
title4.place(x=575,y=30)

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
    
    
    checkbutton = Checkbutton(text, text=i[0]+"\tRs. "+i[1], variable=var,cursor="arrow",
                              bg='pink', fg='black',height=2,anchor='w',font=("Arial",12),padx=20)
    text.window_create("end", window=checkbutton)
    text.insert("end", "\n\n")
    if var.get()>0:
        i[2]=1
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
    
    
    checkbutton = Checkbutton(text, text=i[0]+"\tRs. "+i[1], variable=var,cursor="arrow",
                              bg='pink', fg='black',height=2,anchor='w',font=("Arial",12),padx=20)
    text.window_create("end", window=checkbutton)
    text.insert("end", "\n\n")
    if var.get()>0:
        i[2]=1
# Make the widget inaccessible to users by preventing them from inserting text into it.
text['state']='disabled'

cup = Image.open('./images/cupcake.png')
resized= cup.resize((50,50), Image.ANTIALIAS)
new2= ImageTk.PhotoImage(resized)
cupcake = Label(frame,text="CUPCAKES", foreground="pink",background="blue",
                borderwidth=2, justify=tk.CENTER,width=350, font=("Times",22,"bold"),
                relief="ridge",image=new2,compound="right")
cupcake.place(x=820,y=10)
text = ScrolledText(frame, width=42, height=10)
text.place(x=820,y=70)
text.insert("end", "\n")

for i in menu["CUPCAKES"]:
    var = IntVar()
    
    checkbutton = Checkbutton(text, text=i[0]+"\tRs. "+i[1], variable=var,cursor="arrow",
                              bg='pink', fg='black',height=2,anchor='w',font=("Arial",12),padx=20)
    text.window_create("end", window=checkbutton)
    text.insert("end", "\n\n")
    if var.get()>0:
        i[2]=1
# Make the widget inaccessible to users by preventing them from inserting text into it.
text['state']='disabled'

coo = Image.open('./images/cookies.png')
resized= coo.resize((50,50), Image.ANTIALIAS)
new3= ImageTk.PhotoImage(resized)
cookie = Label(frame,text="COOKIES", foreground="pink",background="blue",
                borderwidth=2, justify=tk.CENTER,width=350, font=("Times",22,"bold"),
                relief="ridge",image=new3,compound="right")
cookie.place(x=20,y=260)
text = ScrolledText(frame, width=42, height=10)
text.place(x=20,y=320)
text.insert("end", "\n")

for i in menu["COOKIES"]:
    var = IntVar()
   
    checkbutton = Checkbutton(text, text=i[0]+"\tRs. "+i[1],
                              variable=var,cursor="arrow",bg='pink', fg='black',
                              height=2,anchor='w',font=("Arial",12),padx=20)
    text.window_create("end", window=checkbutton)
    text.insert("end", "\n\n")
    if var.get()>0:
        i[2]=1
# Make the widget inaccessible to users by preventing them from inserting text into it.
text['state']='disabled'

sav = Image.open('./images/pastry.png')
resized= sav.resize((50,50), Image.ANTIALIAS)
new4= ImageTk.PhotoImage(resized)
savory = Label(frame,text="SAVOURIES", foreground="pink",background="blue",
                borderwidth=2, justify=tk.CENTER,width=350, font=("Times",22,"bold"),
                relief="ridge",image=new4,compound="right")
savory.place(x=420,y=260)
text = ScrolledText(frame, width=42, height=10)
text.place(x=420,y=320)
text.insert("end", "\n")

for i in menu["SAVOURIES"]:
    var = IntVar()
    
    checkbutton = Checkbutton(text, text=i[0]+"\tRs. "+i[1],
                              variable=var,cursor="arrow",bg='pink', fg='black',
                              height=2,anchor='w',font=("Arial",12),padx=20)
    text.window_create("end", window=checkbutton)
    text.insert("end", "\n\n")
    if var.get()>0:
        i[2]=1
# Make the widget inaccessible to users by preventing them from inserting text into it.
text['state']='disabled'

brd = Image.open('./images/bread.png')
resized= brd.resize((50,50), Image.ANTIALIAS)
new5= ImageTk.PhotoImage(resized)
bread = Label(frame,text="BREADS", foreground="pink",
                background="blue", borderwidth=2, justify=tk.CENTER,width=350,
                font=("Times",22,"bold"), relief="ridge",image=new5,compound="right")
bread.place(x=820,y=260)
text = ScrolledText(frame, width=42, height=10)
text.place(x=820,y=320)
text.insert("end", "\n")

for i in menu["BREADS"]:
    var = IntVar()
   
    
    checkbutton = Checkbutton(text, text=i[0]+"\tRs. "+i[1], variable=var,cursor="arrow",
                              bg='pink', fg='black',height=2,anchor='w',font=("Arial",12),padx=20)
    text.window_create("end", window=checkbutton)
    text.insert("end", "\n\n")
    if var.get()>0:
        i[2]=1
# Make the widget inaccessible to users by preventing them from inserting text into it.
text['state']='disabled'
bill=[]
def checkout1():
    print("inside checkout function")
    for i in menu.keys():
        for j in menu[i]:
            if int(j[2])>0:
                temp = [j[0],j[1],j[2],j[1]]
                bill.append(temp)
    
def x():
    print("inside checkout function")

checkout = Button(menuframe, text="PLACE ORDER", font = ("Arial",12, "bold"),fg="pink",height=2,width=10,bg="red",relief=RIDGE,cursor="hand2",command=lambda: [checkout1(),billframe.place(x=25,y=25)])
#[checkout(bill),cartframe.place(x=25,y=25)]
#menuframe.place(x=25,y=25)

title= Label(billframe, text="WE HAVE RECEIVED YOUR ORDER!", fg="black",font=("Times",22,'bold'),bg="lightblue")
title.place(x=520,y=30) 



checkout.place(x=1140, y=40)
img5 = Image.open('./images/logo.png')

canvas5= Canvas(billframe, width= 65, height= 65,bg="lightblue")
canvas5.place(x=50, y=10)
resized_image5= img5.resize((50,50), Image.ANTIALIAS)
new_image5= ImageTk.PhotoImage(resized_image5)

#Insert an image into the Canvas Items
canvas5.create_image(10,10, anchor=NW ,image=new_image4)
title5 = Label(billframe, text="BAKE O'CLOCK", fg="red",font=("Arial",10,'bold'),bg="lightblue")
title5.place(x=32,y=80)


from math import inf
nodes = [ 'AIRPORT', 'ANCHOLI', 'CHAMAN IQBAL COLONY', 'DALMIA','GULISTAN E JAUHAR', 'GULSHAN E IQBAL', 'MODEL COLONY','MALIR CANT', 'SHAH FAISAL TOWN', 'KARSAZ']
edges=[ ("GULISTAN E JAUHAR", "AIRPORT", 7),( 'GULISTAN E JAUHAR', 'ANCHOLI',15),('GULISTAN E JAUHAR', 'CHAMAN IQBAL COLONY',5.4),
        ( 'GULISTAN E JAUHAR', 'DALMIA',9.7),( 'GULISTAN E JAUHAR', 'GULSHAN E IQBAL',11.2),('GULISTAN E JAUHAR', 'MODEL COLONY',13.4),
        ( 'GULISTAN E JAUHAR', 'MALIR CANT',17.5),( 'GULISTAN E JAUHAR', 'SHAH FAISAL TOWN',12.8),( 'GULISTAN E JAUHAR', 'KARSAZ',14.2),
        ('AIRPORT', 'ANCHOLI', 14),('AIRPORT', 'GULSHAN E IQBAL', 13), ('AIRPORT', 'MODEL COLONY', 4),('AIRPORT', 'MALIR CANT', 12),
        ('AIRPORT', 'SHAH FAISAL TOWN', 12),('AIRPORT', 'KARSAZ', 11),('ANCHOLI', 'CHAMAN IQBAL COLONY', 10.2),('ANCHOLI','DALMIA', 8.3),
        ('ANCHOLI', 'GULSHAN E IQBAL', 4.7), ('ANCHOLI', 'MODEL COLONY', 17.2),('ANCHOLI', 'MALIR CANT', 21.1),('ANCHOLI', 'SHAH FAISAL TOWN', 14.2),
        ('ANCHOLI', 'KARSAZ', 6.6),('CHAMAN IQBAL COLONY', 'DALMIA', 7.1),('CHAMAN IQBAL COLONY', 'GULSHAN E IQBAL', 8.3),
        ('CHAMAN IQBAL COLONY', 'MODEL COLONY', 10.5),('CHAMAN IQBAL COLONY', 'MALIR CANT', 12.4),('CHAMAN IQBAL COLONY', 'SHAH FAISAL TOWN', 10),
        ('CHAMAN IQBAL COLONY', 'KARSAZ', 10.7),('DALMIA', 'GULSHAN E IQBAL', 4.7),('DALMIA', 'MODEL COLONY', 11.5),('DALMIA', 'MALIR CANT', 11.5),
        ('DALMIA', 'SHAH FAISAL TOWN', 8.5),('DALMIA', 'KARSAZ' ,5.3),('GULSHAN E IQBAL', 'MODEL COLONY', 12), ('GULSHAN E IQBAL', 'MALIR CANT', 18),
        ('GULSHAN E IQBAL', 'SHAH FAISAL TOWN', 9.5), ('GULSHAN E IQBAL', 'KARSAZ', 6.9), ('MODEL COLONY', 'MALIR CANT', 10),
        ('MODEL COLONY', 'SHAH FAISAL TOWN', 7.4),('MODEL COLONY', 'KARSAZ', 14), ('MALIR CANT', 'SHAH FAISAL TOWN', 18), ('MALIR CANT', 'KARSAZ', 21),
        ('SHAH FAISAL TOWN', 'KARSAZ', 12)]
G = {}
def addNodes(G,nodes):
    for x in nodes:
        G[x]=[]
    return G


def addEdges(G, edges, directed = False):
    
    if directed==True:
        # lst=[]
        for x in edges:
            G[x[0]].append((x[1],x[2]))
            # G[x].extend(x[2])
    elif directed==False:
        for x in edges:
        
            G[x[1]].append((x[0],x[2]))

            G[x[0]].append((x[1],x[2]))
    return G
addNodes(G,nodes)
addEdges(G, edges, False)
def BinarySearch(x, y, lst):
  start=  0
  end =len(lst) - 1
  while  start<=end :
    middle = (start+end) // 2
    c= y[lst[middle]]
    if c == y[x]:
      return middle
    elif c > y[x]:
      end = middle - 1  
    else:
      start = middle + 1
  return end+1
def getShortestPath (graph,initial,final):
    path = {}
    adjacent = {}
    queue = [initial]
    for node in graph:
        path[node] =math.inf
        adjacent[node] = None    
    path[initial] = 0
    while queue:
        new= queue.pop(0)
        for x,y in graph[new]:
            alter = y + path[new]
            if path[x] > alter:
                path[x] = alter
                adjacent[x] = new
                queue.insert(BinarySearch(x, path, queue),x)
    
    a=path[final]
   
    return a
def calcdel():
   
        con = sqlite3.connect('userdata.db')
        c = con.cursor()
        for row in c.execute("Select * from record"):
            are = row[4]
        dis = getShortestPath (G,"GULISTAN E JAUHAR",are)
        if dis>0 and dis<=10:
            fee = 50
        elif dis>10 and dis<=20:
            fee = 100
        elif dis>20:
            fee = 150
        return fee


text = ScrolledText(billframe, width=42, height=20)
text.place(x=470,y=150)
text.insert("end", "\n")
num = random.randint(2763718,9485198908)
text.insert("end", f"Bill Number:{num}\n")
fee = calcdel()
total = 0
for i in bill:
    total+=int(i[3])
if total>5000:
    fee = 0
total1 = fee + total
for i in bill:
    lbl = Label(text, text=str(i[0])+"\t"+str(i[1])+"\t"+str(i[2])+"\t"+str(i[3]))
    text.window_create("end", window=lbl)
    text.insert("end", "\n")
text.insert("end", f"\nTotal:{total}")
text.insert("end", f"\nDelivery fee:{fee}")
text.insert("end", f"\nTotal Price:{total1}")
            
welcomeframe.place(x=25,y=25)
window.mainloop()

