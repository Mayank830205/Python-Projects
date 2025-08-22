from tkinter import *
from tkinter import ttk
import tkinter as tk
import os
from PIL import Image,ImageTk
 
win=Tk()
win.config(bg="white")
win.state("zoomed")
#win.minsize(width="1920",height="1080")
#win.maxsize(width="1920",height="1080")

def back():
    win.destroy()
    os.system("python first.py")

image= Image.open("C:\\Users\\HP\\Desktop\\hotel management system\\img9.png")
image = image.resize((1200,700))

tk_image = ImageTk.PhotoImage(image)
image_label = tk.Label(win,image=tk_image)
image_label.pack()



btn=Button(win,text="Back >>",width=10,height=1,fg="white",bg="blue",font=("bold",20),command=back)
btn.place(x=1020,y=570)
win.mainloop()