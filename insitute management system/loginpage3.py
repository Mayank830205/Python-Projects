from tkinter import *
import tkinter as tk
from PIL import Image,ImageTk
from tkinter import ttk
from tkinter import messagebox
import os
import pymysql as sql

def db_connect():
    conn= sql.connect(host='localhost',user='root',password='',port=3306,database='institute__management__system')
    cur=conn.cursor()
    return conn,cur

def show():
    username=ent1.get().strip()   #extra space hta deta h strip()
    password=ent.get()
    cmd=f"select * from login where username='{username}'"
    conn,cur=db_connect()
    data=cur.execute(cmd)
    print(data)
    if data:
        cmd=f"select * from login where username='{username}' and password='{password}'"
        data=cur.execute(cmd)
        if data:
            messagebox.showinfo("Login Done","LoginSuccessfully")
            win.destroy()
            os.system("python mainpage.py")
            return afterlog()
        else:
            messagebox.showwarning("wrong Password","Incorrect Password")
    else:
        messagebox.showwarning("Not Exist","Not Registerd Account")

def afterlog():
    username=ent1.get()
    password=ent.get()
    if username=="" or password=="":
        messagebox.showwarning("Fill It","please fill all field")
    else:
        messagebox.showwarning("success","successfully login ")
        win.destroy()
        os.system("python mainpage.py")
    
def togglepassword():
    if ent.cget("show")=="":
        ent.config(show="*")
        eyebutton.config(text="👁️")
    else:
        ent.config(show="")
        eyebutton.config(text="😊")

def forget():
    win.destroy()
    os.system(" python forgetpass.py")

def cancel():
    win.destroy()
    os.system(" python afterprogerssbar.py")

def reset():
    entvar1.set("")
    entvar2.set("")

win=Tk()
win.state('zoomed')

#top pr icon lane k liyee
win.iconbitmap("D:\\insitute management system\\IMS project\\logouok.ico")     

image3=Image.open("D:\\insitute management system\\IMS project\\loginbggg.png")
image3=image3.resize((1550,900))
tk_image3=ImageTk.PhotoImage(image3)
image_label=tk.Label(win,image=tk_image3)
image_label.place(x=840,y=0)

image2=Image.open("D:\\insitute management system\\IMS project\\loginbggg.png")
image2=image2.resize((1550,900))
tk_image2=ImageTk.PhotoImage(image2)
image_label=tk.Label(win,image=tk_image2)
image_label.place(x=840,y=0)

#background k liye 
image=Image.open("D:\\insitute management system\\IMS project\\Picsart_24-12-27_02-40-00-703.png")
image=image.resize((850,790))
tk_image=ImageTk.PhotoImage(image)
image_label=tk.Label(win,bg="white",image=tk_image)
image_label.place(x=4,y=2)

image1=Image.open("D:\\insitute management system\\IMS project\\logo.png")
image1=image1.resize((160,160))
tk_image1=ImageTk.PhotoImage(image1)
image_label=tk.Label(win,bg="black",image=tk_image1)
image_label.place(x=345,y=49)

win.title(" U O K ")
win.geometry("1470x980")
win.config(bg="#EDEDED")

lbl=Label(win,text="Login To Your Account",bg="black",fg="white",font=("Impact",32))
lbl.place(x=244,y=186)
lbl=Label(win,text="Enter the details to get started",bg="black",fg="white",font=("Calibri Light (Headings)",13))
lbl.place(x=244,y=236)

lbl=Label(win,text="Username",bg="black",fg="white",font=("Aparajita",14,"bold"))
lbl.place(x=195,y=280)
entvar1=StringVar()
ent1=Entry(win,width=29,font=("Arial Black",17),textvariable=entvar1)
ent1.place(x=195,y=305)

lbl=Label(win,text="Password",bg="black",fg="white",font=("Aparajita",14,"bold"))
lbl.place(x=195,y=355)
entvar2=StringVar()
ent=Entry(win,width=29,font=("Arial Black",17),show="*",textvariable=entvar2)
ent.place(x=195,y=380)
eyebutton=ttk.Button(win,width=2,text="👁️",command=togglepassword)
eyebutton.place(x=640,y=384)

btn=Button(win,text="LOG IN",font=("Arial Black",17,"bold"),fg="black",bg="yellow",width=26,command=show)
btn.place(x=220,y=490)

btn=Button(win,text="Cancel",font=("Arial Black",13,"bold"),fg="black",bg="yellow",width=10,height=1,command=cancel)
btn.place(x=430,y=600)

btn=Button(win,text="Reset",font=("Arial Black",13,"bold"),fg="black",bg="yellow",width=10,height=1,command=reset)
btn.place(x=280,y=600)

btn=Button(win,text="forget Paasword ?",font=("Calibri Light (Headings)",11),fg="white",bg="black",width=14,height=1,command=forget)
btn.place(x=195,y=430)

win.mainloop()