from tkinter import *
import tkinter as tk
from PIL import Image,ImageTk
from tkinter import ttk
from tkinter import messagebox
from functools import reduce
import pymysql as sql
import os
import datetime

def clear():
    entvar1.set("")
    entvar2.set("")
    entvar3.set("")    
    entvar4.set("")
    entvar5.set("")

def cancel():
    win.destroy()
    os.system("python mainpage.py")

def db_connect():
    conn= sql.connect(host='localhost',user='root',password='',port=3306,database='institute__management__system')
    cur=conn.cursor()
    return conn,cur

def show():
    reg_no=ent1.get()
    
    if reg_no=="":
        messagebox.showwarning("Warning","Please fill all fields!!!")
        clear()
    else:
        cmd=f"select name,mother_name,duration from student_record where reg_no='{ent1.get()}'"
        conn,cur=db_connect()
        cur.execute(cmd) 
        record=cur.fetchone()
        if record:
            ent2.insert(0,record[0])
            ent3.insert(0,record[1])
            ent4.insert(0,record[2])
        conn.commit()
        
def submit():
    reg_no=(ent1.get())
    fullname=(ent2.get())
    mothername=(ent3.get())
    duration=(ent4.get())
    fees=(ent5.get())
    x=datetime.datetime.now()
    year=x.strftime("%Y")           #date functions   Y=year , b= small month name , d=date
    month=x.strftime("%b")
    day=x.strftime("%d")
    date=day+"-"+month+"-"+year

    if reg_no=="" or fullname=="" or mothername=="" or duration=="" or fees=="":
        messagebox.showwarning("warning","please provide a valid input")
    else:
        conn,cur=db_connect()
        cmd=f"insert into fees_record (reg_no,fees,date) values ('{reg_no}','{fees}','{date}')"
        cur.execute(cmd)
        conn.commit()
        messagebox.showinfo("success","successfuly")
        clear()

    '''if reg_no == "":
        messagebox.showwarning("Warning","Please provide a valid input!!!")
    else:
        cmd=f"select reg_no from student_record"
        conn,cur=db_connect()
        data=cur.execute(cmd)
        cur.fetchall()
        r_set = list(reduce(lambda x, y: x + y, data))
        if reg_no in r_set:
            cmd=f"insert into fees_record (reg_no,fees,date) values ('{ent1.get()}','{ent5.get()}','{date}') where "
            cur.execute(cmd)
            conn.commit()
            messagebox.showinfo("Sucess","successfully done")
            clear()
        else:
            cmd=f"update fees_record set fees={fees} where reg_no='{reg_no}'"
            #messagebox.showwarning("Warning","Username is already exists !!! try differnt username")
            clear()'''
    


win=Tk()
win.state("zoomed")
win.iconbitmap("D:\\insitute management system\\IMS project\\logouok.ico")
win.title(" U O K ")

image=Image.open("D:\\insitute management system\\IMS project\\Feesss.png")
image=image.resize((1550,850))
tk_image=ImageTk.PhotoImage(image)
image_label=tk.Label(win,image=tk_image)
image_label.place(x=0,y=0)

image6=Image.open("D:\\insitute management system\\IMS project\\DU-Feessss.png")
image6=image6.resize((480,190))
tk_image6=ImageTk.PhotoImage(image6)
image_label=tk.Label(win,bg="black",image=tk_image6)
image_label.place(x=920,y=50)

lbl=Label(win,text="Registration Number",bg="#CDCDCD",fg="black",font=("Calibri (Body)",20,"bold"),width=17,height=1)
lbl.place(x=840,y=300)
entvar1=StringVar()
ent1=Entry(win,width=5,font=("Calibri (Body)",16),textvariable=entvar1)
ent1.place(x=1200,y=306)

lbl=Label(win,text="Full Name",bg="#CDCDCD",fg="black",font=("Calibri (Body)",20,"bold"),width=9,height=1)
lbl.place(x=840,y=370)
entvar2=StringVar()
ent2=Entry(win,width=20,font=("Calibri (Body)",16),textvariable=entvar2)
ent2.place(x=1200,y=374)

lbl=Label(win,text="Mother's Name",bg="#CDCDCD",fg="black",font=("Calibri (Body)",20,"bold"),width=12,height=1)
lbl.place(x=840,y=440)
entvar3=StringVar()
ent3=Entry(win,width=20,font=("Calibri (Body)",16),textvariable=entvar3)
ent3.place(x=1200,y=440)

lbl=Label(win,text="Duration",bg="#CDCDCD",fg="black",font=("Calibri (Body)",20,"bold"),width=7,height=1)
lbl.place(x=840,y=510)
entvar4=StringVar()
ent4=Entry(win,width=20,font=("Calibri (Body)",16),textvariable=entvar4)
ent4.place(x=1200,y=514)

lbl=Label(win,text="Fees",bg="#CDCDCD",fg="black",font=("Calibri (Body)",20,"bold"),width=4,height=1)
lbl.place(x=840,y=580)
entvar5=StringVar()
ent5=Entry(win,width=20,font=("Calibri (Body)",16),textvariable=entvar5)
ent5.place(x=1200,y=584)

btn=Button(win,text="Show record",width=10,height=1,bg="green",fg="white",font=("Calibri (Body)",10,"bold"),command=show)
btn.place(x=1300,y=304)
btn=Button(win,text="Cancel",width=11,height=1,bg="darkred",fg="white",font=("Calibri (Body)",14,"bold"),command=cancel)
btn.place(x=1100,y=688)
btn=Button(win,text="Submit",width=11,height=1,bg="darkred",fg="white",font=("Calibri (Body)",14,"bold"),command=submit)
btn.place(x=930,y=688)
btn=Button(win,text="Clear",width=11,height=1,bg="darkred",fg="white",font=("Calibri (Body)",14,"bold"),command=clear)
btn.place(x=1270,y=688)
win.mainloop()
