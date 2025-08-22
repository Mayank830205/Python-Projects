from tkinter import *
from PIL import Image, ImageTk
import tkinter as tk
from tkinter import ttk
import os

def Home():
    win.destroy()
    
    os.system("python menubar.py") 

def Mydetail():
    win.destroy()
    os.system("python mydetail.py") 
    
    
def Merriage():
    win.destroy()
    os.system("python marriage.py") 
    
def Bday():
    win.destroy()
    os.system("python bdayhall.py") 

def Dance():
    win.destroy()
    os.system("python dancehall.py") 
    
    
def Viewfeedback():
    win.destroy()
    os.system("python viewfeedback.py") 
    
def Feedback():
    win.destroy()
    os.system("python Rating.py") 


win=Tk()

win.geometry("1100x700")
#win.state('zoomed')

win.config(bg="white")
files1=Image.open("C:\\Users\\HP\\Desktop\\Event managment\\image\\heart.png")  # used for open image
files2=files1.resize((1200,500)) #for assign size
 
tk_image=ImageTk.PhotoImage(files2) #tk_imagee is a var name and ImageTk.PhotoImage is predefined
 
new_Label=tk.Label(win,image=tk_image) # here is image= is predefined
new_Label.place(x=0,y=150) 

talk=Label(win,text="⭐EVENT MANAGMENT⭐",bg="white",fg="black",font=("Algerian",28,"bold"))
talk.place(x=20,y=30)

blank=Label(win,bg="white",fg="black",width=70,height=1,font=("Arial",22,"bold"))
blank.place(x=4,y=120)

b1=Button(win,bg="black",fg="white",text="Home",width=7,height=1,font=("Arial",14,"bold"),relief="flat",command=Home)
b1.place(x=15,y=120)

b2=Button(win,bg="black",fg="white",text="My Detail",width=7,height=1,font=("Arial",14,"bold"),relief="flat",command=Mydetail)
b2.place(x=120,y=120)

b3=Button(win,bg="black",fg="white",text="Merriage Hall",width=11,height=1,font=("Arial",14,"bold"),relief="flat", command=Merriage )
b3.place(x=230,y=120)

b4=Button(win,bg="black",fg="white",text="Birthday Hall",width=11,height=1,font=("Arial",14,"bold"),relief="flat",command=Bday )
b4.place(x=390,y=120)

b5=Button(win,bg="black",fg="white",text="Dance Hall",width=11,height=1,font=("Arial",14,"bold"),relief="flat",command=Dance )
b5.place(x=540,y=120)

b6=Button(win,bg="black",fg="white",text="View Feedback",width=11,height=1,font=("Arial",14,"bold"),relief="flat",command=Viewfeedback )
b6.place(x=690,y=120)

b7=Button(win,bg="black",fg="white",text="Feedback",width=9,height=1,font=("Arial",14,"bold"),relief="flat" ,command=Feedback)
b7.place(x=855,y=120)

b7=Button(win,fg="black",bg="white",text="Logout",width=9,height=1,font=("Arial",14,"bold"),relief="flat" )
b7.place(x=980,y=120)

#Blank=Label(win,bg="white",fg="black",width=34,height=13,font=("Arial",22,"bold"))
#Blank.place(x=110,y=190)


A=Label(win,text="  Detail  ",bg="firebrick4",fg="white",font=("Lucida Calligraphy",24,"bold","underline"))
A.place(x=300,y=200)

C=Label(win,text="First Name",bg="firebrick4",fg="white",font=("Lucida Calligraphy",16,"bold"))
C.place(x=150,y=290)

Cent=Entry(win,bg="white",width=20,font=("Lucida Calligraphy",16,"bold"))
Cent.place(x=350,y=290)

D=Label(win,text="Last Name",bg="firebrick4",fg="white",font=("Lucida Calligraphy",16,"bold"))
D.place(x=150,y=350)

Dent=Entry(win,bg="white",width=20,font=("Lucida Calligraphy",16,"bold"))
Dent.place(x=350,y=350)

E=Label(win,text="User Id",bg="firebrick4",fg="white",font=("Lucida Calligraphy",16,"bold"))
E.place(x=150,y=410)

Eent=Entry(win,bg="white",width=20,font=("Lucida Calligraphy",16,"bold"))
Eent.place(x=350,y=410)

F=Label(win,text="Password",bg="firebrick4",fg="white",font=("Lucida Calligraphy",16,"bold"))
F.place(x=150,y=470)

Fent=Entry(win,bg="white",width=20,font=("Lucida Calligraphy",16,"bold"))
Fent.place(x=350,y=470)

G=Label(win,text="Gender",bg="firebrick4",fg="white",font=("Lucida Calligraphy",16,"bold"))
G.place(x=150,y=530)

Gent=Entry(win,bg="white",width=20,font=("Lucida Calligraphy",16,"bold"))
Gent.place(x=350,y=530)

H=Label(win,text="Contact No.",bg="firebrick4",fg="white",font=("Lucida Calligraphy",16,"bold"))
H.place(x=150,y=690)

Hent=Entry(win,bg="white",width=20,font=("Lucida Calligraphy",16,"bold"))
Hent.place(x=350,y=690)

Lg=Button(win,text="Submit",bg="green",fg="white",font=("Lucida Calligraphy",14,"bold") )
Lg.place(x=550,y=580)


win.mainloop()