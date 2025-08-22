from tkinter import *
from PIL import Image,ImageTk
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import pymysql as sql
import os
from functools import reduce

def back():
    win.destroy()
    os.system("python mainpage.py")
    
def db_connect():
    conn= sql.connect(host='localhost',user='root',password='',port=3306,database='institute__management__system')
    cur=conn.cursor()
    return conn,cur

def show():
    regi_no=ent1.get()
    conn,cur=db_connect() 
    cmd=f"select student_record.name,student_record.father_name,student_record.course,fees_record.fees,fees_record.date from student_record inner join fees_record on student_record.reg_no = fees_record.reg_no where student_record.reg_no={regi_no}"
    cur.execute(cmd)
    data=cur.fetchall()
    conn.close()

    student_data=list(reduce(lambda x,y:x+y,data))
    print(student_data)
    lbl2.config(text=student_data[0])
    lbl3.config(text=student_data[1])
    lbl4.config(text=student_data[2])
    amount_lbl.config(text=student_data[3])
    date_lbl.config(text=student_data[4])

def cancel():
    win.destroy()
    os.system("python mainpage.py")

win=Tk()
win.state('zoomed')
win.title(" U O K ")
win.geometry("1650x784")
win.iconbitmap("D:\\insitute management system\\IMS project\\logouok.ico")

image=Image.open("D:\\insitute management system\\IMS project\\Receiptbbbggg.png")
image=image.resize((1530,790))
tk_image=ImageTk.PhotoImage(image)
image_label=tk.Label(win,image=tk_image)
image_label.pack()

image7=Image.open("D:\\insitute management system\\IMS project\\logouok.png")
image7=image7.resize((60,60))
tk_image7=ImageTk.PhotoImage(image7)
image_label=tk.Label(win,image=tk_image7)
image_label.place(x=1200,y=12)

lbl=Label(win,text="University Of Kota",fg="black",bg="white",font=("Rockwell Extra Bold",18),height=2)
lbl.place(x=1270,y=13)
lbl=Label(win,bg="#28313B",height=20,width=90)
lbl.place(x=800,y=205)
lbl=Label(win,text="INSTITUTE",fg="white",bg="#28313B",font=("Gill Sans Ultra Bold",80))
lbl.place(x=820,y=249)
lbl=Label(win,text="final receipt",fg="white",bg="#28313B",font=("Comic Sans MS",58,"bold","underline"))
lbl.place(x=930,y=360)
lbl=Label(win,bg="#3D3D3D",height=40,width=75)
lbl.place(x=98,y=88)
lbl=Label(win,bg="white",height=40,width=75)
lbl.place(x=80,y=70)

image1=Image.open("D:\\insitute management system\\IMS project\\logouok.png")
image1=image1.resize((63,63))
tk_image1=ImageTk.PhotoImage(image1)
image_label=tk.Label(win,bg="black",image=tk_image1)
image_label.place(x=82,y=70)
lbl=Label(win,text="University Of Kota",fg="white",bg="black",font=("Rockwell Extra bold",25),width=18)
lbl.place(x=152,y=72)
lbl=Label(win,text="MBS Marg, near Kabir Circle, Swami Vivekananda Nagar,",fg="black",bg="white",font=("Calibri (Body)",13,"bold"))
lbl.place(x=155,y=120)
lbl=Label(win,text="Kota, Rajasthan 324005",fg="black",bg="white",font=("Calibri (Body)",13,"bold"))
lbl.place(x=280,y=142)

lbl=Label(win,bg="black",font=("Calibri (Body)",20,"bold"),width=30)
lbl.place(x=92,y=186)
lbl=Label(win,text="FEES RECEIPT",fg="black",bg="lightgray",font=("Calibri (Body)",20,"bold"),width=30)
lbl.place(x=84,y=178)
lbl=Label(win,text="___________________________________________________",fg="black",bg="white",font=("bold"),width=47)
lbl.place(x=84,y=350)
lbl=Label(win,text="Regi.No.:",fg="black",bg="white",font=("Calibri (Body)",14,"bold","underline"))
lbl.place(x=90,y=240)
ent1=Entry(win,fg="black",bg="white",font=("Calibri (Body)",13),width=7)
ent1.place(x=180,y=240)

lbl=Label(win,text="Student Name:",fg="black",bg="white",font=("Calibri (Body)",13,"bold","underline"))
lbl.place(x=80,y=274)
lbl2=Label(win,fg="black",bg="white",font=("Calibri (Body)",13))
lbl2.place(x=210,y=274)

lbl=Label(win,text="Father's Name:",fg="black",bg="white",font=("Calibri (Body)",13,"bold","underline"))
lbl.place(x=80,y=310)
lbl3=Label(win,fg="black",bg="white",font=("Calibri (Body)",13))
lbl3.place(x=210,y=310)

lbl=Label(win,text="Course Name:",fg="black",bg="white",font=("Calibri (Body)",13,"bold","underline"))
lbl.place(x=86,y=340)
lbl4=Label(win,fg="black",bg="white",font=("Calibri (Body)",13))
lbl4.place(x=200,y=340)

lbl=Label(win,text="Date:",fg="black",bg="white",font=("Calibri (Body)",15,"bold","underline"))
lbl.place(x=400,y=230)
date_lbl=Label(win,fg="black",bg="white",font=("Calibri (Body)",14),width=13)
date_lbl.place(x=460,y=229)

lbl=Label(win,text="Student's Fees Details                Amount",fg="darkblue",bg="white",font=("Calibri (Body)",17,"bold"),width=36)
lbl.place(x=80,y=380)
amount_lbl=Label(win,fg="black",bg="white",font=("Calibri (Body)",22,"bold"))
amount_lbl.place(x=460,y=440)
lbl=Label(win,bg="black",width=0,height=14)
lbl.place(x=400,y=376)
lbl=Label(win,bg="white",fg="black",text="Total Amount----",width=13,font=("Calibri (Body)",20,"bold"))
lbl.place(x=120,y=440)
lbl=Label(win,bg="black",width=75,height=0)
lbl.place(x=80,y=580)
lbl=Label(win,bg="white",fg="black",text="All above mentioned ammount onec paid are not",width=40,font=("Calibri (Body)",16,"bold"))
lbl.place(x=85,y=605)
lbl=Label(win,bg="white",fg="black",text="refundable in any case whatsever.",width=40,font=("Calibri (Body)",16,"bold"))
lbl.place(x=85,y=630)

btn=Button(win,text="Show record",width=10,height=1,bg="green",fg="white",font=("Calibri (Body)",10,"bold"),command=show)
btn.place(x=280,y=237)
btn=Button(win,text="Back",width=17,height=0,bg="green",fg="white",font=("Calibri (Body)",14,"bold"),command=back)
btn.place(x=240,y=700)
win.mainloop()