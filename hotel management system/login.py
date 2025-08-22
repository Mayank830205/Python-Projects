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
 
def login():
    a=ent1.get()
    b=ent2.get()
    cmd=f"select * from login where username='{a}'" # first we chack username present or not 
    conn,cur=db_connect()
    data=cur.execute(cmd)
    if data: # if username data is present then
        cmd=f"select * from login where username= '{ent1.get()}' and password= '{ent2.get()}'"   # if username and password both are present then
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

def back():
    win.destroy()
    os.system("python first.py")



def fun():
    win.destroy()
    os.system("python singup.py")

image= Image.open("C:\\Users\\HP\\Desktop\\hotel management system\\img5.jpeg")
image = image.resize((1280,700))

tk_image = ImageTk.PhotoImage(image)

image_label = tk.Label(win,image=tk_image)
image_label.pack()

lab=Label(win,text="",width=15,height=8,fg="#FFFEFE", font=("bold",40),bg="#F2D8A4")
lab.place(x=700,y=60)

lab=Label(win,text="LOG IN",width=10,fg="#000000", font=("bold",30),bg="#F2D8A4")
lab.place(x=830,y=90)


lab=Label(win,text="Username",width=8,fg="#000000",font=("bold",20) ,bg="#F2D8A4")
lab.place(x=730,y=180)
ent1=Entry(win,width=25,font=("bold",21),fg="#000000",bg="#F2D8A4")
ent1.place(x=730,y=240)


lab=Label(win,text="Password",width=8,fg="#000000",font=("bold",20),bg="#F2D8A4")
lab.place(x=730,y=290)
ent2=Entry(win,width=25,font=("bold",21),fg="#000000",bg="#F2D8A4")
ent2.place(x=730,y=350)

lab=Label(win,text="You don't have any account ? ",width=25,fg="#000000",font=("bold",15),bg="#F2D8A4")
lab.place(x=730,y=400)

btn=Button(win,text="Sign up",width=6,fg="green",font=("bold",15),bg="#F2D8A4",relief=FLAT,command=fun)
btn.place(x=1000,y=400)

btn=Button(win,text="Log in",width=13,height=1,fg="#000000",font=("bold",20),bg="#F2D8A4",command=login)
btn.place(x=700,y=460)

btn=Button(win,text="back",width=13,height=1,fg="#000000",font=("bold",20),command=back,bg="#F2D8A4")
btn.place(x=930,y=460)

win.mainloop()