from tkinter import *
from tkinter import ttk,messagebox
import tkinter as tk
import os
from PIL import Image,ImageTk
 

win=Tk()
win.config(bg="skyblue")
win.state("zoomed")

def Home():
    win.destroy()
    os.system("python Home.py")


image= Image.open("images//img9.jpg")
image = image.resize((1270,600))

tk_image = ImageTk.PhotoImage(image)

image_label = tk.Label(win,image=tk_image)
image_label.place(x=0,y=110)


lab=Label(win,text="",width=100,height=2,fg="#FFFEFE", font=("bold",35),bg="#507F80")
lab.place(x=0,y=0)


lab=Label(win,text="Here are Some Facilities Available on Clothes\n shop and at Clothe Bajar",width=40,height=2,fg="#000000", font=("bold",25),bg="#507F80")
lab.place(x=10,y=10)

btn=Button(win,text="back Home",width=15,height=1,fg="#FFFFFF",font=("bold",20),command=Home,bg="#0023F5")
btn.place(x=1550,y=30)

win.mainloop()