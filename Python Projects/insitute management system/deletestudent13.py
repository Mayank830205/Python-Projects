from tkinter import *
import tkinter as tk
from PIL import Image,ImageTk
from tkinter import ttk
import os
from tkinter import messagebox
import pymysql as sql
win=Tk()
win.state("zoomed")
win.iconbitmap("D:\\insitute management system\\IMS project\\logouok.ico")
win.title(" U O K ")

def db_connect():
    conn= sql.connect(host='localhost',user='root',password='',port=3306,database='institute__management__system')
    cur=conn.cursor()
    return conn,cur

def deletestudent():
    registration_no=ent.get()
    cmd=f"delete from student_record where reg_no='{ent.get()}'"
    conn,cur=db_connect()
    data=cur.execute(cmd)
    conn.commit()
    if registration_no=="":
        messagebox.showwarning("","enter registration no.")
    elif data:
        messagebox.showinfo("","Student record successfully deleted")
        clear()
    else:
        messagebox.showwarning("Warning","This record not exist")
        clear()

def deleteteacher():
    reg_no=ent1.get()
    cmd=f"delete from teacher_record where reg_no='{ent1.get()}'"
    conn,cur=db_connect()
    data=cur.execute(cmd)
    conn.commit()
    if reg_no=="":
        messagebox.showwarning("","enter registration no.")
    elif data:
        messagebox.showinfo("","Student record successfully deleted")
        clear()
    else:
        messagebox.showwarning("Warning","This record not exist")
        clear()
        
def clear():
    entvar1.set("")
    entvar2.set("")

def cancel():
    win.destroy()
    os.system("python mainpage.py")

image=Image.open("D:\\insitute management system\\IMS project\\delete bg.png")
image=image.resize((1550,800))
tk_image=ImageTk.PhotoImage(image)
image_label=tk.Label(win,image=tk_image)
image_label.place(x=0,y=0)

lbl=Label(win,bg="#FFDB01",width=80,height=20)
lbl.place(x=90,y=60)
lbl=Label(win,bg="#FFDB01",width=80,height=20)
lbl.place(x=90,y=430)

lbl=Label(win,text="Delete Student Records",bg="#FFDB01",fg="black",font=("Arial Black",30,"bold","underline"))
lbl.place(x=110,y=70)
entvar1=StringVar()
ent=Entry(win,width=30,font=("Calibri (Body)",20),textvariable=entvar1)
ent.place(x=150,y=170)
btn=Button(win,text="Delete",width=15,bg="red",fg="white",font=("Calibri (Body)",17,"bold"),command=deletestudent)
btn.place(x=260,y=270)

lbl=Label(win,text="Delete Teachers Records",bg="#FFDB01",fg="black",font=("Arial Black",28,"bold","underline"))
lbl.place(x=110,y=440)
entvar2=StringVar()
ent1=Entry(win,width=30,font=("Calibri (Body)",20),textvariable=entvar2)
ent1.place(x=150,y=540)
btn=Button(win,text="Delete",width=15,bg="red",fg="white",font=("Calibri (Body)",17,"bold"),command=deleteteacher)
btn.place(x=260,y=640)

btn=Button(win,text="Cancel",width=13,height=1,bg="red",fg="white",font=("Calibri (Body)",17,"bold"),command=cancel)
btn.place(x=660,y=690)

win.mainloop()