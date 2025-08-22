from tkinter import *
from PIL import Image, ImageTk
import tkinter as tk
from tkinter import ttk
import os
from tkcalendar import DateEntry
from tkinter import messagebox
import pymysql as sql
from functools import reduce


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
    os.system("python pyment_detail.py") 
    
def logout():
    # Display a confirmation message
    confirm = messagebox.askyesno("Logout", "Are you sure you want to logout?")
    if confirm:
        # Close the application or redirect to login screen
        win.destroy()    
    
    


def db_connect():
    conn=sql.connect(host='localhost',port=3306,user='root',password='',database='Event')
    cur=conn.cursor()
    return conn,cur

    
def submit():
    a=Cent.get()
    b=Fent.get()
    c=Newvar.get()
    d=Newvar2.get()
    e=Newvar3.get()
    f=Newvar4.get()
    g=date.get()
    if (a=="") or (b=="") or (c=="") or (d=="") or (e=="") or (f=="") or (g==""):
        messagebox.showwarning("Warning","Please provide a valid input!!!")
    else:
        conn,cur=db_connect()
        cmd1='select * from hall'
        cur.execute(cmd1)
        hall_name=cur.fetchall() # name ke sath data lata hai
        hall_name=list(reduce(lambda x,y:x+y,hall_name))
        print(hall_name[0])
        cmd=f"insert into booking(hallname,name, mobile_no, event_type,food_type,food_timing,decoration_type,checkout_date) values('{hall_name[0]}','{Cent.get()}', {Fent.get()}, '{Newvar.get()}','{Newvar2.get()}', '{Newvar3.get()}','{Newvar4.get()}', '{date.get()}')"
            
        cur.execute(cmd)
        conn.commit()
        messagebox.showinfo("Send","Send Successfully")
        win.destroy()
        os.system("python Payment.py") 
        
    
win=Tk()

#win.geometry("1000x700")
win.state('zoomed')
win.config(bg="white")

files1=Image.open("C:\\Users\\HP\\Desktop\\Event managment\\image\\book2.png")  # used for open image
files2=files1.resize((1300,500)) #for assign size
 
tk_image=ImageTk.PhotoImage(files2) #tk_imagee is a var name and ImageTk.PhotoImage is predefined
 
new_Label=tk.Label(win,image=tk_image) # here is image= is predefined
new_Label.place(x=0,y=150) 

talk=Label(win,text="⭐EVENT MANAGMENT⭐",bg="white",fg="black",font=("Snap ITC",28,"bold"))
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

b8=Button(win,bg="black",fg="white",text="Logout",width=9,height=1,font=("Arial",14,"bold"),relief="flat" ,command=logout)
b8.place(x=1040,y=120)


#Blank=Label(win,bg="white",fg="black",width=26,height=13,font=("Script MT Bold",22,"bold"))
#Blank.place(x=110,y=190)


A=Label(win,text="Booking",bg="white",fg="black",font=("Script MT Bold",34,"bold","underline"))
A.place(x=320,y=180)

C=Label(win,text="First Name",bg="white",fg="black",font=("Script MT Bold",19,"bold"))
C.place(x=150,y=290)

Cent=Entry(win,bg="white",width=20,font=("Script MT Bold",19,"bold"))
Cent.place(x=350,y=290)

'''D=Label(win,text="User Id",bg="white",fg="black",font=("Script MT Bold",19,"bold"))
D.place(x=150,y=330)

Dent=Entry(win,bg="white",width=20,font=("Script MT Bold",19,"bold"))
Dent.place(x=350,y=330)

E=Label(win,text="Email Id",bg="white",fg="black",font=("Script MT Bold",19,"bold"))
E.place(x=150,y=370)

Eent=Entry(win,bg="white",width=20,font=("Script MT Bold",19,"bold"))
Eent.place(x=350,y=370)'''

F=Label(win,text="Mobile No.",bg="white",fg="black",font=("Script MT Bold",19,"bold"))
F.place(x=150,y=330)

Fent=Entry(win,bg="white",width=20,font=("Script MT Bold",19,"bold"))
Fent.place(x=350,y=330)

G=Label(win,text="Event Type",bg="white",fg="black",font=("Script MT Bold",19,"bold"))
G.place(x=150,y=370)

#Gent=Entry(win,bg="white",width=20,font=("Script MT Bold",19,"bold"))
#Gent.place(x=350,y=370)
Newvar = StringVar()
cb=ttk.Combobox(win,textvariable=Newvar)
cb['values']=('Merriage Event','Birthday Event','other')
cb['state']='readonly'
#Eent=Entry(win,bg="grey",width=20,font=("Rockwell Extra Bold",18,"bold"))
cb.place(x=350,y=370)


H=Label(win,text="Food Type",bg="white",fg="black",font=("Script MT Bold",19,"bold"))
H.place(x=150,y=410)

#Hent=Entry(win,bg="white",width=20,font=("Script MT Bold",19,"bold"))
#Hent.place(x=350,y=410)
Newvar2 = StringVar()
cb=ttk.Combobox(win,textvariable=Newvar2)
cb['values']=('Vegetarian','Non Vegetarian','Both','Speacial')
cb['state']='readonly'
#Eent=Entry(win,bg="grey",width=20,font=("Rockwell Extra Bold",18,"bold"))
cb.place(x=350,y=410)


I=Label(win,text="Food Timing",bg="white",fg="black",font=("Script MT Bold",19,"bold"))
I.place(x=150,y=450)

#Ient=Entry(win,bg="white",width=20,font=("Script MT Bold",19,"bold"))
#Ient.place(x=350,y=450)
Newvar3 = StringVar()
cb=ttk.Combobox(win,textvariable=Newvar3)
cb['values']=('Morning','Afternoon','Evening','Night')
cb['state']='readonly'
#Eent=Entry(win,bg="grey",width=20,font=("Rockwell Extra Bold",18,"bold"))
cb.place(x=350,y=450)

J=Label(win,text="Decoration Type",bg="white",fg="black",font=("Script MT Bold",19,"bold"))
J.place(x=150,y=490)

#Jent=Entry(win,bg="white",width=20,font=("Script MT Bold",19,"bold"))
#Jent.place(x=350,y=490)
Newvar4 = StringVar()
cb=ttk.Combobox(win,textvariable=Newvar4)
cb['values']=('Lighting decoration','Floral decoration','Balloon decoration','Speacial decoration')
cb['state']='readonly'
#Eent=Entry(win,bg="grey",width=20,font=("Rockwell Extra Bold",18,"bold"))
cb.place(x=350,y=490)



k=Label(win,text="Check OutDate",bg="white",fg="black",font=("Script MT Bold",19,"bold"))
k.place(x=150,y=530)
date=DateEntry(win,date_pattern="yyyy-mm-dd",width=38)
#kent=Entry(win,bg="white",width=20,font=("Script MT Bold",19,"bold"))
date.place(x=350,y=530)

E=Label(win,text="Hall Type",bg="white",fg="black",font=("Script MT Bold",19,"bold"))
E.place(x=150,y=570)

Newvar = StringVar()
cb=ttk.Combobox(win,textvariable=Newvar)
cb['values']=('AC','Non AC')
cb['state']='readonly'
#Eent=Entry(win,bg="white",width=20,font=("Rockwell Extra Bold",18,"bold"))
cb.place(x=350,y=570)

Lg=Button(win,text="Submit",bg="green",fg="white",font=("Script MT Bold",14,"bold"),command=submit )
Lg.place(x=650,y=580)




win.mainloop()