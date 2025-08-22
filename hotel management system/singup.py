from tkinter import *
from tkinter import ttk,messagebox
import tkinter as tk
import os
from PIL import Image,ImageTk
import pymysql as sql

def db_connect():
    
    conn=sql.connect(host='localhost',port=3306,user='root',password='', database="hotel")
    cur=conn.cursor()
    cur=conn.cursor()
    return conn,cur
  
  

def fun(): # here signup button call by funtion 
    
    a=ent1.get()
    b=ent2.get()
    #c=Eent.get()
    if (a=="") or (b=="") :
        messagebox.showwarning("Warning","Please provide a valid input!!!")
    else:
        cmd=f"insert into login values ('{ent1.get()}', '{ent2.get()}')"
        conn,cur=db_connect()    
        cur.execute(cmd)
        conn.commit()
        messagebox.showinfo("Send","Send Successfully")
        win.destroy()     
        os.system("python login.py")

 

win=Tk()
win.config(bg="skyblue")
win.state("zoomed")





def back():
    win.destroy()
    os.system("python login.py")



image= Image.open("C:\\Users\\HP\\Desktop\\hotel management system\\img5.jpeg")
image = image.resize((1280,700))

tk_image = ImageTk.PhotoImage(image)

image_label = tk.Label(win,image=tk_image)
image_label.pack()


lab=Label(win,text="",width=12,height=6,fg="#FFFEFE", font=("bold",50),bg="#F2D8A4")
lab.place(x=700,y=60)

lab=Label(win,text="Sign UP",width=10,fg="#000000", font=("bold",30),bg="#F2D8A4")
lab.place(x=830,y=90)


lab=Label(win,text="Username",width=8,fg="#000000",font=("bold",20) ,bg="#F2D8A4")
lab.place(x=730,y=180)
ent1=Entry(win,width=25,font=("bold",21),fg="#000000",bg="#F2D8A4")
ent1.place(x=730,y=240)


lab=Label(win,text="Password",width=8,fg="#000000",font=("bold",20),bg="#F2D8A4")
lab.place(x=730,y=290)
ent2=Entry(win,width=25,font=("bold",21),fg="#000000",bg="#F2D8A4")
ent2.place(x=730,y=350)

btn=Button(win,text="Sign up",width=11,height=1,fg="#000000",font=("bold",20),bg="#F2D8A4",command=fun)
btn.place(x=730,y=400)

btn=Button(win,text="back",width=11,height=1,fg="#000000",font=("bold",20),command=back,bg="#F2D8A4")
btn.place(x=940,y=400)

win.mainloop() 