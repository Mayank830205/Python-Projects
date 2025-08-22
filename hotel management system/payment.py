from tkinter import *
from tkinter import ttk,messagebox
import tkinter as tk
import os
from PIL import Image,ImageTk
import pymysql as sql


def pre():
    win.destroy()
    os.system("python booking.py")
    

def db_connect():
    conn=sql.connect(host='localhost',port=3306,user='root',password='',database='hotel')
    cur=conn.cursor()
    return conn,cur

    
def fun():
    a=ent1.get()
    b=ent2.get()
    c=ent3.get()
    #d=Eent.get()
    if (a=="") or (b=="") or (c=="") :
        messagebox.showwarning("Warning","Please provide a valid input!!!")
    else:
        cmd=f"insert into payment(Card_number , Expiry_date, Cvv) values('{ent1.get()}', '{ent2.get()}','{ent3.get()}')"
        conn,cur=db_connect()      
        cur.execute(cmd)
        conn.commit()
        messagebox.showinfo("Send","Send Successfully")
        win.destroy()
        os.system("python home.py")

 
win=Tk()
win.config(bg="#48B5FF")
win.state("zoomed")
#win.minsize(width="1920",height="1080")
#win.maxsize(width="1920",height="1080")



'''def fun():
    a=ent1.get()
    a=ent2.get()
    a=ent3.get()
    if a=="":
        messagebox.showerror("empty","Please fill the Details")
    messagebox.showinfo("Success","payment Successfully")

'''

image= Image.open("C:\\Users\\HP\\Desktop\\hotel management system\\img11.webp")
image = image.resize((1280,670))

tk_image = ImageTk.PhotoImage(image)

image_label = tk.Label(win,image=tk_image)
image_label.pack()


lab=Label(win,text="",width=15,height=6,font=("bold",50),bg="#FFEFB6")
lab.place(x=20,y=130)

file1=PhotoImage(file="imf3.png")
lab1=Label(win,image=file1)
lab1.place(x=120,y=200)

file=PhotoImage(file="img10.png")
lab=Label(win,image=file)
lab.place(x=420,y=200)



lab=Label(win,text="Payment Details",width=20,fg="#000000", font=("bold",30),bg="#FFEFB6")
lab.place(x=100,y=150)


lab=Label(win,text="Card Number:",width=11,fg="#000000",font=("bold",15) ,bg="#FFEFB6")
lab.place(x=100,y=310)
ent1=Entry(win,width=25,font=("bold",15),fg="#000000",bg="#F0F0F0")
ent1.place(x=270,y=310)


lab=Label(win,text="Booking for: {{Clothes}}",width=19 ,fg="#000000", font=("bold",15),bg="#FFEFB6")
lab.place(x=100,y=350)


lab=Label(win,text="Expiry Date:",width=9,fg="#000000",font=("bold",15) ,bg="#FFEFB6")
lab.place(x=100,y=400)
ent2=Entry(win,width=25,font=("bold",15),fg="#000000",bg="#F0F0F0")
ent2.place(x=270,y=400)


lab=Label(win,text="CVV:",width=4,fg="#000000",font=("bold",15) ,bg="#FFEFB6")
lab.place(x=100,y=450)
ent3=Entry(win,width=25,font=("bold",15),fg="#000000",bg="#F0F0F0")
ent3.place(x=270,y=450)

btn=Button(win,text="Previous",width=10,fg="#000000",font=("bold",20),bg="#A1FB8E", command=pre)
btn.place(x=100,y=500)

btn=Button(win,text="Submit",width=10,fg="#000000",font=("bold",20),bg="#A1FB8E",command=fun)
btn.place(x=370,y=500)

win.mainloop()