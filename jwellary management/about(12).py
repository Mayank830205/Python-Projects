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
    os.system("python Home.py")

image= Image.open("C:\\Users\\HP\\Desktop\\JWELLARY MANAGEMENT\\image\\about.png")
image = image.resize((1260,650))

tk_image = ImageTk.PhotoImage(image)
image_label = tk.Label(win,image=tk_image)
image_label.pack()



btn=Button(win,text="Back>>",width=6,height=1,fg="#FFFEFE",font=("bold",20),command=back,bg="#09082E")
btn.place(x=1140,y=596)
win.mainloop()