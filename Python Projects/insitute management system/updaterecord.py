from tkinter import *
from PIL import Image,ImageTk
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import pymysql as sql
import os
from functools import reduce

def cancel():
    win.destroy()
    os.system("python mainpage.py")
    
def db_connect():
    conn= sql.connect(host='localhost',user='root',password='',port=3306,database='institute__management__system')
    cur=conn.cursor()
    return conn,cur
def update():
    reg_no=ent.get()
    field=var.get()
    new=ent1.get()

    if reg_no=="" or field=="" or new=="":
        messagebox.showwarning("Warning","Please fill all fields!!!")
    else:
        cmd=f"update student_record set {var.get()}='{new}' where reg_no='{reg_no}'"
        conn,cur=db_connect()
        data=cur.execute(cmd)
        conn.commit()
        messagebox.showinfo("Update record","Employee record is successfully Updated")
        clear()
        reg_no_set=list(reduce(lambda x,y:x+y,data))
        if reg_no not in reg_no_set:
            messagebox.showwarning("warning","Emp_id is not exists")
            
def clear():
    entvar.set("")

win=Tk()
win.state('zoomed')
win.title(" U O K ")
win.geometry("1650x784")
win.iconbitmap("D:\\insitute management system\\IMS project\\logouok.ico")

image=Image.open("D:\\insitute management system\\IMS project\\imagesupdatebg.png")
image=image.resize((1530,800))
tk_image=ImageTk.PhotoImage(image)
image_label=tk.Label(win,image=tk_image)
image_label.pack()

lbl=Label(win,text="Registration Number",bg="#01BBEA",fg="black",font=("Calibri (Body)",33,"bold"),width=16,height=1)
lbl.place(x=130,y=170)
ent=Entry(win,width=4,font=("Calibri (Body)",23))
ent.place(x=640,y=173)

lbl=Label(win,text="Which field in you want to update",bg="#02B3E5",fg="black",font=("Calibri (Body)",33,"bold"),width=26,height=1)
lbl.place(x=50,y=290)
var=StringVar()
com=ttk.Combobox(win,width=60,height=11,textvariable=var)
com['state']='readonly'
com['values']=('Name','Father_Name','Mother_Name','Gender','DOB','Mobile_No.','Email','Course','Duration','Address')
com.place(x=200,y=350)

lbl=Label(win,text="if you select DOB column so follow this format - YYYY-MM-DD",bg="#0289C1",fg="black",font=("Calibri (Body)",10,"bold"),width=49,height=1)
lbl.place(x=422,y=580)
lbl=Label(win,text="New Update",bg="#02A5DC",fg="black",font=("Calibri (Body)",30,"bold"),width=10,height=1)
lbl.place(x=100,y=540)
entvar=StringVar()
ent1=Entry(win,width=15,font=("Calibri (Body)",18),textvariable=entvar)
ent1.place(x=430,y=547)

btn=Button(win,text="Update",font=("Arial",18,"bold"),fg="purple",width=13,command=update)
btn.place(x=180,y=650)
btn=Button(win,text="Cancel",font=("Arial",18,"bold"),fg="purple",width=13,command=cancel)
btn.place(x=440,y=650)
win.mainloop()