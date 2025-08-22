from tkinter import *
import tkinter as tk
from tkinter import ttk
from PIL import Image,ImageTk
from tkcalendar import DateEntry
from tkinter import messagebox
import pymysql as sql
import os                                 # 1 page ke baad dusri file lane k liye 

def db_connect():    # database se connect krne k liye ye pura function likhte h 
    conn= sql.connect(host='localhost',user='root',password='',port=3306,database='institute__management__system')
    cur=conn.cursor()
    return conn,cur

def admission():
    reg_no=ent.get()
    name=ent1.get()
    father=ent2.get()
    mother=ent3.get()
    if var.get()==0:
        gender="Male"
    if var.get()==1:
        gender="Female"
    dob=date4.get()
    mobile=ent5.get()
    email=ent6.get()
    course=ent7.get()
    duration=ent8.get()
    address=ent9.get()
    
    if reg_no=="" or name=="" or father=="" or mother=="" or gender=="" or dob=="" or mobile=="" or email=="" or course=="" or duration=="" or address=="":
        messagebox.showwarning("Warning","Please provide a valid input!!!")
    else:
        conn,cur=db_connect()
        cmd=f"insert into student_record (reg_no,name,father_name,mother_name,gender,dob,mobile_no,email,course,duration,address) values ('{reg_no}','{name}','{father}','{mother}','{gender}','{dob}','{mobile}','{email}','{course}','{duration}','{address}')"
        cur.execute(cmd)     # query ko excute krne k liye lhate h     # fatchall() function se database se pura data aata h  
        conn.commit()        # database me changes ko permanently save kr deta h, dubara cancel krke nhi clana pdta 
        messagebox.showinfo("susscess","Submited")
        clear()
        if reg_no=={ent.get()}:
            messagebox.showwarning("Warning","Please change the register number!!!")
def clear():
    entvar.set("")
    entvar1.set("")
    entvar2.set("")
    entvar3.set("")    
    entvar5.set("")
    entvar6.set("")
    entvar7.set("")
    entvar8.set("")
    entvar9.set("")
    
def cancel():
    win.destroy()
    os.system("python mainpage.py")

win=Tk()
win.state("zoomed")
win.iconbitmap("D:\\insitute management system\\IMS project\\logouok.ico")
win.title(" U O K ")

image=Image.open("D:\\insitute management system\\IMS project\\Admissionbg.png")
image=image.resize((1535,800))
tk_image=ImageTk.PhotoImage(image)
image_label=tk.Label(win,image=tk_image)
image_label.place(x=0,y=0)

lbl=Label(win,text="A D M I S S I O N S",bg="#A35B1D",fg="white",width=30,font=("Bodoni MT black",60,"bold","underline"))
lbl.place(x=0,y=5)

image2=Image.open("D:\\insitute management system\\IMS project\\Admissionn.png")
image2=image2.resize((190,94))
tk_image2=ImageTk.PhotoImage(image2)
image_label=tk.Label(win,bg="#A35B1D",image=tk_image2)
image_label.place(x=190,y=5)

lbl=Label(win,bg="#C0DBEA",width=50,height=22)
lbl.place(x=1150,y=432)
image1=Image.open("D:\\insitute management system\\IMS project\\login4.png")
image1=image1.resize((330,320))
tk_image1=ImageTk.PhotoImage(image1)
image_label=tk.Label(win,bg="black",image=tk_image1)
image_label.place(x=1160,y=440)

lbl=Label(win,text="Register No-",bg="black",fg="white",font=("Calibri (Body)",18,"bold"),width=12,height=1)
lbl.place(x=160,y=120)
entvar=StringVar()
ent=Entry(win,width=17,font=("Calibri (Body)",16),textvariable=entvar)
ent.place(x=350,y=120)

lbl=Label(win,text="Full Name",bg="#593210",fg="white",font=("Calibri (Body)",18,"bold"),width=12,height=1)
lbl.place(x=160,y=200)
entvar1=StringVar()
ent1=Entry(win,width=17,font=("Calibri (Body)",16),textvariable=entvar1)
ent1.place(x=430,y=200)

lbl=Label(win,text="Father's Name",bg="#593210",fg="white",font=("Calibri (Body)",18,"bold"),width=12,height=1)
lbl.place(x=160,y=280)
entvar2=StringVar()
ent2=Entry(win,width=17,font=("Calibri (Body)",16),textvariable=entvar2)
ent2.place(x=430,y=280)

lbl=Label(win,text="Mother's Name",bg="#593210",fg="white",font=("Calibri (Body)",18,"bold"),width=12,height=1)
lbl.place(x=160,y=360)
entvar3=StringVar()
ent3=Entry(win,width=17,font=("Calibri (Body)",16),textvariable=entvar3)
ent3.place(x=430,y=360)
    
lbl=Label(win,text="Gender",bg="#593210",fg="white",font=("Calibri (Body)",18,"bold"),width=12,height=1)
lbl.place(x=160,y=440)
var=IntVar()
radio1=Radiobutton(win,text="Male",font=(0),value="0",variable=var)
radio1.place(x=440,y=440)
radio2=Radiobutton(win,text="Female",font=(0),value="1",variable=var)
radio2.place(x=540,y=440)

lbl=Label(win,text="Date Of Birth",bg="#593210",fg="white",font=("Calibri (Body)",18,"bold"),width=12,height=1)
lbl.place(x=160,y=520)
date4=DateEntry(win,date_pattern="yyyy-mm-dd",width=20,font=("Calibri (Body)",13))
date4.place(x=430,y=520)

lbl=Label(win,text="Mobile No.",bg="#593210",fg="white",font=("Calibri (Body)",18,"bold"),width=12,height=1)
lbl.place(x=160,y=600)
entvar5=StringVar()
ent5=Entry(win,width=17,font=("Calibri (Body)",16),textvariable=entvar5)
ent5.place(x=430,y=600)

lbl=Label(win,text="Email ID",bg="#593210",fg="white",font=("Calibri (Body)",18,"bold"),width=12,height=1)
lbl.place(x=160,y=680)
entvar6=StringVar()
ent6=Entry(win,width=17,font=("Calibri (Body)",16),textvariable=entvar6)
ent6.place(x=430,y=680)

lbl=Label(win,text="Course",bg="#593210",fg="white",font=("Calibri (Body)",18,"bold"),width=12,height=1)
lbl.place(x=840,y=200)
entvar7=StringVar()
ent7=Entry(win,width=17,font=("Calibri (Body)",16),textvariable=entvar7)
ent7.place(x=1100,y=200)

lbl=Label(win,text="Duration(year)",bg="#593210",fg="white",font=("Calibri (Body)",18,"bold"),width=12,height=1)
lbl.place(x=840,y=280)
entvar8=StringVar()
ent8=Entry(win,width=17,font=("Calibri (Body)",16),textvariable=entvar8)
ent8.place(x=1100,y=280)

lbl=Label(win,text="Address",bg="#593210",fg="white",font=("Calibri (Body)",18,"bold"),width=12,height=1)
lbl.place(x=840,y=360)
entvar9=StringVar()
ent9=Entry(win,width=17,font=("Calibri (Body)",16),textvariable=entvar9)
ent9.place(x=1100,y=360)

btn=Button(win,text="Submit",width=7,bg="black",fg="white",font=("Calibri (Body)",17,"bold"),command=admission)
btn.place(x=550,y=730)

btn=Button(win,text="Cancel",width=7,bg="black",fg="white",font=("Calibri (Body)",17,"bold"),command=cancel)
btn.place(x=800,y=730)
win.mainloop()