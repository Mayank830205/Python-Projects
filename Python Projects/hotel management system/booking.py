from tkinter import *
from tkinter import ttk,messagebox
import tkinter as tk
import os
from PIL import Image,ImageTk
from tkcalendar import DateEntry
import pymysql as sql

def Home():
    win.destroy()
    os.system("python Home.py")

def db_connect():
    conn=sql.connect(host='localhost',port=3306,user='root',password='',database='hotel')
    cur=conn.cursor()
    return conn,cur

    
def payment():
    a=ent1.get()
    b=ent2.get()
    c=ent3.get()
    d=ent4.get()
    e=ent5.get()
    f=ent6.get()
    g=ent7.get()
    #d=Eent.get()
    if (a=="") or (b=="") or (c=="") or (d=="") or (e=="") or (f=="") or (g=="") :
        messagebox.showwarning("Warning","Please provide a valid input!!!")
    else:
        cmd=f"insert into booking(Full_name ,Email , Phone_no,Aadhar_card,Check_in,Time,Room_no) values('{ent1.get()}', '{ent2.get()}',{ent3.get()},{ent4.get()},'{ent5.get()}','{ent6.get()}','{ent7.get()}')"
        conn,cur=db_connect()      
        cur.execute(cmd)
        conn.commit()
        messagebox.showinfo("Success","book Successfully")
        win.destroy()
        os.system("python payment.py")

 
win=Tk()
win.config(bg="#73FBFD")
win.state("zoomed")





image= Image.open("C:\\Users\\HP\\Desktop\\hotel management system\\img6.jpg")
image = image.resize((1280,680))

tk_image = ImageTk.PhotoImage(image)
image_label = tk.Label(win,image=tk_image)
image_label.pack()

lab=Label(win,text="",width=16,height=8,fg="#000000", font=("bold",50),bg="#FFE9B5")
lab.place(x=519,y=30)

lab=Label(win,text="Hotel Room Booking",width=20,fg="#000000", font=("bold",30),bg="#FFE9B5")
lab.place(x= 580,y=40)

lab=Label(win,text=" Booking for: Hotel_Room ",width=23,fg="#000000", font=("bold",15),bg="#FFE9B5")
lab.place(x=550,y=90)

lab=Label(win,text="Full Name",width=8,fg="#000000",font=("bold",20) ,bg="#FFE9B5")
lab.place(x=530,y=130)
ent1=Entry(win,width=25,font=("bold",21),fg="#000000",bg="#FFE9B5")
ent1.place(x=730,y=130)

lab=Label(win,text="Email",width=4,fg="#000000",font=("bold",20) ,bg="#FFE9B5")
lab.place(x=530,y=190)
ent2=Entry(win,width=25,font=("bold",21),fg="#000000",bg="#FFE9B5")
ent2.place(x=730,y=190)


lab=Label(win,text="Phone N0.",width=8,fg="#000000",font=("bold",20) ,bg="#FFE9B5")
lab.place(x=530,y=250)
ent3=Entry(win,width=25,font=("bold",21),fg="#000000",bg="#FFE9B5")
ent3.place(x=730,y=250)


lab=Label(win,text="Aadhar card no.",width=12,fg="#000000",font=("bold",20) ,bg="#FFE9B5")
lab.place(x=530,y=310)
ent4=Entry(win,width=25,font=("bold",21),fg="#000000",bg="#FFE9B5")
ent4.place(x=730,y=310)

lab=Label(win,text="Chack in",width=7,fg="#000000",font=("bold",20) ,bg="#FFE9B5")
lab.place(x=530,y=370)
ent5=Entry(win,width=25,font=("bold",21),fg="#000000",bg="#FFE9B5")
ent5.place(x=730,y=370)


lab=Label(win,text="Time",width=4,fg="#000000",font=("bold",20) ,bg="#FFE9B5")
lab.place(x=530,y=430)
ent6=Entry(win,width=25,font=("bold",21),fg="#000000",bg="#FFE9B5")
ent6.place(x=730,y=430)

lab=Label(win,text="Room no.",width=7,fg="#000000",font=("bold",20) ,bg="#FFE9B5")
lab.place(x=530,y=490)
ent7=Entry(win,width=25,font=("bold",21),fg="#000000",bg="#FFE9B5")
ent7.place(x=730,y=490)




btn=Button(win,text="Book Room",width=20,height=1,fg="#000000",font=("bold",15),bg="#A1FB8E",command=payment)
btn.place(x=530,y=560)

btn=Button(win,text="Back Home",width=20,height=1,fg="#000000",font=("bold",15),bg="#A1FB8E",command=Home  )
btn.place(x=900,y=560)



win.mainloop()