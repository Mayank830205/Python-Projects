from tkinter import *
from PIL import Image, ImageTk
import tkinter as tk
from tkinter import ttk
import os
from tkinter import filedialog
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
    conn = sql.connect(host='localhost', port=3306, user='root', password='', database='police')
    cur = conn.cursor()
    return conn, cur

def show_record(root):  # Pass the Tk root window
    conn, cur = db_connect()

    cur.execute("SELECT * FROM maping")
    rows = cur.fetchall()
    
    

    # Create a Treeview widget
    treeview = ttk.Treeview(root, columns=("Case_Id", "Case_Type", "Location", "Date_And_Time", "Description"), show='headings')
    treeview.place(x=50, y=300)  # Fixed: x instead of k

    column = ["Case_Id", "Case_Type", "Location", "Date_And_Time", "Description"]
    for i in range(len(column)):
        treeview.column(column[i], width=240, anchor="center")
        treeview.heading(column[i], text=column[i])

    # Insert data into the Treeview
    for row in rows:
        treeview.insert('', 'end', values=row)

if __name__ == "__main__":
    win = Tk()
    win.state('zoomed')  # Adjust window size
            # Pass root to show_record
     
    
    



talk=Label(win,text="👉CRIME REPORTING👈",bg="white",fg="black",font=("Snap ITC",28,"bold"))
talk.place(x=18,y=30)

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




files1=Image.open("C:\\Users\\HP\\Desktop\\police complain management python\\image\\report.png")  # used for open image
files2=files1.resize((1300,500)) #for assign size
 
tk_image=ImageTk.PhotoImage(files2) #tk_imagee is a var name and ImageTk.PhotoImage is predefined
 
new_Label=tk.Label(win,image=tk_image) # here is image= is predefined
new_Label.place(x=0,y=150) 

A=Label(win,text="Report Details",fg="white",bg="black",font=("Arial",34,"bold","underline"))
A.place(x=450,y=180)

show_record(win) 

win.mainloop()