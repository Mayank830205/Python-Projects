from tkinter import *
from tkinter import ttk,messagebox
import tkinter as tk
import os
from PIL import Image,ImageTk
import pymysql as sql
from tkcalendar import DateEntry
 
win=Tk()
win.config(bg="#73FBFD")
win.state("zoomed")
#win.minsize(width="1920",height="1080")
#win.maxsize(width="1920",height="1080")

def booking():
    win.destroy()
    os.system("python booking.py")

def contact():
    win.destroy()
    os.system("python contact.py")

def service():
    win.destroy()
    os.system("python service.py")

def Home():
    win.destroy()
    os.system("python Home.py")

def About():
    os.system("python About.py") 

def cancel():
    win.destroy()
    
def mybook():
    win.destroy()
    os.system("python mycart.py")    

def show():
    a=ent1.get()
    if a=="":
        messagebox.showerror("empty","Please fill the train details ")
        messagebox.showinfo("Success","Search Train")
    
    win.destroy()
    os.system("python train.py")

image= Image.open("images//img3.jpg")
image = image.resize((1920,1080))

tk_image = ImageTk.PhotoImage(image)
image_label = tk.Label(win,image=tk_image)
image_label.pack()




frame=Frame(win,bg="#F0B87B",width=1920,height=100)
frame.place(x=0,y=1)

lab=Label(frame,text="Online Fation Store",width=25,height=0,fg="#000000",font=("bold",30),bg="#F0B87B")
lab.place(x=0,y=25)


btn=Button(frame,text="Home",width=8,fg="#000000",font=("bold",20),bg="#F0B87B",relief="flat",command=Home)
btn.place(x=490,y=20)

btn=Button(frame,text="About",width=8,fg="#000000",font=("bold",20),bg="#F0B87B",command=About,relief="flat")
btn.place(x=600,y=20)
btn=Button(frame,text="Order",width=8,fg="#000000",font=("bold",20),bg="#F0B87B",command=mybook,relief="flat")
btn.place(x=720,y=20)
btn=Button(frame,text="Contact",width=8,fg="#000000",font=("bold",20),bg="#F0B87B",relief="flat",command=contact)
btn.place(x=850,y=20)
btn=Button(frame,text="Service",width=8,fg="#000000",font=("bold",20),bg="#F0B87B",relief="flat",command=service)
btn.place(x=980,y=20)
btn=Button(frame,text="Logout",width=8,fg="#000000",font=("bold",20),bg="#F0B87B",relief="flat",command=cancel)
btn.place(x=1100,y=20)

ent1=Entry(win,width=70,font=("bold",35),fg="#000000",bg="#F0F0F0")
ent1.place(x=0,y=100)

file3=PhotoImage(file="images//img4.png")
lab3=Label(win,image=file3)
lab3.place(x=1800,y=105)

lab=Label(win,text="",width=10,height=5,fg="#000000", font=("bold",50),bg="#F0B87B")
lab.place(x=175,y=290)
file=PhotoImage(file="images//img5.png")
lab=Label(win,image=file)
lab.place(x=200,y=300)
lab=Label(win,text="Clothes for Man ",width=20,height=1,fg="#000000", font=("bold",20),bg="#F0B87B")
lab.place(x=200,y=550)
btn=Button(win,text="More",width=20,height=1,fg="#000000",font=("bold",20),bg="#A1FB8E",)
btn.place(x=205,y=600)


lab=Label(win,text="",width=10,height=5,fg="#000000", font=("bold",50),bg="#F0B87B")
lab.place(x=775,y=290)
file1=PhotoImage(file="images//img6.png")
lab1=Label(win,image=file1)
lab1.place(x=800,y=300)
lab=Label(win,text="Clothes for Woman ",width=20,height=1,fg="#000000", font=("bold",20),bg="#F0B87B")
lab.place(x=810,y=550)
btn=Button(win,text="More",width=20,height=1,fg="#000000",font=("bold",20),bg="#A1FB8E",)
btn.place(x=810,y=600)


lab=Label(win,text="",width=10,height=5,fg="#000000", font=("bold",50),bg="#F0B87B")
lab.place(x=1375,y=290)
file2=PhotoImage(file="images//img7.png")
lab2=Label(win,image=file2)
lab2.place(x=1400,y=300)
lab=Label(win,text="Clothes for Kids ",width=20,height=1,fg="#000000", font=("bold",20),bg="#F0B87B")
lab.place(x=1420,y=550)
btn=Button(win,text="More",width=20,height=1,fg="#000000",font=("bold",20),bg="#A1FB8E",)
btn.place(x=1410,y=600)
win.mainloop()