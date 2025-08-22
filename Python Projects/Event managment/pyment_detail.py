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
    
    cur.execute("SELECT * FROM payment")
    rows = cur.fetchall()
    r_set = list(rows)
    
    # Create a Treeview widget
    treeview = ttk.Treeview(columns=("Customer_Name", "Payment_method", "Amount"), show='headings', height=10)
    treeview.place(x=180,y=200)
    column = ["Customer_Name", "Payment_method", "Amount"]
    for i in range(len(column)):
        treeview.column(f"#{i+1}", width=300, anchor=CENTER)
        treeview.heading(column[i], text=column[i])

    # Insert data into the Treeview
    for row in r_set:
        treeview.insert('', 'end', values=row)
  
if __name__ == "__main__":
    # Initialize the database connection
    conn, cur = db_connect()        
    
    
    
    

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

b7=Button(win,bg="black",fg="white",text="Logout",width=9,height=1,font=("Arial",14,"bold"),relief="flat",command=logout )
b7.place(x=1040,y=120)

files1=Image.open("C:\\Users\\HP\\Desktop\\Event managment\\image\\pixl.png")  # used for open image
files2=files1.resize((1150,466)) #for assign size
 
tk_image=ImageTk.PhotoImage(files2) #tk_imagee is a var name and ImageTk.PhotoImage is predefined
 
new_Label=tk.Label(win,image=tk_image) # here is image= is predefined
new_Label.place(x=50,y=170) 

show_record()

win.mainloop()