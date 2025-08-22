from tkinter import *
from PIL import Image, ImageTk
import tkinter as tk
from tkinter import ttk
import os
from tkinter import messagebox
import pymysql as sql

#import csv
import pandas as pd

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

def show_record():
    
    cur.execute("SELECT * FROM rating")
    rows = cur.fetchall()
    r_set = list(rows)
    
    # Create a Treeview widget
    treeview = ttk.Treeview(columns=("Name", "Rating", "Customer_Review"), show='headings', height=21)
    treeview.place(x=30,y=180)
    column = ["Name",  "Rating", "Customer_Review"]
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


files1=Image.open("C:\\Users\\HP\\Desktop\\JWELLARY MANAGEMENT\\image\\sign.png")  # used for open image
files2=files1.resize((600,450)) #for assign size
 
tk_image=ImageTk.PhotoImage(files2) #tk_imagee is a var name and ImageTk.PhotoImage is predefined
 
new_Label=tk.Label(win,image=tk_image) # here is image= is predefined
new_Label.place(x=660,y=180) 

#Blank=Label(win,bg="white",fg="black",width=34,height=13,font=("Arial",22,"bold"))
#Blank.place(x=110,y=190)


talk=Label(win,text=" JWELERY COLLECTION ❤",bg="white",fg="black",font=("Algerian",30,"bold"))
talk.place(x=370,y=30)
'''files1=Image.open("C:\\Users\\HP\\Desktop\\JWELLARY MANAGEMENT\\image\\hom.png")  # used for open image
files2=files1.resize((1215,600)) #for assign size
 
tk_image=ImageTk.PhotoImage(files2) #tk_imagee is a var name and ImageTk.PhotoImage is predefined
 
new_Label=tk.Label(win,image=tk_image) # here is image= is predefined
new_Label.place(x=30,y=100) 

'''

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







show_record()

win.mainloop()