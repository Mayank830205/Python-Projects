from tkinter import *
from PIL import Image, ImageTk
import tkinter as tk
from tkinter import ttk
import pymysql as sql
from tkinter import messagebox
import os
 
def db_connect():
    conn=sql.connect(host='localhost',port=3306,user='root',password='',database='Event')
    cur=conn.cursor()
    return conn,cur

    
def submit():
    a=Cent.get()
    b=Dent.get()
    c=Eent.get()
    d=Fent.get()
    #d=Eent.get()
    if (a=="") or (b=="") or (c=="") or (d=="") :
        messagebox.showwarning("Warning","Please provide a valid input!!!")
    else:
        cmd=f"insert into contactme(Name, Email, Subject, Message) values('{a}','{b}', '{c}','{d}')"
        conn,cur=db_connect()      
        cur.execute(cmd)
        conn.commit()
        messagebox.showinfo("Send","Send Successfully")
        win.destroy()
      
   


win=Tk()

win.geometry("940x550")
#win.state('zoomed')
win.config(bg="white")

files1=Image.open("C:\\Users\\HP\\Desktop\\Event managment\\image\\contact.png")  # used for open image
files2=files1.resize((1000,550)) #for assign size
 
tk_image=ImageTk.PhotoImage(files2) #tk_imagee is a var name and ImageTk.PhotoImage is predefined
 
new_Label=tk.Label(win,image=tk_image) # here is image= is predefined
new_Label.pack()

con=Label(win,text="🙏...Contact...🙏",bg="white",fg="black",font=("Lucida Calligraphy",28,"bold"))
con.place(x=370,y=20)

C=Label(win,text="NAME",bg="white",fg="black",font=("Lucida Calligraphy",15,"bold"))
C.place(x=350,y=150)

Cent=Entry(win,bg="white",width=15,font=("Lucida Calligraphy",15,"bold"))
Cent.place(x=570,y=150)

D=Label(win,text="Email",bg="white",fg="black",font=("Lucida Calligraphy",15,"bold"))
D.place(x=350,y=200)

Dent=Entry(win,bg="white",width=15,font=("Lucida Calligraphy",15,"bold"))
Dent.place(x=570,y=200)

E=Label(win,text="Subject",bg="white",fg="black",font=("Lucida Calligraphy",15,"bold"))
E.place(x=350,y=250)

Eent=Entry(win,bg="white",width=15,font=("Lucida Calligraphy",15,"bold"))
Eent.place(x=570,y=250)

F=Label(win,text="Message",bg="white",fg="black",font=("Lucida Calligraphy",15,"bold"))
F.place(x=350,y=300)

Fent=Entry(win,bg="white",width=15,font=("Lucida Calligraphy",15,"bold"))
Fent.place(x=570,y=300)


 
  
c3=Button(win,bg="green",fg="white",text="Send",width=7,height=1,font=("Arial",14,"bold"),relief="flat",command=submit )
c3.place(x=760,y=350)
  
  
det=Label(win,text="india \n Phone -1234567890 \n Subject- contact to management \n Email- abc@gmail.com",bg="white",fg="black",font=("Lucida Calligraphy",12,"bold"))
det.place(x=600,y=430)



win.mainloop()