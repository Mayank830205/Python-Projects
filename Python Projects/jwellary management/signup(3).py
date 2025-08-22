from tkinter import *
from PIL import Image, ImageTk
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import pymysql as sql

def db_connect():
    conn=sql.connect(host='localhost',port=3306,user='root',password='',database='jwellery')
    cur=conn.cursor()
    return conn,cur

def signup(): # here signup button call by funtion 
    
    a=Cent.get()
    b=Dent.get()
    c=Eent.get()
    if (a=="") or (b=="") or (c=="") :
        messagebox.showwarning("Warning","Please provide a valid input!!!")
    else:
        cmd=f"insert into user values ('{Cent.get()}', '{Dent.get()}', '{Eent.get()}')"
        conn,cur=db_connect()    
        cur.execute(cmd)
        conn.commit()
        messagebox.showinfo("Send","Send Successfully")
        win.destroy()     
       
    
    
    
    
    
    
   

def cencel():
    win.destroy()
   
win=Tk()

win.geometry("200x200")
win.state('zoomed') #output hmesha full screen me open hoga
win.config(bg="BLACK")
files1=Image.open("C:\\Users\\HP\\Desktop\\JWELLARY MANAGEMENT\\image\\back.png")  # used for open image
files2=files1.resize((1300,700)) #for assign size
 
tk_image=ImageTk.PhotoImage(files2) #tk_imagee is a var name and ImageTk.PhotoImage is predefined
 
new_Label=tk.Label(win,image=tk_image) # here is image= is predefined
new_Label.pack() 

B=Label(win,bg="white",width=25,height=14,font=("Lucida Calligraphy",22,"bold"))
B.place(x=70,y=90)

A=Label(win,text="   Sign Up   ",bg="white",fg="black",font=("Lucida Calligraphy",30,"bold","underline"))
A.place(x=180,y=140)

C=Label(win,text="NAME",bg="white",fg="black",font=("Lucida Calligraphy",19,"bold"))
C.place(x=100,y=270)

Cent=Entry(win,bg="white",width=15,font=("Lucida Calligraphy",19,"bold"))
Cent.place(x=300,y=270)

D=Label(win,text="USERNAME",bg="white",fg="black",font=("Lucida Calligraphy",19,"bold"))
D.place(x=100,y=360)

Dent=Entry(win,bg="white",width=15,font=("Lucida Calligraphy",19,"bold"))
Dent.place(x=300,y=360)

E=Label(win,text="PASSWORD",bg="white",fg="black",font=("Lucida Calligraphy",19,"bold"))
E.place(x=100,y=450)

Eent=Entry(win,bg="white",width=15,font=("Lucida Calligraphy",19,"bold"))
Eent.place(x=300,y=450)


Lg=Button(win,text="Ok",width=5,height=1,font=("Lucida Calligraphy",16,"bold"),command=signup )
Lg.place(x=200,y=540)



Sg=Button(win,text="Cencel",width=6,height=1,font=("Lucida Calligraphy",16,"bold"),command=cencel)
Sg.place(x=400,y=540)


win.mainloop()