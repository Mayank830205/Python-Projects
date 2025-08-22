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
 
def fun():
    a=ent1.get()
    b=ent2.get()
    cmd=f"select * from signup where username='{a}'" # first we chack username present or not 
    conn,cur=db_connect()
    data=cur.execute(cmd)
    if data: # if username data is present then
        cmd=f"select * from signup where username= '{ent1.get()}' and password= '{ent2.get()}'"   # if username and password both are present then
        data=cur.execute(cmd)
        if data:
            messagebox.showinfo("login", "Login Sucessfully")  # print it
            win.destroy()                                       # then excute all query
            os.system("python home.py")                      # then open menubar page
            
        else:
            messagebox.showwarning("warning","Wrong Password enter valid password")   # if username present but password not present then print it
            
    else:
        messagebox.showwarning("warning","username and password is not exist")


win=Tk()
win.config(bg="skyblue")
win.state("zoomed")

def Home():
    win.destroy()
    os.system("python home.py")


def sign():
    win.destroy()
    os.system("python signup.py")



image= Image.open("images//img3.jpg")
image = image.resize((1920,1080))

tk_image = ImageTk.PhotoImage(image)

image_label = tk.Label(win,image=tk_image)
image_label.pack()


lab=Label(win,text="",width=17,height=7,fg="#FFFEFE", font=("bold",50),bg="#0D0D0D")
lab.place(x=600,y=150)




lab=Label(win,text="LOG IN",width=10,fg="#FFFEFE", font=("bold",50),bg="#0D0D0D")
lab.place(x=750,y=190)


lab=Label(win,text="Username",width=8,fg="#FFFEFE",font=("bold",20) ,bg="#0D0D0D")
lab.place(x=664,y=300)
ent1=Entry(win,width=25,font=("bold",21),fg="#FFFEFE",bg="#0D0D0D")
ent1.place(x=800,y=300)


lab=Label(win,text="Password",width=8,fg="#FFFEFE",font=("bold",20),bg="#0D0D0D")
lab.place(x=664,y=400)
ent2=Entry(win,width=25,font=("bold",21),fg="#FFFEFE",bg="#0D0D0D")
ent2.place(x=800,y=400)

lab=Label(win,text="You have an account aalready ",width=25,fg="#FFFEFE",font=("bold",15),bg="#0D0D0D")
lab.place(x=664,y=460)

btn=Button(win,text="Sign up",width=6,fg="#73FBFD",font=("bold",15),bg="#0D0D0D",command=sign,relief=FLAT)
btn.place(x=935,y=455)

btn=Button(win,text="Log in",width=15,height=1,fg="#FFFEFE",font=("bold",20),bg="#0D0D0D",command=fun)
btn.place(x=650,y=550)

btn=Button(win,text="back",width=15,height=1,fg="#FFFEFE",font=("bold",20),bg="#0D0D0D")
btn.place(x=950,y=550)

win.mainloop()