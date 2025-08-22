from tkinter import *
from tkinter import ttk,messagebox
import tkinter as tk
import os
from PIL import Image,ImageTk
import pymysql as sql
from tkcalendar import DateEntry
 
def Home():
    win.destroy()
    os.system("python home.py")

#def history():
 #   win.destroy()
  #  os.system("python history.py") 
    
def room():
    win.destroy()
    os.system("python rooms.py") 
    
def gallary():
    win.destroy()
    os.system("python gallery.py") 

def feedback():
    win.destroy()
    os.system("python feedback.py") 
    
def mybook():
    win.destroy()
    os.system("python bookingshow.py") 
    
def cencel():
    win.destroy()
    #os.system("python history.py") 
    

def book():
    win.destroy()
    os.system("python booking.py") 
 
win=Tk()
win.config(bg="#73FBFD")
win.state("zoomed")
#win.minsize(width="1920",height="1080")
#win.maxsize(width="1920",height="1080")

image= Image.open("C:\\Users\\HP\\Desktop\\hotel management system\\img4.jpg")
image = image.resize((1270,700))

tk_image = ImageTk.PhotoImage(image)
image_label = tk.Label(win,image=tk_image)
image_label.pack()

frame=Frame(win,bg="#1D4A8C",width=1920,height=100)
frame.place(x=0,y=1)   

lab=Label(frame,text="The Ritz \nIndia",width=10,height=0,fg="#FFFFFF",font=("bold",30),bg="#1D4A8C")
lab.place(x=0,y=0)

#btn=Button(frame,text="Home",width=8,fg="#FFFFFF",font=("bold",19),bg="#1D4A8C",relief="flat",command=Home)
#btn.place(x=300,y=20)

btn=Button(frame,text="Home",width=8,fg="#FFFFFF",font=("bold",19),bg="#1D4A8C",relief="flat",command=Home)
btn.place(x=430,y=20)
btn=Button(frame,text="Rooms",width=8,fg="#FFFFFF",font=("bold",19),bg="#1D4A8C",relief="flat",command=room)
btn.place(x=570,y=20)
btn=Button(frame,text="Gallery",width=8,fg="#FFFFFF",font=("bold",19),bg="#1D4A8C",relief="flat",command=gallary)
btn.place(x=700,y=20)
btn=Button(frame,text="Feedback",width=8,fg="#FFFFFF",font=("bold",19),bg="#1D4A8C",relief="flat",command=feedback)
btn.place(x=840,y=20)
btn=Button(frame,text="My Bookings",width=10,fg="#FFFFFF",font=("bold",19),bg="#1D4A8C",relief="flat",command=mybook)
btn.place(x=990,y=20)
btn=Button(frame,text="Cancel",width=9,fg="#FFFFFF",font=("bold",19),bg="#1D4A8C",relief="flat",command=cencel)
btn.place(x=1130,y=20)

btn=Button(win,text="Book Now",width=24,height=1,fg="white",font=("bold",20),bg="green",relief="flat",command=book)
btn.place(x=430,y=570)

lab=Label(text="Welcome To",width=10,height=1,fg="#FFFFFF",font=("bold",16),bg="#4A2A29")
lab.place(x=580,y=120)
lab=Label(text="The Ritz India",width=15,height=1,fg="#FFFFFF",font=("bold",25),bg="#4A2A29")
lab.place(x=500,y=180)

win.mainloop()