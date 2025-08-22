from tkinter import *
from tkinter import ttk,messagebox
import tkinter as tk
import os
from PIL import Image,ImageTk
from tkcalendar import DateEntry
import pymysql as sql



def db_connect():
    conn=sql.connect(host='localhost',port=3306,user='root',password='',database='cloth')
    cur=conn.cursor()
    return conn,cur

    
def payment():
    a=ent1.get()
    b=ent2.get()
    c=ent3.get()
    d=ent5.get()
    if (a=="") or (b=="") or (c=="") or (d=="") :
        messagebox.showwarning("Warning","Please provide a valid input!!!")
    else:
        cmd=f"insert into mycart(Full_name ,Email , Phone_no,Address) values('{ent1.get()}', '{ent2.get()}',{ent3.get()},'{ent5.get()}')"
        conn,cur=db_connect()      
        cur.execute(cmd)
        conn.commit()
        messagebox.showinfo("Send","Send Successfully")
        win.destroy()

 
win=Tk()
win.config(bg="#73FBFD")
win.state("zoomed")

def Home():
    win.destroy()
    os.system("python Home.py")


image= Image.open("images//img 12.webp")
image = image.resize((1270,720))

tk_image = ImageTk.PhotoImage(image)
image_label = tk.Label(win,image=tk_image)
image_label.pack()

    
    


lab=Label(win,text="",width=20,height=7,fg="#000000", font=("bold",50),bg="#FAAFC9")
lab.place(x=500,y=10)

lab=Label(win,text="Customer Details",width=20,fg="#000000", font=("bold",30),bg="#FAAFC9")
lab.place(x=600,y=30)

lab=Label(win,text=" Order for: {{Clothes}}",width=20,fg="#000000", font=("bold",20),bg="#FAAFC9")
lab.place(x=560,y=110)

lab=Label(win,text="Full Name",width=8,fg="#000000",font=("bold",20) ,bg="#FAAFC9")
lab.place(x=600,y=190)
ent1=Entry(win,width=25,font=("bold",21),fg="#000000",bg="#F0F0F0")
ent1.place(x=750,y=190)

lab=Label(win,text="Email",width=4,fg="#000000",font=("bold",20) ,bg="#FAAFC9")
lab.place(x=600,y=250)
ent2=Entry(win,width=25,font=("bold",21),fg="#000000",bg="#F0F0F0")
ent2.place(x=750,y=250)


lab=Label(win,text="Phone N0.",width=8,fg="#000000",font=("bold",20) ,bg="#FAAFC9")
lab.place(x=600,y=310)
ent3=Entry(win,width=25,font=("bold",21),fg="#000000",bg="#F0F0F0")
ent3.place(x=750,y=310)





lab=Label(win,text="Address",width=6,fg="#000000",font=("bold",20) ,bg="#FAAFC9")
lab.place(x=600,y=370)
ent5=Entry(win,width=25,font=("bold",21),fg="#000000",bg="#F0F0F0")
ent5.place(x=750,y=370)






btn=Button(win,text="Order Now",width=15,height=1,fg="#000000",font=("bold",20),bg="#A1FB8E",command=payment)
btn.place(x=600,y=470)

btn=Button(win,text="Back Home",width=15,height=1,fg="#000000",font=("bold",20),bg="#A1FB8E",command=Home  )
btn.place(x=900,y=470)



win.mainloop()