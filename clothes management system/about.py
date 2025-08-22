from tkinter import *
from tkinter import ttk
import tkinter as tk
import os
from PIL import Image,ImageTk
 
win=Tk()
win.config(bg="#73FBFD")
win.state("zoomed")

def back():
    win.destroy()
    os.system("python Home.py")

image= Image.open("images\\img13.png")
image = image.resize((1300,780))

tk_image = ImageTk.PhotoImage(image)
image_label = tk.Label(win,image=tk_image)
image_label.pack()



btn=Button(win,text="Back",width=6,height=1,fg="#FFFEFE",font=("bold",20),command=back,bg="#09082E")
btn.place(x=1800,y=30)
win.mainloop()