from tkinter import *
from tkinter import ttk
import tkinter as tk
import os
from PIL import Image,ImageTk
 
def back():
    win.destroy()
    os.system("python Home.py")
 
def book():
    win.destroy()
    os.system("python booking.py")

win=Tk()
win.config(bg="white")
win.minsize(width="1280",height="700")
win.maxsize(width="1280",height="700")



file=PhotoImage(file="IMG13.png")
lab=Label(win,image=file)
lab.place(x=0,y=0)

file2=PhotoImage(file="IMG14.png")
lab2=Label(win,image=file2)
lab2.place(x=640,y=0)

lab=Label(win,text="DOUBLE BED",width=20,fg="#000000", font=("bold",25),bg="#F2D8A4")
lab.place(x=90,y=0)

lab=Label(win,text="SINGLE BET",width=20,fg="#000000", font=("bold",25),bg="#F2D8A4")
lab.place(x=740,y=0)

btn1=Button(win,text="BOOK NOW",width=25,height=1,fg="black",font=("bold",20),bg="#62DE3C" ,command=book)
btn1.place(x=100,y=550)

btn2=Button(win,text="BOOK NOW",width=25,height=1,fg="black",font=("bold",20),bg="#62DE3C",command=book)
btn2.place(x=750,y=550)

btn=Button(win,text="Back >>",width=10,height=1,fg="white",bg="blue",font=("bold",20),command=back)
btn.place(x=550,y=590)

win.mainloop()