from tkinter import *
from PIL import Image, ImageTk
import tkinter as tk
import os
import pymysql as sql
from tkinter import ttk
from tkinter import messagebox

def db_connect():
    conn=sql.connect(host='localhost',port=3306,user='root',password='',database='Event')
    cur=conn.cursor()
    return conn,cur
  
  

def login(): #here we call function on login button who used to save data when we click
    username=Cent.get() # username = we give name "username" to  Cent (entry box) 
    password=Dent.get() # password = we give name "password" to  Dent (entry box) 
    cmd=f"select * from user where username='{username}'" # first we chack username present or not 
    conn,cur=db_connect() # for call function (db_connect ())
    data=cur.execute(cmd) # it used excute sql quary
    if data: # if username data is present then
        cmd=f"select * from user where username= '{Cent.get()}' and password= '{Dent.get()}'"   # if username and password both are present then
        data=cur.execute(cmd)
        if data:
            messagebox.showinfo("login", "Login Sucessfully")  # print it
            win.destroy()                                       # then excute all query
            os.system("python menubar.py")                      # then open menubar page
            
        else:
            messagebox.showwarning("warning","Wrong Password enter valid password")   # if username present but password not present then print it
            
    else:
        messagebox.showwarning("warning","username and password is not exist") # if user name and password both are not present
    

def signup():
    os.system("python Signup.py")
win=Tk()

win.state('zoomed') #output hmesha full screen me open hoga
files1=Image.open("C:\\Users\\HP\\Desktop\\Event managment\\image\\glitter.png")  # used for open image
files2=files1.resize((1300,800)) #for assign size
 
tk_image=ImageTk.PhotoImage(files2) #tk_imagee is a var name and ImageTk.PhotoImage is predefined
 
new_Label=tk.Label(win,image=tk_image) # here is image= is predefined
new_Label.pack() 



B=Label(win,fg="white",bg="black",width=24,height=13,font=("Lucida Calligraphy",22,"bold"))
B.place(x=110,y=90)

A=Label(win,text="LOGIN FORM",fg="white",bg="black",font=("Lucida Calligraphy",24,"bold","underline"))
A.place(x=250,y=130)

C=Label(win,text="USERNAME",fg="white",bg="black",font=("Lucida Calligraphy",18,"bold"))
C.place(x=150,y=230)

Cent=Entry(win,bg="white",width=25,font=("Lucida Calligraphy",18,"bold"))
Cent.place(x=150,y=290)

D=Label(win,text="PASSWORD",fg="white",bg="black",font=("Lucida Calligraphy",18,"bold"))
D.place(x=150,y=340)

Dent=Entry(win,bg="white",width=25,font=("Lucida Calligraphy",18,"bold"))
Dent.place(x=150,y=400)

text=Label(win,text="forgate password ??",fg="white",bg="black",font=("Lucida Calligraphy",9,"bold"))
text.place(x=150,y=450)

Rs=Button(win,text="Reset",width=7,height=1,bg="black",fg="blue",font=("Lucida Calligraphy",13,"bold"),relief="flat")
Rs.place(x=290,y=440)

Lg=Button(win,text="Login",width=7,height=1,font=("Lucida Calligraphy",14,"bold"),command=login )
Lg.place(x=330,y=510)



Sg=Button(win,text="Sign up",width=7,height=1,font=("Lucida Calligraphy",14,"bold"),command=signup )
Sg.place(x=460,y=510)


#B=Label(win,bg="white",bg="black",width=24,height=15,font=("Lucida Calligraphy",22,"bold"))
#B.place(x=110,y=90)


blank=Label(win,fg="white",bg="black",width=16,height=6,font=("Lucida Calligraphy",22,"bold"))
blank.place(x=800,y=170)


talk=Label(win,text=" WELCOME 😊",fg="white",bg="black",font=("Lucida Calligraphy",18,"bold"))
talk.place(x=860,y=230)

tal=Label(win,text="👈 Login Here ",fg="white",bg="black",font=("Lucida Calligraphy",17,"bold"))
tal.place(x=860,y=310)


heading=Label(win,text="BY :- \n ❤ RENU PARETA ❤",fg="ivory2",bg="black",font=("Lucida Calligraphy",28,"bold"))
heading.place(x=720,y=500)

win.mainloop()