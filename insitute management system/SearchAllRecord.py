from tkinter import *
from PIL import Image,ImageTk
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import pymysql as sql
import os
def db_connect():
    conn= sql.connect(host='localhost',user='root',password='',port=3306,database='institute__management__system')
    cur=conn.cursor()
    return conn,cur

def show():
    cmd=f"select * from student_record"
    conn,cur=db_connect()
    cur.execute(cmd)
    rows=list(cur.fetchall())
    treeview=ttk.Treeview(columns=("Reg. No","Name","Father Name","Mother Name","Gender","DOB","Contact","Email","Course","Duration","Address"),show='headings',height=10)
    column=["Reg. No","Name","Father Name","Mother Name","Gender","DOB","Contact","Email","Course","Duration","Address"]
    for i in range(0,11):
        treeview.column(f"# {i+1}",width=139,anchor=CENTER)
        treeview.heading(column[i],text=column[i])
    for j in range(0,len(rows)):
        treeview.insert('','end',values=rows[j])
    treeview.place(x=3,y=140)

def cancel():
    win.destroy()
    os.system(" python mainpage.py")

win=Tk()
win.state('zoomed')
win.title(" U O K ")
win.geometry("1650x784")
win.iconbitmap("D:\\insitute management system\\IMS project\\logouok.ico")

image=Image.open("D:\\insitute management system\\IMS project\\croud.png")
image=image.resize((1530,790))
tk_image=ImageTk.PhotoImage(image)
image_label=tk.Label(win,image=tk_image)
image_label.pack()

lbl=Label(win,text="Search All Student Records",fg="white",font=("Rockwell Extra Bold",36),bg="blue",width=22,height=0)
lbl.place(x=400,y=30)
lbl=Label(win,bg="lightblue",width=220,height=19)
lbl.place(x=2,y=130)

btn=Button(win,text="Cancel",bg="black",fg="white",font=("Rockwell Extra Bold",14),width=18,command=cancel)
btn.place(x=670,y=375)
show()
win.mainloop()