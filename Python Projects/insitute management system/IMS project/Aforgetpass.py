from tkinter import *
import tkinter as tk
from tkinter import ttk
import os

win=Tk()
win.state("zoomed")
win.geometry("300x300")
win.config(bg="white")
win.iconbitmap("D:\insitute management system\logouok.ico")
win.title(" U O K ")

'''def cancel():
    win.destroy()
    os.system(" python loginpage3.py")'''

lbl=Label(win,bg="black",width=73,height=36)
lbl.place(x=800,y=120)
lbl=Label(win,bg="darkred",width=73,height=36)
lbl.place(x=780,y=100)

lbl=Label(win,bg="black",width=69,height=36)
lbl.place(x=320,y=120)
lbl=Label(win,bg="darkred",width=73,height=36)
lbl.place(x=300,y=100)
lbl=Label(win,bg="white",width=63,height=33)
lbl.place(x=320,y=120)

file=PhotoImage(file="D:\insitute management system\imagepng(14).png")
lbl=Label(win,image=file,width=460,height=500)
lbl.place(x=320,y=120)

lbl=Label(win,text="Forget your password ?",bg="darkred",fg="white",font=("Arial Black",24,"bold","underline"))
lbl.place(x=815,y=150)
lbl=Label(win,text="Please enter the email address you'd like your password",bg="darkred",fg="white",font=("Calibri Light (Headings)",13,"bold"))
lbl.place(x=815,y=250)
lbl=Label(win,text="reset information sent to....",bg="darkred",fg="white",font=("Calibri Light (Headings)",13,"bold"))
lbl.place(x=815,y=270)

lbl=Label(win,text="Email address & Mobile No.",bg="darkred",fg="white",font=("Aparajita",18,"bold"))
lbl.place(x=815,y=358)
ent=Entry(win,font=(20),width=40)
ent.place(x=815,y=390)

btn=Button(win,text="Submid",font=("Cooper Black",22,"bold"),bg="yellow",fg="darkred",width=21)
btn.place(x=815,y=490)

btn=Button(win,text="Cancel",font=("Arial Black",15,"bold"),fg="black",bg="yellow",width=10)
btn.place(x=966,y=580)
win.mainloop()