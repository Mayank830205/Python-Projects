from tkinter import *
from tkinter import ttk,messagebox
import tkinter as tk
import os
from PIL import Image,ImageTk
import pymysql as sql


'''def pre():
    win.destroy()
    os.system("python mycart.py")
   ''' 

def db_connect():
    conn=sql.connect(host='localhost',port=3306,user='root',password='',database='cloth')
    cur=conn.cursor()
    return conn,cur

    
def fun():
    a=ent1.get()
    b=ent2.get()
    c=ent3.get()
    d=ent4.get()
    #d=Eent.get()
    if (a=="") or (b=="") or (c=="") or (d=="") :
        messagebox.showwarning("Warning","Please provide a valid input!!!")
    else:
        cmd=f"insert into feedack(Full_name ,Last_name , Country ,Subject ) values('{ent1.get()}', '{ent2.get()}','{ent3.get()}','{ent4.get()}')"
        conn,cur=db_connect()      
        cur.execute(cmd)
        conn.commit()
        messagebox.showinfo("Send","Send Successfully")
        win.destroy()

 

win=Tk()
win.config(bg="skyblue")
win.state("zoomed")
#win.minsize(width="1920",height="1080")
#win.maxsize(width="1920",height="1080")



'''def fun():
    a=ent1.get()
    a=ent2.get()
    a=ent3.get()
    a=ent4.get()
    if a=="":
        messagebox.showerror("empty","Please fill the Details")
    messagebox.showinfo("Success","Thank you for feedback")
    win.pack_propagate()
   ''' 


lab=Label(win,text="",width=17,height=10,fg="#FFFEFE", font=("bold",30),bg="black")
lab.place(x=450,y=0)

lab=Label(win,text="Send Feedback",width=15,fg="#FFFEFE", font=("bold",20),bg="black")
lab.place(x=530,y=10)


lab=Label(win,text="First Name:",width=9,fg="#FFFEFE",font=("bold",12) ,bg="black")
lab.place(x=500,y=80)
ent1=Entry(win,width=35,fg="black",font=("bold",11))
ent1.place(x=500,y=110)


lab=Label(win,text="Last Name:",width=9,fg="#FFFEFE",font=("bold",12),bg="black")
lab.place(x=500,y=150)
ent2=Entry(win,width=35,fg="black",font=("bold",11))
ent2.place(x=500,y=180)


lab=Label(win,text="Country:",width=6,fg="#FFFEFE",font=("bold",12),bg="black")
lab.place(x=500,y=220)
ent3=Entry(win,width=35,fg="black",font=("bold",11))
ent3.place(x=500,y=250)


lab=Label(win,text="Subject:",width=6,fg="#FFFEFE",font=("bold",12),bg="black")
lab.place(x=500,y=300)
ent4=Entry(win,width=14,font=("corbel light",29),fg="black")
ent4.place(x=500,y=330)


btn=Button(win,text="Submit",width=30,height=1,fg="black",font=("bold",15),bg="#62DE3C",command=fun)
btn.place(x=470,y=400)

lab=Label(win,text="",width=50,height=4,fg="#FFFEFE", font=("bold",33),bg="black")
lab.place(x=0,y=470)

lab=Label(win,text="Contact Us",width=9,fg="#FFFFFF", font=("bold",20),bg="#000000")
lab.place(x=50,y=490)
lab=Label(win,text="Useful Links",width=10,fg="#FFFFFF", font=("bold",20),bg="#000000")
lab.place(x=480,y=490)
lab=Label(win,text="Payment Options",width=13,fg="#FFFFFF", font=("bold",20),bg="#000000")
lab.place(x=880,y=490)

lab=Label(win,text="Email:ClothesShop19gmail.com",width=25,fg="#FFFFFF", font=("bold",10),bg="#000000")
lab.place(x=5,y=520)
lab=Label(win,text="Phone: +91 697584955",width=19,fg="#FFFFFF", font=("bold",10),bg="#000000")
lab.place(x=5,y=550)
lab=Label(win,text="Address: Mhaveer nagar vistar yojna 1-H-7 first floor\n mai vist buldding",width=42,fg="#FFFFFF", font=("bold",10),bg="#000000")
lab.place(x=0,y=580)
lab=Label(win,text="beside of shiv jyoti in front of dot code edification",width=39,fg="#FFFFFF", font=("bold",10),bg="#000000")
lab.place(x=0,y=635)


lab=Label(win,text="About Us",width=7,fg="#FFFFFF", font=("bold",10),bg="#000000")
lab.place(x=480,y=520)
lab=Label(win,text="Privacy Policy",width=11,fg="#FFFFFF", font=("bold",10),bg="#000000")
lab.place(x=480,y=555)
lab=Label(win,text="Terms of Service",width=13,fg="#FFFFFF", font=("bold",10),bg="#000000")
lab.place(x=480,y=590)
lab=Label(win,text="FAQs",width=4,fg="#FFFFFF", font=("bold",10),bg="#000000")
lab.place(x=490,y=625)

file=PhotoImage(file="img23.png")
lab=Label(win,image=file)
lab.place(x=950,y=540)

file1=PhotoImage(file="img24.png")
lab1=Label(win,image=file1)
lab1.place(x=880,y=540)

file2=PhotoImage(file="imf4.png")
lab2=Label(win,image=file2)
lab2.place(x=1000,y=540)

file3=PhotoImage(file="img25.png")
lab3=Label(win,image=file3)
lab3.place(x=1050,y=540)

win.mainloop()