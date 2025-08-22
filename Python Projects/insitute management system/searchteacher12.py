from tkinter import *
import tkinter as tk
from PIL import Image,ImageTk
from tkinter import ttk
from tkinter import messagebox
import pymysql as sql
import os
win=Tk()
win.state("zoomed")
win.config(bg="#DEDEDE")
win.iconbitmap("D:\\insitute management system\\IMS project\\logouok.ico")
win.title(" U O K ")

def db_connect():
    conn= sql.connect(host='localhost',user='root',password='',port=3306,database='institute__management__system')
    cur=conn.cursor()
    return conn,cur

def clear():
    entvar.set("")

def show():
    registration_no=ent.get()
    if registration_no=="":
        messagebox.showwarning("Warning","please fill all fields")
    else:
        cmd=f"select * from teacher_record where reg_no='{registration_no}'"
        conn,cur=db_connect()
        data=cur.execute(cmd)
        employe = cur.fetchall()      
        conn.commit()
        if data:
            for i in employe:
                tree.insert('','end',value=(i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[8]))
            clear()
        else:
            messagebox.showwarning("Warning","No record found")

def cancel():
    win.destroy()
    os.system("python mainpage.py")

image=Image.open("D:\\insitute management system\\IMS project\\pexelsssteacher.png")
image=image.resize((1530,800))
tk_image=ImageTk.PhotoImage(image)
image_label=tk.Label(win,image=tk_image)
image_label.pack()

lbl=Label(win,text="Search Teacher",bg="#00C9FB",fg="white",font=("Bodoni MT black",50,"bold","underline"),width=36)
lbl.place(x=0,y=50)

lbl=Label(win,text="Registration Number",bg="#00C9FB",fg="black",font=("Calibri (Body)",26,"bold"),width=17)
lbl.place(x=20,y=200)
entvar=StringVar()
ent=Entry(win,width=15,font=("Calibri (Body)",20),textvariable=entvar)
ent.place(x=420,y=208)

image6=Image.open("D:\\insitute management system\\IMS project\\imagesaearchhh.png")
image6=image6.resize((80,80))
tk_image6=ImageTk.PhotoImage(image6)
image_label=tk.Label(win,bg="#63605D",image=tk_image6)
image_label.place(x=350,y=50)

image5=Image.open("D:\\insitute management system\\IMS project\\imagesaearchhh.png")
image5=image5.resize((80,80))
tk_image5=ImageTk.PhotoImage(image5)
image_label=tk.Label(win,bg="#63605D",image=tk_image5)
image_label.place(x=1170,y=50)

btn=Button(win,text="Show Details",width=10,bg="darkred",fg="white",font=("Calibri (Body)",14,"bold"),command=show)
btn.place(x=720,y=207)
btn=Button(win,text="Cancel",width=10,bg="darkred",fg="white",font=("Calibri (Body)",14,"bold"),command=cancel)
btn.place(x=900,y=207)

style=ttk.Style()
style.theme_use("default")
style.configure("Treeview",fieldbackground="skyblue",foreground="black",rowheight=52)
style.configure("Treeview.Heading",background="darkred",foreground="white",font=("Arial",13,"bold"),padding=(5,5))

tree=ttk.Treeview(win,columns=("1","2","3","4","5","6","7","8","9"),show="headings",height=8)
tree.place(x=42,y=350)

tree.heading("1",text="Reg.No.")
tree.heading("2",text="Name")
tree.heading("3",text="Gender")
tree.heading("4",text="DOB")
tree.heading("5",text="Mobileno.")
tree.heading("6",text="Emailno.")
tree.heading("7",text="fieldname")
tree.heading("8",text="Expreience")
tree.heading("9",text="Address")

tree.column("1",width=70,anchor="center")
tree.column("2",width=80,anchor="center")
tree.column("3",width=70,anchor="center")
tree.column("4",width=90,anchor="center")
tree.column("5",width=90,anchor="center")
tree.column("6",width=100,anchor="center")
tree.column("7",width=100,anchor="center")
tree.column("8",width=100,anchor="center")
tree.column("9",width=100,anchor="center")

win.mainloop()