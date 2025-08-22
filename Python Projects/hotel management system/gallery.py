from tkinter import *
from tkinter import ttk
import tkinter as tk
import os
from PIL import Image,ImageTk

def back():
    win.destroy()
    os.system("python Home.py")

 
win=Tk()
win.config(bg="white")
win.minsize(width="1280",height="720")
win.maxsize(width="1280",height="720")
image= Image.open("C:\\Users\\HP\\Desktop\\hotel management system\\IMG14.jpg")
image = image.resize((1250,700))

tk_image = ImageTk.PhotoImage(image)
image_label = tk.Label(win,image=tk_image)
image_label.pack()

lab=Label(win,text="The Ritz Hotel India",width=30,height=0,fg="#FFFFFF",font=("bold",30),bg="#1D4A8C")
lab.place(x=30,y=0)

btn=Button(win,text="Back >>",width=10,height=1,fg="white",bg="blue",font=("bold",20),command=back)
btn.place(x=1020,y=570)

win.mainloop()