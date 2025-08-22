from tkinter import *
from tkinter import ttk,messagebox
import tkinter as tk
import os
from PIL import Image,ImageTk
import pymysql as sql

def db_connect():
    
    conn=sql.connect(host='localhost',port=3306,user='root',password='', database="cloth")
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
        cmd=f"insert into signup values ('{ent1.get()}', '{ent2.get()}')"
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
    os.system("python first..py")

def Home():
    win.destroy()
    os.system("python Home.py")


def sign():
    win.destroy()
    os.system("python signup.py")

image= Image.open("images//img2.jpg")
image = image.resize((1920,1080))

tk_image = ImageTk.PhotoImage(image)

image_label = tk.Label(win,image=tk_image)
image_label.pack()

lab=Label(win,text="",width=17,height=7,fg="#FFFEFE", font=("bold",50),bg="#0D0D0D")
lab.place(x=600,y=150)




lab=Label(win,text="Sign UP",width=10,fg="#FFFEFE", font=("bold",50),bg="#0D0D0D")
lab.place(x=750,y=180)


lab=Label(win,text="Username",width=8,fg="#FFFEFE",font=("bold",20) ,bg="#0D0D0D")
lab.place(x=664,y=300)
ent1=Entry(win,width=25,font=("bold",21),fg="#FFFEFE",bg="#0D0D0D")
ent1.place(x=800,y=300)


lab=Label(win,text="Password",width=8,fg="#FFFEFE",font=("bold",20),bg="#0D0D0D")
lab.place(x=664,y=400)
ent2=Entry(win,width=25,font=("bold",21),fg="#FFFEFE",bg="#0D0D0D")
ent2.place(x=800,y=400)


btn=Button(win,text="Sign UP",width=15,height=1,fg="#FFFEFE",font=("bold",20),bg="#0D0D0D",command=fun)
btn.place(x=650,y=550)

btn=Button(win,text="back",width=15,height=1,fg="#FFFEFE",font=("bold",20),command=back,bg="#0D0D0D")
btn.place(x=950,y=550)

win.mainloop()