from tkinter import *
import tkinter as tk
from PIL import Image,ImageTk
from tkcalendar import DateEntry
from tkinter import messagebox
from tkinter import ttk
import pymysql as sql
import os
def db_connect():  
    conn= sql.connect(host='localhost',user='root',password='',port=3306,database='institute__management__system')
    cur=conn.cursor()
    return conn,cur

def admission():
    reg_no=ent.get()
    name=ent1.get()
    if var.get()==0:
        gender="Male"
    if var.get()==1:
        gender="Female"
    dob=date2.get()
    mobile=ent3.get()
    email=ent4.get()
    feild=ent5.get()
    duration=ent6.get()
    address=ent7.get()
    
    if reg_no=="" or name=="" or gender=="" or dob=="" or mobile=="" or email=="" or feild=="" or duration=="" or address=="":
        messagebox.showwarning("Warning","Please provide a valid input!!!")
   
    else:
        conn,cur=db_connect()
        cmd=f"insert into teacher_record (reg_no,name,gender,dob,mobile_no,email,feild,duration,address) values ('{reg_no}','{name}','{gender}','{dob}',{mobile},'{email}','{feild}','{duration}','{address}')"
        cur.execute(cmd)     # query ko excute krne k liye lhate h     # fatchall() function se database se pura data aata h  
        conn.commit()        # database me changes ko permanently save kr deta h, dubara cancel krke nhi clana pdta 
        messagebox.showinfo("susscess","Submited")
        clear()
        
def clear():
    entvar.set("")
    entvar1.set("")
    entvar2.set("")
    entvar3.set("")    
    entvar4.set("")
    entvar5.set("")
    entvar6.set("")

def cancel():
    win.destroy()
    os.system("python mainpage.py")

win=Tk()
win.state("zoomed")
win.iconbitmap("D:\\insitute management system\\IMS project\\logouok.ico")
win.title(" U O K ")

image7=Image.open("D:\\insitute management system\\IMS project\\imagesearchtee.png")
image7=image7.resize((1550,800))
tk_image7=ImageTk.PhotoImage(image7)
image_label=tk.Label(win,image=tk_image7)
image_label.place(x=1,y=1)

lbl=Label(win,text="  Basic Information Of Teacher  ",bg="yellow",fg="red",font=("Bodoni MT black",40,"bold","underline"))
lbl.place(x=650,y=40)

lbl=Label(win,text="Register no.",bg="#89FFFF",fg="black",font=("Calibri (Body)",16,"bold"),width=9,height=1)
lbl.place(x=670,y=135)
entvar=StringVar()
ent=Entry(win,width=3,font=("Calibri (Body)",16),textvariable=entvar)
ent.place(x=820,y=136)

lbl=Label(win,text="Full Name",bg="#89FFFF",fg="black",font=("Calibri (Body)",20,"bold"),width=8,height=1)
lbl.place(x=670,y=220)
entvar1=StringVar()
ent1=Entry(win,width=26,font=("Calibri (Body)",13),textvariable=entvar1)
ent1.place(x=850,y=223)

lbl=Label(win,text="Gender",bg="#89FFFF",fg="black",font=("Calibri (Body)",20,"bold"),width=6,height=1)
lbl.place(x=670,y=290)
var=IntVar()
radio=Radiobutton(win,font=(1),text="Male",value="0",variable=var)
radio.place(x=860,y=287)
radio=Radiobutton(win,font=(1),text="Female",value="1",variable=var)
radio.place(x=970,y=287)

lbl=Label(win,text="Date Of Birth",bg="#89FFFF",fg="black",font=("Calibri (Body)",18,"bold"),width=10,height=1)
lbl.place(x=670,y=367)
date2=DateEntry(win,date_pattern="yyyy-mm-dd",width=24,font=("Calibri (Body)",13))
date2.place(x=850,y=367)

lbl=Label(win,text="Mobile No.",bg="#89FFFF",fg="black",font=("Calibri (Body)",18,"bold"),width=8,height=1)
lbl.place(x=670,y=440)
entvar2=StringVar()
ent3=Entry(win,width=26,font=("Calibri (Body)",13),textvariable=entvar2)
ent3.place(x=850,y=440)

lbl=Label(win,text="Email ID",bg="#89FFFF",fg="black",font=("Calibri (Body)",20,"bold"),width=7,height=1)
lbl.place(x=670,y=520)
entvar3=StringVar()
ent4=Entry(win,width=26,font=("Calibri (Body)",13),textvariable=entvar3)
ent4.place(x=850,y=520)

lbl=Label(win,text="Field Name",bg="#89FFFF",fg="black",font=("Calibri (Body)",18,"bold"),width=9,height=1)
lbl.place(x=1150,y=220)
entvar4=StringVar()
ent5=Entry(win,width=20,font=("Calibri (Body)",13),textvariable=entvar4)
ent5.place(x=1330,y=224)

lbl=Label(win,text="Expreience",bg="#89FFFF",fg="black",font=("Calibri (Body)",17,"bold"),width=9,height=1)
lbl.place(x=1150,y=290)
entvar5=StringVar()
ent6=Entry(win,width=20,font=("Calibri (Body)",13),textvariable=entvar5)
ent6.place(x=1330,y=294)

lbl=Label(win,text="Address",bg="#89FFFF",fg="black",font=("Calibri (Body)",19,"bold"),width=7,height=1)
lbl.place(x=1150,y=360)
entvar6=StringVar()
ent7=Entry(win,width=20,font=("Calibri (Body)",13),textvariable=entvar6)
ent7.place(x=1330,y=360)

btn=Button(win,text="Submit",width=10,height=1,bg="white",fg="#3A1B45",font=("Cooper Black",22,"bold"),command=admission)
btn.place(x=830,y=650)

btn=Button(win,text="Cancel",width=10,height=1,bg="white",fg="#3A1B45",font=("Cooper Black",22,"bold"),command=cancel)
btn.place(x=1100,y=650)
win.mainloop()