from tkinter import *
from PIL import Image, ImageTk
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import os

import pymysql as sql
def db_connect():
    conn=sql.connect(host='localhost',port=3306,user='root',password='',database='police')
    cur=conn.cursor()
    return conn,cur

def reset():
    a=Cent.get()
    b=Dent.get()
    c=Eent.get()
    
    
    cmd=f"select * from user where username= '{Cent.get()}'"
    conn,cur=db_connect()
    data=cur.execute(cmd)
    if data:
        cmd=f"update user set password='{Dent.get()}' where username='{Cent.get()}'"
        cur.execute(cmd)
        conn.commit()
        messagebox.showinfo("reset", "password changed successfully") 
        win.destroy()
        os.system("python second(login).py")
    else:
        messagebox.showwarning("warning","username not exist")
    
    
    messagebox.showinfo()
    
    '''
    if (a=="") or (b=="") or (c=="") :
        messagebox.showwarning("Warning","Please provide a valid input!!!")
    else:
        cmd=f"select * from user where username='{a}'"
        conn,cur=db_connect() # for call function (db_connect ())
        data=cur.execute(cmd) 
        if data :
            
            cmd=f"insert into user values ('{Cent.get()}', '{Dent.get()}', '{Eent.get()}')"
            conn,cur=db_connect()    
            cur.execute(cmd)
            conn.commit() # changes show krta hai
            messagebox.showinfo("Password","Password Change Successfully")
            win.destroy()     
            os.system("python second(login).py")       
        else :
            messagebox.showwarning("Warning","Username Not availble!!!")
          
          
      '''      
    
   
def cencel():
    win.destroy()
    
    os.system("python second(login).py") 

win=Tk()

win.geometry("900x800")

#win.state('zoomed') #output hmesha full screen me open hoga
files1=Image.open("C:\\Users\\HP\\Desktop\\police complain management python\\image\\reset.png")  # used for open image
files2=files1.resize((400,700)) #for assign size
 
tk_image=ImageTk.PhotoImage(files2) #tk_imagee is a var name and ImageTk.PhotoImage is predefined
 
new_Label=tk.Label(win,image=tk_image) # here is image= is predefined
new_Label.place(x=0,y=10) 

A=Label(win,text="Reset Password",bg="snow2",fg="black",font=("Lucida Calligraphy",27,"bold","underline"))
A.place(x=500,y=50)

C=Label(win,text="NAME",bg="snow2",fg="black",font=("Lucida Calligraphy",15,"bold"))
C.place(x=450,y=180)

Cent=Entry(win,bg="white",width=25,font=("Lucida Calligraphy",15,"bold"))
Cent.place(x=450,y=230)

D=Label(win,text="NEW PASSWORD",bg="snow2",fg="black",font=("Lucida Calligraphy",15,"bold"))
D.place(x=450,y=280)

Dent=Entry(win,bg="white",width=25,font=("Lucida Calligraphy",15,"bold"))
Dent.place(x=450,y=340)

E=Label(win,text="CONFIRM PASSWORD",bg="snow2",fg="black",font=("Lucida Calligraphy",15,"bold"))
E.place(x=450,y=400)

Eent=Entry(win,bg="white",width=25,font=("Lucida Calligraphy",15,"bold"))
Eent.place(x=450,y=470)


Lg=Button(win,text="Ok",bg="black",fg="white",width=7,height=1,font=("Lucida Calligraphy",14,"bold"),command=reset )
Lg.place(x=500,y=550)



Sg=Button(win,text="Cencel",bg="black",fg="white",width=7,height=1,font=("Lucida Calligraphy",14,"bold"),command=cencel )
Sg.place(x=650,y=550)


win.mainloop()