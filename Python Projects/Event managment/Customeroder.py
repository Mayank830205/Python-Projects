from tkinter import *
from PIL import Image, ImageTk
import tkinter as tk
from tkinter import ttk
import os
import pymysql as sql
import csv
import pandas as pd
from tkinter import messagebox

def Home():
    
    
    os.system("python menubar.py") 

def About():
    win.destroy()
    os.system("python About.py") 
    
    
def Merriage():
    win.destroy()
    os.system("python marriage.py") 
    
def Bday():
    win.destroy()
    os.system("python bdayhall.py") 

def Dance():
    win.destroy()
    os.system("python dancehall.py") 
    
    
def Viewfeedback():
    win.destroy()
    os.system("python viewfeedback.py") 
    
def Feedback():
    win.destroy()
    os.system("python Rating.py") 
    
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

def show_record():
    
    conn,cur=db_connect()
    data=cur.execute("select hallname,name,mobile_no,event_type,food_type,food_timing,decoration_type,checkout_date from booking")
    rows=cur.fetchall()
    with open('output.csv', 'w', newline='') as csv_file:
        csv_writer = csv.writer(csv_file)
        column_names = [desc[0] for desc in cur.description]  # Column names
        csv_writer.writerow(column_names)
        csv_writer.writerows(rows)
    record=pd.read_csv('output.csv')
    rec=list(record.loc[0:])
    print(rec)
    r_set=record.to_numpy().tolist()
    treeview=ttk.Treeview(columns=("hallname","name","mobile_no","event_type","food_type","food_timing","decoration_type","checkout_date"),show='headings',height=10)
    column=["hallname","name","mobile_no","event_type","food_type","food_timing","decoration_type","checkout_date"] # yaha pr column name change kar dena dono jagh upar aur niche
    for i in range(0,8):
        treeview.column(f"# {i+1}",width=150,anchor=CENTER)
        treeview.heading(column[i],text=rec[i])
    for j in range(0,len(r_set)):
        treeview.insert('','end',values=r_set[j])
    treeview.place(x=10,y=200)



win=Tk()

win.state("zoomed")
#win.state('zoomed')
win.config(bg="white")


files1=Image.open("C:\\Users\\HP\\Desktop\\Event managment\\image\\whit.png")  # used for open image
files2=files1.resize((1300,700)) #for assign size
 
tk_image=ImageTk.PhotoImage(files2) #tk_imagee is a var name and ImageTk.PhotoImage is predefined
 
new_Label=tk.Label(win,image=tk_image) # here is image= is predefined
new_Label.pack() 




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

b6=Button(win,bg="black",fg="white",text="View Feedback",width=11,height=1,font=("Arial",14,"bold"),relief="flat",command=Viewfeedback )
b6.place(x=690,y=120)

b7=Button(win,bg="black",fg="white",text="Feedback",width=9,height=1,font=("Arial",14,"bold"),relief="flat" ,command=Feedback)
b7.place(x=855,y=120)

b7=Button(win,bg="black",fg="white",text="Logout",width=9,height=1,font=("Arial",14,"bold"),relief="flat" ,command=logout)
b7.place(x=980,y=120)




show_record()

win.mainloop()