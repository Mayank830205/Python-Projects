from tkinter import *
from tkinter import ttk,Frame,Button
import tkinter as tk
import os 
from PIL import Image,ImageTk
 
win=Tk()
win.state("zoomed")
#win.minsize(width="1920",height="1080")
#win.maxsize(width="1920",height="1080")

def book():
    win.destroy()
    os.system("python login.py")
    
def back():
    win.destroy()
    os.system("python first.py")

'''def Home():
    win.destroy()
    os.system("python home.py")
'''

def login():
    win.destroy()
    os.system("python login.py")
    
def contact():
    win.destroy()
    os.system("python contact.py")

def history():
    win.destroy()
    os.system("python history.py")

image= Image.open("C:\\Users\\HP\\Desktop\\hotel management system\\img2.jpg")
image = image.resize((1280,700))

tk_image = ImageTk.PhotoImage(image)

image_label = tk.Label(win,image=tk_image)
image_label.pack()



lab=Label(win,text="",width=50,height=1,fg="#000000", font=("bold",50),bg="#75B2FA")
lab.place(x=0,y=0)
frame=Frame(win,bg="#75B2FA",width=1280,height=70)
frame.place(x=0,y=45)
lab=Label(win,text=" The Ritz \nIndia ",width=10,fg="#000000", font=("bold ",30),bg="#75B2FA")
lab.place(x=0,y=0)                                                       

lab=Label(win,text="Welcome to The Ritz India",width=20,fg="#000000", font=("bold",20),bg="#75B2FA")
lab.place(x=500,y=0)

btn=Button(frame,text="Home",width=9,fg="#000000",font=("bold",15),bg="#75B2FA",relief="flat")#,command=Home)
btn.place(x=550,y=20)
btn=Button(frame,text="Login",width=9,fg="#000000",font=("bold",15),bg="#75B2FA",relief="flat",command=login)
btn.place(x=700,y=20)

btn=Button(frame,text="ContactUs",width=9,fg="#000000",font=("bold",15),bg="#75B2FA",relief="flat",command=contact)
btn.place(x=850,y=20)
btn=Button(frame,text="History",width=9,fg="#000000",font=("bold",15),bg="#75B2FA",relief="flat",command=history)
btn.place(x=1000,y=20)
btn=Button(frame,text="BOOK NOW",width=10,fg="#000000",font=("bold",15),bg="#75B2FA",relief="flat",command=book)
btn.place(x=1140,y=0)

lab=Label(win,text="",width=10,height=5,fg="#000000", font=("bold",50),bg="#205210")
lab.place(x=800,y=200)

lab=Label(win,text="Welcome to our hotel, where comfort meets",width=35,fg="#FFFFFF", font=("bold",15),bg="#205210")
lab.place(x=800,y=250)

lab=Label(win,text="elegance.",width=8,fg="#FFFFFF", font=("bold",15),bg="#205210")
lab.place(x=800,y=276)

lab=Label(win,text="We're delighted to youras our guset and are\n committed to making your stay unforgattable.",width=35,fg="#FFFFFF", font=("bold",15),bg="#205210")
lab.place(x=800,y=310)

lab=Label(win,text="Relax, unwind, and let us take care of every",width=35,fg="#FFFFFF", font=("bold",15),bg="#205210")
lab.place(x=800,y=380)

lab=Label(win,text="detail.",width=5,fg="#FFFFFF", font=("bold",15),bg="#205210")
lab.place(x=800,y=410)

lab=Label(win,text="Your satisfaction is our priority, and we hope",width=35,fg="#FFFFFF", font=("bold",15),bg="#205210")
lab.place(x=800,y=439)

lab=Label(win,text="you feel at homr with us.",width=20,fg="#FFFFFF", font=("bold",15),bg="#205210")
lab.place(x=800,y=470)

btn=Button(win,text="Book Now",width=15,height=2,bg="#75B2FA",fg="#000000",font=("bold",20),relief="flat",command=book)
btn.place(x=1650,y=60)

btn=Button(win,text="Chack Availability",width=15,height=1,bg="#FFFFFF",fg="#000000",font=("bold",20),relief="flat",command=book)
btn.place(x=870,y=500)



win.mainloop()