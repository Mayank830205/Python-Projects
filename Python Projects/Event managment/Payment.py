from tkinter import *
from PIL import Image, ImageTk
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
from tkinter import messagebox
import pymysql as sql
import os

def Home():
    #win.destroy()
    
    os.system("python menubar.py") 

def About():
    #win.destroy()
    os.system("python About.py") 
    
    
def Merriage():
    #win.destroy()
    os.system("python marriage.py") 
    
def Bday():
    #win.destroy()
    os.system("python bdayhall.py") 

def Dance():
    #win.destroy()
    os.system("python dancehall.py") 
    
    
def customer_payment():
    #win.destroy()
    os.system("python Payment.py") 
    
def payment_detail():
    #win.destroy()
    os.system("python pyment_detail..py")
    


def submit():
    messagebox.showinfo("Submit","Submit Successfully")
    
def db_connect():
    conn=sql.connect(host='localhost',port=3306,user='root',password='',database='Event')
    cur=conn.cursor()
    return conn,cur

    
def submit():
    a=Cent.get()
    b=Newvar2.get()
    c=Gent.get()
    #d=Eent.get()
    if (a=="") or (b=="") or (c=="") :
        messagebox.showwarning("Warning","Please provide a valid input!!!")
    else:
        cmd=f"insert into payment(Customer_Name, Payment_method, Amount) values('{Cent.get()}', '{Newvar2.get()}','{Gent.get()}')"
        conn,cur=db_connect()      
        cur.execute(cmd)
        conn.commit()
        messagebox.showinfo("Send","Send Successfully")
        win.destroy()
        os.system("python menubar.py") 
    
win=Tk()

#win.geometry("1000x700")
win.state('zoomed')
win.config(bg="white")
talk=Label(win,text="⭐EVENT MANAGMENT⭐",bg="white",fg="black",font=("Algerian",28,"bold"))
talk.place(x=20,y=30)

blank=Label(win,fg="white",bg="black",width=70,height=1,font=("Arial",22,"bold"))
blank.place(x=4,y=120)

b1=Button(win,bg="black",fg="white",text="Home",width=7,height=1,font=("Arial",14,"bold"),relief="flat",command=Home)
b1.place(x=15,y=120)

b2=Button(win,bg="black",fg="white",text="About",width=7,height=1,font=("Arial",14,"bold"),relief="flat",command=About)
b2.place(x=120,y=120)

b3=Button(win,bg="black",fg="white",text="Merriage Hall",width=11,height=1,font=("Arial",14,"bold"),relief="flat", command=Merriage )
b3.place(x=230,y=120)

b4=Button(win,bg="black",fg="white",text="Birthday Hall",width=11,height=1,font=("Arial",14,"bold"),relief="flat",command=Bday )
b4.place(x=390,y=120)

b5=Button(win,bg="black",fg="white",text="Dance Hall",width=11,height=1,font=("Arial",14,"bold"),relief="flat",command=Dance )
b5.place(x=540,y=120)

b6=Button(win,bg="black",fg="white",text="Customer_Pyment",width=15,height=1,font=("Arial",14,"bold"),relief="flat",command=customer_payment )
b6.place(x=690,y=120)

b7=Button(win,bg="black",fg="white",text="Payment_detail",width=15,height=1,font=("Arial",14,"bold"),relief="flat" ,command=payment_detail)
b7.place(x=870,y=120)

b7=Button(win,bg="black",fg="white",text="Logout",width=9,height=1,font=("Arial",14,"bold"),relief="flat" )
b7.place(x=1040,y=120)



files1=Image.open("C:\\Users\\HP\\Desktop\\Event managment\\image\\pixl.png")  # used for open image
files2=files1.resize((1150,466)) #for assign size
 
tk_image=ImageTk.PhotoImage(files2) #tk_imagee is a var name and ImageTk.PhotoImage is predefined
 
new_Label=tk.Label(win,image=tk_image) # here is image= is predefined
new_Label.place(x=50,y=170) 


Blank=Label(win,bg="white",fg="black",width=38,height=12,font=("Arial",22,"bold"))
Blank.place(x=260,y=197)


C=Label(win,text="Customer Name",bg="white",fg="black",font=("Script MT Bold",19,"bold"))
C.place(x=350,y=250)

Cent=Entry(win,bg="white",width=20,font=("Script MT Bold",19,"bold"))
Cent.place(x=350,y=300)




F=Label(win,text="Payment Method",bg="white",fg="black",font=("Script MT Bold",19,"bold"))
F.place(x=350,y=350)
Newvar2 = StringVar()
F=ttk.Combobox(win,textvariable=Newvar2)
F['values']=('UPI','Credit card','Debit Card')
F['state']='readonly'
F.place(x=350,y=400)

G=Label(win,text="Amount",bg="white",fg="black",font=("Script MT Bold",19,"bold"))
G.place(x=350,y=450)

Gent=Entry(win,bg="white",width=20,font=("Script MT Bold",19,"bold"))
Gent.place(x=350,y=500)



Lg=Button(win,text="Submit",bg="green",fg="white",font=("Rockwell Extra Bold",14,"bold"),command=submit )
Lg.place(x=780,y=550)


win.mainloop()