from tkinter import *
import tkinter as tk
from PIL import Image,ImageTk
from tkinter import ttk
import os
import pymysql as sql
from tkinter import messagebox

def db_connect():
    conn= sql.connect(host='localhost',user='root',password='',port=3306,database='institute__management__system')
    cur=conn.cursor()
    return conn,cur

def forgot_password():
    username=ent.get().strip()
    new_password1=ent2.get()
    new_password2=ent1.get()
    if (username=="") or (new_password1=="") or (new_password2==""):
        messagebox.showwarning("Warning","Please provide a valid input!!!")
    
    elif  new_password1!=new_password2:
        messagebox.showwarning("Warning","password not matched")
    else:
        cmd=f"update login set password='{new_password1}' where username='{username}'"
        conn,cur=db_connect()
        cur.execute(cmd)
        conn.commit()
        messagebox.showinfo("reset","password successfully changed")
        clear()

def clear():
    entvar1.set("")
    entvar2.set("")
    entvar3.set("")

def cancel():
    win.destroy()
    os.system(" python loginpage3.py")

def toggle_password():
    if ent1.cget("show")=="":
        ent1.config(show="*")
        eye_button.config(text="👁️")
    else:
        ent1.config(show="")
        eye_button.config(text="😊")

def togglepassword():
    if ent2.cget("show")=="":
        ent2.config(show="*")
        eyebutton.config(text="👁️")
    else:
        ent2.config(show="")
        eyebutton.config(text="😊")

win=Tk()
win.state("zoomed")
win.config(bg="black")
win.iconbitmap("D:\\insitute management system\\IMS project\\logouok.ico")
win.title(" U O K ")

lbl=Label(win,bg="white",width=73,height=36)
lbl.place(x=300,y=100)
lbl=Label(win,bg="black",width=140,height=33)
lbl.place(x=320,y=120)
lbl=Label(win,bg="white",width=73,height=33)
lbl.place(x=800,y=120)
lbl=Label(win,bg="darkred",width=2,height=10)
lbl.place(x=830,y=280)
lbl=Label(win,text="FORGET YOUR",bg="white",fg="black",font=("Arial Black",38),width=13,height=1)
lbl.place(x=853,y=280)
lbl=Label(win,text="PASSWORD",bg="white",fg="black",font=("Arial Black",38),width=11,height=1)
lbl.place(x=880,y=350)

lbl=Label(win,text="Please enter a new password below...",bg="black",fg="white",font=("Aparajita",15),width=32,height=3)
lbl.place(x=322,y=120)

lbl=Label(win,text="Username",bg="black",fg="white",font=("Aparajita",16,"bold"))
lbl.place(x=322,y=215)
entvar1=StringVar()
ent=Entry(win,font=(16),width=39,textvariable=entvar1)
ent.place(x=327,y=240)

lbl2=Label(win,text="New Password *",bg="black",fg="white",font=("Aparajita",16,"bold"),width=13,height=1)
lbl2.place(x=322,y=304)
entvar2=StringVar()
ent2=Entry(win,font=("Aparajita",16),width=36,show="*",textvariable=entvar2)
ent2.place(x=327,y=330)
eyebutton=ttk.Button(win,width=2,text="👁️",command=togglepassword)
eyebutton.place(x=740,y=332)

lbl1=Label(win,text="Re-enter new password *",bg="black",fg="white",font=("Aparajita",16,"bold"),width=20,height=1)
lbl1.place(x=322,y=383)
entvar3=StringVar()
ent1=Entry(win,font=("Aparajita",16),width=36,show="*",textvariable=entvar3)
ent1.place(x=327,y=410)
eye_button=ttk.Button(win,width=2,text="👁️",command=toggle_password)
eye_button.place(x=740,y=412)

lbl=Label(win,text="short: Your password is to short.",bg="black",fg="white",font=("Calibri Light (Headings)",16,"bold"))
lbl.place(x=327,y=460)
lbl=Label(win,text="Hint:-The password should be at least twenty characters long.To make it",bg="black",fg="white",font=("Calibri Light (Headings)",10))
lbl.place(x=327,y=490)
lbl=Label(win,text="stronger, use upper and lower case letter,number and symbols like !\"?$%^&",bg="black",fg="white",font=("Calibri Light (Headings)",10))
lbl.place(x=327,y=510)

btn=Button(win,text="Submit",font=("Calibri Light (Headings)",15,"bold"),command=forgot_password)
btn.place(x=390,y=560)
btn=Button(win,text="Cancel",font=("Calibri Light (Headings)",15,"bold"),command=cancel)
btn.place(x=570,y=560)
win.mainloop()