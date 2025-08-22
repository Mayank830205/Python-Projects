from tkinter import *
import tkinter as tk
from PIL import Image,ImageTk
from tkinter import ttk
from tkinter import messagebox
import os
import pymysql as sql

win=Tk()
win.state("zoomed")
win.config(bg="#DEDEDE")
win.iconbitmap("D:\\insitute management system\\IMS project\\logouok.ico")
win.title(" U O K ")

def clear():
    entvar.set("")

def db_connect():
    conn= sql.connect(host='localhost',user='root',password='',port=3306,database='institute__management__system')
    cur=conn.cursor()
    return conn,cur

def indistudent():
    registration_no=ent.get()
    if registration_no=="":
        messagebox.showwarning("Warning","please fill all fields")
    else:
        cmd=f"select * from student_record where reg_no='{registration_no}'"
        conn,cur=db_connect()
        data=cur.execute(cmd)
        employe = cur.fetchall()      
        conn.commit()
        if data:
            for i in employe:
                tree.insert('','end',value=(i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[8],i[9],i[10]))
            clear()
        else:
            messagebox.showwarning("Warning","No record found")

def cancel():
    win.destroy()
    os.system("python mainpage.py")

image=Image.open("D:\\insitute management system\\IMS project\\searchhhbg.png")
image=image.resize((1550,800))
tk_image=ImageTk.PhotoImage(image)
image_label=tk.Label(win,bg="#DEDEDE",image=tk_image)
image_label.place(x=0,y=0)

lbl=Label(win,text="Search Individual Students details",bg="#D3F0FA",fg="darkblue",font=("Bodoni MT black",40,"bold","underline"))
lbl.place(x=350,y=30)

image6=Image.open("D:\\insitute management system\\IMS project\\searchpppppp.png")
image6=image6.resize((240,300))
tk_image6=ImageTk.PhotoImage(image6)
image_label=tk.Label(win,bg="#D3F0FA",image=tk_image6)
image_label.place(x=1,y=1)

lbl=Label(win,text="Registration Number",bg="#D3F0FA",fg="black",font=("Calibri (Body)",22,"bold"),width=17,height=1)
lbl.place(x=470,y=120)
entvar=StringVar()
ent=Entry(win,width=20,font=("Calibri (Body)",20),textvariable=entvar)
ent.place(x=800,y=123)

btn=Button(win,text="Show Details",width=10,height=1,bg="blue",fg="white",font=("Calibri (Body)",18,"bold"),command=indistudent)
btn.place(x=700,y=190)

style=ttk.Style()
style.theme_use("default")
style.configure("Treeview",fieldbackground="pink",foreground="black",rowheight=55)
style.configure("Treeview.Heading",background="lightgreen",foreground="black",font=("Arial",13,"bold"),padding=(3,7))

tree=ttk.Treeview(win,columns=("1","2","3","4","5","6","7","8","9","10","11"),show="headings",height=8)
tree.place(x=2,y=320)

tree.heading("1",text="Reg.No.")
tree.heading("2",text="Name")
tree.heading("3",text="Father Name")
tree.heading("4",text="Mother Name")
tree.heading("5",text="Gender")
tree.heading("6",text="DOB")
tree.heading("7",text="Contact")
tree.heading("8",text="Email ID")
tree.heading("9",text="Course")
tree.heading("10",text="Duration")
tree.heading("11",text="Address")

tree.column("1",width=70,anchor="center")
tree.column("2",width=130,anchor="center")
tree.column("3",width=160,anchor="center")
tree.column("4",width=160,anchor="center")
tree.column("5",width=90,anchor="center")
tree.column("6",width=140,anchor="center")
tree.column("7",width=170,anchor="center")
tree.column("8",width=190,anchor="center")
tree.column("9",width=90,anchor="center")
tree.column("10",width=80,anchor="center")
tree.column("11",width=250,anchor="center")

btn=Button(win,text="Cancel",width=12,bg="red",fg="white",font=("Calibri (Body)",18,"bold"),command=cancel)
btn.place(x=690,y=737)
win.mainloop()