from tkinter import *
from tkinter import ttk,messagebox
import tkinter as tk
import os
from PIL import Image,ImageTk
def back():
    win.destroy()
    os.system("python first.py")

win=Tk()
win.config(bg="#FFFFFF")
win.state("zoomed")
#win.minsize(width="1920",height="1080")
#win.maxsize(width="1920",height="1080")

image= Image.open("C:\\Users\\HP\\Desktop\\hotel management system\\img8.jpg")
image = image.resize((600,700))

tk_image = ImageTk.PhotoImage(image)

image_label = tk.Label(win,image=tk_image)
image_label.place(x=0,y=0)

file=PhotoImage(file="img15.png")
lab=Label(win,image=file)
lab.place(x=750,y=90)


file1=PhotoImage(file="img17.png")
lab1=Label(win,image=file1)
lab1.place(x=750,y=210)



file2=PhotoImage(file="img19.png")
lab2=Label(win,image=file2)
lab2.place(x=750,y=360)

file3=PhotoImage(file="img20.png")
lab3=Label(win,image=file3)
lab3.place(x=750,y=510)

lab=Label(win,text="Our Office Address",width=15,fg="black", font=("bold",30),bg="#FFFFFF")
lab.place(x=800,y=50)

lab=Label(win,text="Mhaveer nagar vistar yojna 1-H-7 first floor main vist \nbuldding beside of shiv jyoti in front of Dot code\n edification convent kota west, rajasthan, kota",width=45,fg="black", font=("bold",13),bg="#FFFFFF")
lab.place(x=800,y=100)

lab=Label(win,text="General Enquiries",width=14,fg="black", font=("bold",30),bg="#FFFFFF")
lab.place(x=800,y=200)

lab=Label(win,text="Call US",width=6,fg="black", font=("bold",30),bg="#FFFFFF")
lab.place(x=800,y=350)

lab=Label(win,text="+91 697584955",width=13,fg="black", font=("bold",20),bg="#FFFFFF")
lab.place(x=800,y=400)

lab=Label(win,text="Our Timing",width=8,fg="black", font=("bold",30),bg="#FFFFFF")
lab.place(x=800,y=500)

lab=Label(win,text="Mon-Sun: 10:00AM 07:00PM",width=24,fg="black", font=("bold",15),bg="#FFFFFF")
lab.place(x=800,y=550)

btn=Button(win,text="Back >>",width=10,height=1,fg="white",bg="blue",font=("bold",20),command=back)
btn.place(x=1080,y=570)
win.mainloop()