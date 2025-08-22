from tkinter import *
from PIL import Image,ImageTk
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import pymysql as sql
import os
win=Tk()

def next1():
    win.destroy()
    os.system("python signup.py")

def next():
    win.destroy()
    os.system("python loginpage3.py")
    
win.state('zoomed')
win.title(" U O K ")
win.geometry("1650x784")

win.iconbitmap("D:\\insitute management system\\IMS project\\logouok.ico")

image=Image.open("D:\\insitute management system\\IMS project\\kotauok.png")
image=image.resize((1540,788))
tk_image=ImageTk.PhotoImage(image)
image_label=tk.Label(win,image=tk_image)
image_label.pack()

leb=Label(win,text=" Institute  Management  System ",font=("Bodoni MT Black",46,"underline"),bg="red",fg="yellow")
leb.place(x=520,y=710)
leb=Label(win,text=" Institute",font=("Bodoni MT Black",46,"underline"),bg="red",fg="white")
leb.place(x=520,y=710)

image1=Image.open("D:\\insitute management system\\IMS project\\logouok.png")
image1=image1.resize((160,150))
tk_image1=ImageTk.PhotoImage(image1)
image_label=tk.Label(win,image=tk_image1)
image_label.place(x=190,y=10)

btn=Button(win,text="LOGIN",width=7,height=1,bg="blue",fg="white",font=("Cooper Black",26),command=next)
btn.place(x=1200,y=630)

btn=Button(win,text="SIGNUP",width=7,height=1,bg="blue",fg="white",font=("Cooper Black",26),command=next1)
btn.place(x=1000,y=630)

win.mainloop()