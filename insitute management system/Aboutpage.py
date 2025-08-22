from tkinter import *
import tkinter as tk
from PIL import Image,ImageTk
from tkinter import ttk
import os
from tkinter import messagebox
import pymysql as sql

def cancel():
    win.destroy()
    os.system("python mainpage.py")

win=Tk()
win.state("zoomed")
win.iconbitmap("D:\\insitute management system\\IMS project\\logouok.ico")
win.title(" U O K ")

image=Image.open("D:\\insitute management system\\IMS project\\Aboutpagebg.png")
image=image.resize((1550,960))
tk_image=ImageTk.PhotoImage(image)
image_label=tk.Label(win,image=tk_image)
image_label.place(x=0,y=0)

lbl=Label(win,bg="black",width=130,height=45)
lbl.place(x=70,y=60)

image1=Image.open("D:\\insitute management system\\IMS project\\Screenshottt.png")
image1=image1.resize((870,578))
tk_image1=ImageTk.PhotoImage(image1)
image_label=tk.Label(win,image=tk_image1)
image_label.place(x=90,y=160)

lbl=Label(win,text="About Institute",bg="black",fg="#F7F3F2",font=("Arial Black",46,"bold","underline"))
lbl.place(x=300,y=60)

btn=Button(win,text="Back",width=12,bg="black",fg="white",font=("Calibri (Body)",12,"bold"),command=cancel)
btn.place(x=460,y=742)
win.mainloop()