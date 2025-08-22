from tkinter import *
from tkinter import ttk,messagebox
import tkinter as tk
import os
import csv
import pandas as pd
from PIL import Image,ImageTk
import pymysql as sql
from tkcalendar import DateEntry
 
def Home():
    win.destroy()
    os.system("python home.py")

def history():
    win.destroy()
    os.system("python history.py") 
    
def room():
    win.destroy()
    os.system("python rooms.py") 
    
def gallary():
    win.destroy()
    os.system("python gallery.py") 

def feedback():
    win.destroy()
    os.system("python feedback.py") 
    
def mybook():
    win.destroy()
    os.system("python bookingshow.py") 
    
def cencel():
    win.destroy()
    #os.system("python history.py") 
    

def book():
    win.destroy()
    os.system("python booking.py") 

def db_connect():
    conn=sql.connect(host='localhost',port=3306,user='root',password='',database='hotel')
    cur=conn.cursor()
    return conn,cur

def show_record():
    
    conn,cur=db_connect()
    data=cur.execute("select Full_name ,Email , Phone_no,Aadhar_card,Check_in,Time,Room_no from booking")
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
    treeview=ttk.Treeview(columns=("Full_name" ,"Email" , "Phone_no","Aadhar_card","Check_in","Time","Room_no"),show='headings',height=10)
    column=["Full_name" ,"Email" , "Phone_no","Aadhar_card","Check_in","Time","Room_no"] # yaha pr column name change kar dena dono jagh upar aur niche
    for i in range(0,7):
        treeview.column(f"# {i+1}",width=150,anchor=CENTER)
        treeview.heading(column[i],text=rec[i])
    for j in range(0,len(r_set)):
        treeview.insert('','end',values=r_set[j])
    treeview.place(x=100,y=200)



 
win=Tk()
win.config(bg="#73FBFD")
win.state("zoomed")
#win.minsize(width="1920",height="1080")
#win.maxsize(width="1920",height="1080")

image= Image.open("C:\\Users\\HP\\Desktop\\hotel management system\\bok.png")
image = image.resize((1270,700))

tk_image = ImageTk.PhotoImage(image)
image_label = tk.Label(win,image=tk_image)
image_label.pack()

frame=Frame(win,bg="#1D4A8C",width=1920,height=100)
frame.place(x=0,y=1)   

lab=Label(frame,text="The Ritz India",width=10,height=0,fg="#FFFFFF",font=("bold",30),bg="#1D4A8C")
lab.place(x=0,y=0)

btn=Button(frame,text="Home",width=8,fg="#FFFFFF",font=("bold",19),bg="#1D4A8C",relief="flat",command=Home)
btn.place(x=300,y=20)

btn=Button(frame,text="History",width=8,fg="#FFFFFF",font=("bold",19),bg="#1D4A8C",relief="flat",command=history)
btn.place(x=430,y=20)
btn=Button(frame,text="Rooms",width=8,fg="#FFFFFF",font=("bold",19),bg="#1D4A8C",relief="flat",command=room)
btn.place(x=570,y=20)
btn=Button(frame,text="Gallery",width=8,fg="#FFFFFF",font=("bold",19),bg="#1D4A8C",relief="flat",command=gallary)
btn.place(x=700,y=20)
btn=Button(frame,text="Feedback",width=8,fg="#FFFFFF",font=("bold",19),bg="#1D4A8C",relief="flat",command=feedback)
btn.place(x=840,y=20)
btn=Button(frame,text="My Bookings",width=10,fg="#FFFFFF",font=("bold",19),bg="#1D4A8C",relief="flat",command=mybook)
btn.place(x=990,y=20)
btn=Button(frame,text="Cancel",width=9,fg="#FFFFFF",font=("bold",19),bg="#1D4A8C",relief="flat",command=cencel)
btn.place(x=1130,y=20)

show_record()

win.mainloop()