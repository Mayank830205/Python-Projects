from tkinter import *
from tkinter import ttk,Frame,Button
import tkinter as tk
import os 
from PIL import Image,ImageTk
 
win=Tk()

#win.minsize(width="1920",height="1080")
#win.maxsize(width="1920",height="1080")
win.state("zoomed")

def book():
    win.destroy()
    os.system("python login.py")
image= Image.open("images\\img1.jpg")
image = image.resize((1920,1080))

tk_image = ImageTk.PhotoImage(image)

image_label = tk.Label(win,image=tk_image)
image_label.pack()





lab=Label(win,text="Welcome to Clothes Shop",width=20,fg="black", font=("bold",50),bg="#EBEBEB")
lab.place(x=310,y=50)



lab=Label(win,text="Popular Readymade Garment Retailers in Kota Rajasthan",width=45,fg="black", font=("bold",25),bg="#EBEBEB")
lab.place(x=270,y=130)

btn=Button(win,text="Shop Now",width=25,height=1,bg="#703F25",fg="black",font=("bold",25),command=book)
btn.place(x=310,y=900)





win.mainloop()