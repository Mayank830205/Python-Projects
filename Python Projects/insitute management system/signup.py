from tkinter import *
import tkinter as tk
from PIL import Image,ImageTk
import os
from tkinter import ttk
from tkinter import messagebox
from functools import reduce
import pymysql as sql

def db_connect():
    conn= sql.connect(host='localhost',user='root',password='',port=3306,database='institute__management__system')
    cur=conn.cursor()
    return conn,cur

def sign_up():
    name=ent1.get()
    username=ent2.get().strip()
    password=ent3.get()
    if (name=="") or (username=="") or (password==""):
        messagebox.showwarning("Warning","Please provide a valid input!!!")
    else:
        cmd=f"select username from login"
        conn,cur=db_connect()
        cur.execute(cmd)
        data=cur.fetchall()
        Username_set=list(reduce(lambda x,y:x+y,data))
    
        if username in Username_set:
            messagebox.showwarning("Warning","Username is already exists !!! try differnt username")
        else:
            cmd=f"insert into login values('{name}','{username}','{password}')"
            cur.execute(cmd)
            conn.commit()
            messagebox.showinfo("Sign Up","Account is successfully Created")
            clear()

def clear():
    entvar.set("")
    entvar1.set("")
    entvar2.set("")

win=Tk()
win.state("zoomed")
win.iconbitmap("D:\\insitute management system\\IMS project\\logouok.ico")
win.title(" U O K ")

image=Image.open("D:\\insitute management system\\IMS project\\imagessignuppp.png")
image=image.resize((1530,800))
tk_image=ImageTk.PhotoImage(image)
image_label=tk.Label(win,image=tk_image)
image_label.pack()

def togglepassword():
    if ent3.cget("show")=="":
        ent3.config(show="*")
        eyebutton.config(text="👁️")
    else:
        ent3.config(show="")
        eyebutton.config(text="😊")

def cancel():
    win.destroy()
    os.system(" python afterprogerssbar.py")
   
lbl=Label(win,text="Sign Up",fg="purple",bg="#F6F6F6",font=("Gill Sans Ultra Bold",60,"underline"))
lbl.place(x=900,y=70)

lbl=Label(win,text="Name",bg="#F6F6F6",fg="black",font=("Arial Black",35,"bold"))
lbl.place(x=750,y=200)
entvar=StringVar()
ent1=Entry(win,font=("Arial",25,"bold"),bg="#E3E3E3",width=20,textvariable=entvar)
ent1.place(x=1050,y=220)

lbl=Label(win,text="Username",bg="#F6F6F6",fg="black",font=("Arial Black",35,"bold"))
lbl.place(x=750,y=300)
entvar1=StringVar()
ent2=Entry(win,font=("Arial",25,"bold"),bg="#E3E3E3",width=20,textvariable=entvar1)
ent2.place(x=1050,y=320)

lbl=Label(win,text="Password",bg="#F6F6F6",fg="black",font=("Arial Black",35,"bold"))
lbl.place(x=750,y=400)
entvar2=StringVar()
ent3=Entry(win,font=("Arial",25,"bold"),bg="#E3E3E3",width=20,textvariable=entvar2)
ent3.place(x=1050,y=420)

btn1=Button(win,text="OK",width=12,bg="purple",fg="white",font=("Arial Black",22),command=sign_up)
btn1.place(x=850,y=580)
eyebutton=ttk.Button(win,width=2,text="👁️",command=togglepassword)
eyebutton.place(x=1390,y=426)

btn2=Button(win,text="Cancel",width=12,bg="purple",fg="white",font=("Arial Black",22),command=cancel)
btn2.place(x=1140,y=580)
win.mainloop()