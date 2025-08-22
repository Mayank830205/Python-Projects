from tkinter import *
from PIL import Image, ImageTk
import tkinter as tk
from tkinter import ttk
import os
from tkcalendar import DateEntry
from tkinter import messagebox
import pymysql as sql
from functools import reduce


def home():
    #win.destroy()
    
    os.system("python home(4)).py") 

def about():
    #win.destroy()
    os.system("python about(12).py") 
    
    
def jwelery():
    #win.destroy()
    os.system("python jwellery(5).py") 
    

def booking():
    #win.destroy()
    os.system("python boking_show(7).py")
   
def feedback():
    #win.destroy()
    os.system("python feedback(9).py") 

def customer():
    #win.destroy()
    os.system("python veiw_feedback(10).py") 
    
    
 
    
def logout():
    # Display a confirmation message
    confirm = messagebox.askyesno("Logout", "Are you sure you want to logout?")
    if confirm:
        # Close the application or redirect to login screen
        win.destroy()    
    
    


def db_connect():
    conn=sql.connect(host='localhost',port=3306,user='root',password='',database='jwellery')
    cur=conn.cursor()
    return conn,cur

    
def submit():
    a=Cent.get()
    b=Fent.get()
    c=Newvar.get()
    d=Hent.get()
    e=Newvar3.get()
    f=date.get()
    if (a=="") or (b=="") or (c=="") or (d=="") or (e=="") or (f=="") :
        messagebox.showwarning("Warning","Please provide a valid input!!!")
    else:
        
        cmd=f"insert into booking(Full_Name, Mobile_No, Jwelery_type,Address,Booking_Time,Checkout_Date) values('{Cent.get()}', {Fent.get()}, '{Newvar.get()}',  '{Hent.get()}','{Newvar3.get()}', '{date.get()}')"
        conn,cur=db_connect()      
        cur.execute(cmd)
        conn.commit()
        messagebox.showinfo("Send","Send Successfully")
        win.destroy()
    
        os.system("python payment(8).py") 
    
    
win=Tk()

#win.geometry("1000x700")
win.state('zoomed')
win.config(bg="white")

files1=Image.open("C:\\Users\\HP\\Desktop\\JWELLARY MANAGEMENT\\image\\book.png")  # used for open image
files2=files1.resize((600,450)) #for assign size
 
tk_image=ImageTk.PhotoImage(files2) #tk_imagee is a var name and ImageTk.PhotoImage is predefined
 
new_Label=tk.Label(win,image=tk_image) # here is image= is predefined
new_Label.place(x=660,y=180) 

talk=Label(win,text=" JWELERY COLLECTION ❤",bg="white",fg="black",font=("Algerian",30,"bold"))
talk.place(x=370,y=30)

blank=Label(win,fg="white",bg="black",width=70,height=1,font=("Arial",22,"bold"))
blank.place(x=4,y=120)

b1=Button(win,bg="black",fg="white",text="Home",width=7,height=1,font=("Arial",14,"bold"),relief="flat",command=home)
b1.place(x=15,y=120)

b2=Button(win,bg="black",fg="white",text="About",width=7,height=1,font=("Arial",14,"bold"),relief="flat",command=about)
b2.place(x=140,y=120)

b3=Button(win,bg="black",fg="white",text="Jwellery",width=14,height=1,font=("Arial",14,"bold"),relief="flat", command=jwelery )
b3.place(x=260,y=120)

b4=Button(win,bg="black",fg="white",text="Booking Jwelery",width=14,height=1,font=("Arial",14,"bold"),relief="flat",command=booking )
b4.place(x=445,y=120)



b5=Button(win,bg="black",fg="white",text="Feedback",width=11,height=1,font=("Arial",14,"bold"),relief="flat",command=feedback )
b5.place(x=660,y=120)




b7=Button(win,bg="black",fg="white",text="Customer_Review",width=14,height=1,font=("Arial",14,"bold"),relief="flat" ,command=customer)
b7.place(x=840,y=120)


b8=Button(win,bg="black",fg="white",text="logout",width=11,height=1,font=("Arial",14,"bold"),relief="flat" ,command=logout)
b8.place(x=1050,y=120)





#Blank=Label(win,bg="white",fg="black",width=26,height=13,font=("Script MT Bold",22,"bold"))
#Blank.place(x=110,y=190)


A=Label(win,text="Booking",bg="white",fg="black",font=("Script MT Bold",34,"bold","underline"))
A.place(x=320,y=180)

C=Label(win,text="Full Name",bg="white",fg="black",font=("Script MT Bold",19,"bold"))
C.place(x=150,y=290)

Cent=Entry(win,bg="white",width=20,font=("Script MT Bold",19,"bold"))
Cent.place(x=350,y=290)



F=Label(win,text="Mobile No.",bg="white",fg="black",font=("Script MT Bold",19,"bold"))
F.place(x=150,y=330)

Fent=Entry(win,bg="white",width=20,font=("Script MT Bold",19,"bold"))
Fent.place(x=350,y=330)

G=Label(win,text="Jwellwery Type",bg="white",fg="black",font=("Script MT Bold",19,"bold"))
G.place(x=150,y=370)

#Gent=Entry(win,bg="white",width=20,font=("Script MT Bold",19,"bold"))
#Gent.place(x=350,y=370)
Newvar = StringVar()
cb=ttk.Combobox(win,textvariable=Newvar)
cb['values']=('Gold','Diomond','silver')
cb['state']='readonly'
#Eent=Entry(win,bg="grey",width=20,font=("Rockwell Extra Bold",18,"bold"))
cb.place(x=350,y=370)


H=Label(win,text="Address ",bg="white",fg="black",font=("Script MT Bold",19,"bold"))
H.place(x=150,y=410)

Hent=Entry(win,bg="white",width=20,font=("Script MT Bold",19,"bold"))
Hent.place(x=350,y=410)


I=Label(win,text="Booking Time",bg="white",fg="black",font=("Script MT Bold",19,"bold"))
I.place(x=150,y=450)

#Ient=Entry(win,bg="white",width=20,font=("Script MT Bold",19,"bold"))
#Ient.place(x=350,y=450)
Newvar3 = StringVar()
cb=ttk.Combobox(win,textvariable=Newvar3)
cb['values']=('Morning','Afternoon','Evening','Night')
cb['state']='readonly'
#Eent=Entry(win,bg="grey",width=20,font=("Rockwell Extra Bold",18,"bold"))
cb.place(x=350,y=450)





k=Label(win,text="Check OutDate",bg="white",fg="black",font=("Script MT Bold",19,"bold"))
k.place(x=150,y=490)
date=DateEntry(win,date_pattern="yyyy-mm-dd",width=38)
#kent=Entry(win,bg="white",width=20,font=("Script MT Bold",19,"bold"))
date.place(x=350,y=490)


Lg=Button(win,text="Payment",bg="green",fg="white",font=("Script MT Bold",14,"bold"),command=submit )
Lg.place(x=550,y=580)




win.mainloop()