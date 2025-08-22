from tkinter import *
from PIL import Image, ImageTk
import tkinter as tk
from tkinter import ttk
import os
import pymysql as sql


import pandas as pd

def Home():
   
    
    os.system("python menubar.py") 
    #win.destroy()

def About():
   
    os.system("python About.py") 
    #win.destroy()
    
def Merriage():
   
    os.system("python Mrghall.py") 
    
def Bday():
   
    os.system("python bdayhall.py") 

def Dance():
   
    os.system("python dancehall.py") 
    
    
def Viewfeedback():
   
    os.system("python viewfeedback.py") 
    
def Feedback():
   
    os.system("python Rating.py") 


def db_connect():
    conn=sql.connect(host='localhost',port=3306,user='root',password='',database='Event')
    cur=conn.cursor()
    return conn,cur

def show_record():
    
    cur.execute("SELECT * FROM rating")
    rows = cur.fetchall()
    r_set = list(rows)
    
    # Create a Treeview widget
    treeview = ttk.Treeview(columns=("Name", "Hall_Name", "Rating", "Customer_Review"), show='headings', height=10)
    treeview.place(x=150,y=300)
    column = ["Name", "Hall_Name", "Rating", "Customer_Review"]
    for i in range(len(column)):
        treeview.column(f"#{i+1}", width=200, anchor=CENTER)
        treeview.heading(column[i], text=column[i])

    # Insert data into the Treeview
    for row in r_set:
        treeview.insert('', 'end', values=row)
  
if __name__ == "__main__":
    # Initialize the database connection
    conn, cur = db_connect()        
    
    


win=Tk()

win.state("zoomed")
#win.state('zoomed')
win.config(bg="white")


files1=Image.open("C:\\Users\\HP\\Desktop\\Event managment\\image\\feed.png")  # used for open image
files2=files1.resize((1270,600)) #for assign size
 
tk_image=ImageTk.PhotoImage(files2) #tk_imagee is a var name and ImageTk.PhotoImage is predefined
 
new_Label=tk.Label(win,image=tk_image) # here is image= is predefined
new_Label.place(x=0,y=120) 



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

b7=Button(win,bg="black",fg="white",text="Logout",width=9,height=1,font=("Arial",14,"bold"),relief="flat" )
b7.place(x=980,y=120)




show_record()

win.mainloop()