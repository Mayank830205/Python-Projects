from tkinter import *
from tkinter import ttk,messagebox
import tkinter as tk
import os
from PIL import Image,ImageTk
import pymysql as sql

def back():
    win.destroy()
    os.system("python Home.py")

def db_connect():
    conn=sql.connect(host='localhost',port=3306,user='root',password='',database='hotel')
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
        cmd=f"insert into feedback(Full_name ,Last_name , Country ,Subject ) values('{ent1.get()}', '{ent2.get()}','{ent3.get()}','{ent4.get()}')"
        conn,cur=db_connect()      
        cur.execute(cmd)
        conn.commit()
        messagebox.showinfo("Success","Thank you for feedback")
        win.destroy()
        os.system("python Home.py")
        


win=Tk()
win.config(bg="#FFFFFF")
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

image= Image.open("C:\\Users\\HP\\Desktop\\hotel management system\\img3.jpg")
image = image.resize((1280,700))

tk_image = ImageTk.PhotoImage(image)

image_label = tk.Label(win,image=tk_image)
image_label.pack()


lab=Label(win,text="",width=17,height=9,fg="#FFFEFE", font=("bold",52),bg="#000961")
lab.place(x=300,y=0)

lab=Label(win,text="Send Feedback",width=15,fg="#FFFEFE", font=("bold",25),bg="#000961")
lab.place(x=490,y=10)


lab=Label(win,text="First Name:",width=9,fg="#FFFEFE",font=("bold",20) ,bg="#000961")
lab.place(x=350,y=100)
ent1=Entry(win,width=35,font=("bold",21),fg="black")
ent1.place(x=350,y=150)


lab=Label(win,text="Last Name:",width=9,fg="#FFFEFE",font=("bold",20),bg="#000961")
lab.place(x=350,y=200)
ent2=Entry(win,width=35,font=("bold",21),fg="black")
ent2.place(x=350,y=250)


lab=Label(win,text="Country:",width=6,fg="#FFFEFE",font=("bold",20),bg="#000961")
lab.place(x=350,y=300)
ent3=Entry(win,width=35,font=("bold",21),fg="black")
ent3.place(x=350,y=350)


lab=Label(win,text="Customer Review :",width=14,fg="#FFFEFE",font=("bold",20),bg="#000961")
lab.place(x=350,y=400)
ent4=Entry(win,width=30,font=("corbel light",28),fg="black")
ent4.place(x=350,y=450)


btn=Button(win,text="Submit",width=35,height=1,fg="black",font=("bold",20),bg="#62DE3C",command=fun)
btn.place(x=350,y=550)

btn=Button(win,text="Back >>",width=10,height=1,fg="white",bg="blue",font=("bold",20),command=back)
btn.place(x=1020,y=570)

'''
lab=Label(win,text="",width=50,height=4,fg="#FFFEFE", font=("bold",50),bg="black")
lab.place(x=0,y=730)

lab=Label(win,text="Contact Us",width=9,fg="#FFFFFF", font=("bold",30),bg="#000000")
lab.place(x=180,y=750)
lab=Label(win,text="Useful Links",width=10,fg="#FFFFFF", font=("bold",30),bg="#000000")
lab.place(x=780,y=750)
lab=Label(win,text="Payment Options",width=13,fg="#FFFFFF", font=("bold",30),bg="#000000")
lab.place(x=1280,y=750)

lab=Label(win,text="Email:Theritzindia19gmail.com",width=24,fg="#FFFFFF", font=("bold",15),bg="#000000")
lab.place(x=180,y=820)
lab=Label(win,text="Phone: +91 697584955",width=19,fg="#FFFFFF", font=("bold",15),bg="#000000")
lab.place(x=180,y=850)
lab=Label(win,text="Address: Mhaveer nagar vistar yojna 1-H-7 first floor\n mai vist buldding",width=42,fg="#FFFFFF", font=("bold",15),bg="#000000")
lab.place(x=180,y=880)
lab=Label(win,text="beside of shiv jyoti in front of dot code edification",width=39,fg="#FFFFFF", font=("bold",15),bg="#000000")
lab.place(x=180,y=935)


lab=Label(win,text="About Us",width=7,fg="#FFFFFF", font=("bold",15),bg="#000000")
lab.place(x=780,y=820)
lab=Label(win,text="Privacy Policy",width=11,fg="#FFFFFF", font=("bold",15),bg="#000000")
lab.place(x=780,y=855)
lab=Label(win,text="Terms of Service",width=13,fg="#FFFFFF", font=("bold",15),bg="#000000")
lab.place(x=780,y=890)
lab=Label(win,text="FAQs",width=4,fg="#FFFFFF", font=("bold",15),bg="#000000")
lab.place(x=780,y=925)

file=PhotoImage(file="img23.png")
lab=Label(win,image=file)
lab.place(x=1350,y=820)

file1=PhotoImage(file="img24.png")
lab1=Label(win,image=file1)
lab1.place(x=1280,y=820)

file2=PhotoImage(file="imf4.png")
lab2=Label(win,image=file2)
lab2.place(x=1420,y=820)

file3=PhotoImage(file="img25.png")
lab3=Label(win,image=file3)
lab3.place(x=1490,y=820)
'''
win.mainloop()