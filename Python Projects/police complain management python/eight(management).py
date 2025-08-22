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
    
    os.system("python fifth(home_page).py") 

def About():
    #win.destroy()
    os.system("python nine(about).py") 
    
    
def report():
    #win.destroy()
    os.system("python seven(report).py") 
    
def management():
    #win.destroy()
    os.system("python eight(management).py") 

def maping():
    #win.destroy()
    os.system("python six(crime_maping).py") 
    
    
     
def logout():
    # Display a confirmation message
    confirm = messagebox.askyesno("Logout", "Are you sure you want to logout?")
    if confirm:
        # Close the application or redirect to login screen
        win.destroy()    
    
    


def db_connect():
    conn=sql.connect(host='localhost',port=3306,user='root',password='',database='police')
    cur=conn.cursor()
    return conn,cur

    
def submit():
    
    a=Bent.get()
    b=Cent.get()
    c=Dent.get()
    d=date1.get()
    e=date.get()
    f=Eent.get()
    if (a=="") or (b=="") or (c=="") or (d=="") or (e=="") or (f=="") :
        messagebox.showwarning("Warning","Please provide a valid input!!!")
    else:
        conn,cur=db_connect()
        cmd1='select * from management'
        cur.execute(cmd1)
        
        cmd=f"insert into management(Case_Id , Inspector_Name , Case_Type , Date_Opened , Date_Closed, Case_Description) values('{Bent.get()}', '{Cent.get()}', '{Dent.get()}','{date1.get()}', '{date.get()}','{Eent.get()}')"
            
        cur.execute(cmd)
        conn.commit()
        messagebox.showinfo("Send","Send Successfully")
        win.destroy()
        os.system("python fifth(home_page).py") 
   
win=Tk()

#win.geometry("1000x700")
win.state('zoomed')
win.config(bg="white")

files1=Image.open("C:\\Users\\HP\\Desktop\\police complain management python\\image\\case.png")  # used for open image
files2=files1.resize((1300,500)) #for assign size
 
tk_image=ImageTk.PhotoImage(files2) #tk_imagee is a var name and ImageTk.PhotoImage is predefined
 
new_Label=tk.Label(win,image=tk_image) # here is image= is predefined
new_Label.place(x=0,y=150) 

talk=Label(win,text="👉CASE MANAGEMENT",bg="white",fg="black",font=("Snap ITC",28,"bold","underline"))
talk.place(x=700,y=20)

blank=Label(win,bg="white",fg="black",width=70,height=1,font=("Arial",22,"bold"))
blank.place(x=4,y=120)

b1=Button(win,fg="black",bg="white",text="Home",width=7,height=1,font=("Arial",14,"bold"),relief="flat",command=Home)
b1.place(x=15,y=120)

b2=Button(win,fg="black",bg="white",text="About",width=7,height=1,font=("Arial",14,"bold"),relief="flat",command=About)
b2.place(x=140,y=120)

b3=Button(win,fg="black",bg="white",text="Crime Reporting",width=14,height=1,font=("Arial",14,"bold"),relief="flat", command=report )
b3.place(x=260,y=120)

b4=Button(win,fg="black",bg="white",text="Case Management",width=14,height=1,font=("Arial",14,"bold"),relief="flat",command=management )
b4.place(x=480,y=120)

b5=Button(win,fg="black",bg="white",text="Crime Mapping",width=11,height=1,font=("Arial",14,"bold"),relief="flat",command=maping )
b5.place(x=730,y=120)




b7=Button(win,fg="black",bg="white",text="Logout",width=9,height=1,font=("Arial",14,"bold"),relief="flat" ,command=logout)
b7.place(x=910,y=120)



#Blank=Label(win,bg="white",fg="black",width=26,height=13,font=("Arial",22,"bold"))
#Blank.place(x=110,y=190)


A=Label(win,text="Case Mnanagement",bg="white",fg="black",font=("Arial",30,"bold","underline"))
A.place(x=200,y=180)

B=Label(win,text="Case Id",fg="white",bg="black",font=("Arial",17,"bold"))
B.place(x=150,y=260)

Bent=Entry(win,bg="white",width=18,font=("Arial",17,"bold"))
Bent.place(x=400,y=260)

C=Label(win,text="Inspector Name",fg="white",bg="black",font=("Arial",17,"bold"))
C.place(x=150,y=310)

Cent=Entry(win,bg="white",width=18,font=("Arial",17,"bold"))
Cent.place(x=400,y=310)



D=Label(win,text="Case Type",fg="white",bg="black",font=("Arial",17,"bold"))
D.place(x=150,y=360)

Dent=Entry(win,bg="white",width=18,font=("Arial",17,"bold"))
Dent.place(x=400,y=360)

E=Label(win,text="Date opened",fg="white",bg="black",font=("Arial",17,"bold"))
E.place(x=150,y=410)

date1=DateEntry(win,date_pattern="yyyy-mm-dd",width=25)
date1.place(x=400,y=410)






k=Label(win,text="Date Closed",fg="white",bg="black",font=("Arial",17,"bold"))
k.place(x=150,y=450)
date=DateEntry(win,date_pattern="yyyy-mm-dd",width=25)
#kent=Entry(win,bg="white",width=18,font=("Arial",17,"bold"))
date.place(x=400,y=460)

E=Label(win,text="Case Description ",fg="white",bg="black",font=("Arial",17,"bold"))
E.place(x=150,y=490)
Eent=Entry(win,bg="white",width=18,font=("Arial",17,"bold"))
Eent.place(x=400,y=490)


Lg=Button(win,text="Submit",bg="green",fg="white",font=("Arial",14,"bold"),command=submit )
Lg.place(x=650,y=570)




win.mainloop()