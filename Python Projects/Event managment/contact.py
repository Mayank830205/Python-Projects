from tkinter import *
from PIL import Image, ImageTk
import tkinter as tk
from tkinter import ttk
import pymysql as sql
from tkinter import messagebox
import os
 
def click(e): 
    if name_var.get()=="Name...":
        name_var.set('')  

def leave(e): 
    if name_var.get()=="":
        name_var.set("Name...") 
    
def email_in(e):
    if email_var.get()=="Email...":
        email_var.set('')

def lea(e):
    if email_var.get()=="":
        email_var.set("Email...") 

def enter(e):
    if sub_var.get()=="Subject...":
        sub_var.set('')
def go(e):
    if sub_var.get()=="":
        sub_var.set("Subject...")
        
                 
def on(e):
    if msg_var.get()=="Message...":
        msg_var.set('')
def off(e):
    if msg_var.get()=="":
        msg_var.set("Message...")       
        
        
def db_connect():
    conn=sql.connect(host='localhost',port=3306,user='root',password='',database='Event')
    cur=conn.cursor()
    return conn,cur

    
def submit():
    a=name_var.get()
    b=email_var.get()
    c=sub_var.get()
    d=msg_var.get()
    if (a=="Name...") or (b=="Email...") or (c=="Subject...") or (d=="Message..."):
        messagebox.showwarning("Warning","Please provide a valid input!!!")
    else:
        cmd=f"insert into contactme(Name, Email, Subject , Message) values('{name_var.get()}', '{email_var.get()}','{sub_var.get()}','{msg_var.get()}')"
        conn,cur=db_connect()    
        cur.execute(cmd)
        conn.commit()
        messagebox.showinfo("Send","Send Successfully")
        win.destroy()
      


win=Tk()

win.geometry("940x550")
#win.state('zoomed')
win.config(bg="white")

files1=Image.open("C:\\Users\\HP\\Desktop\\Event managment\\image\\contact.png")  # used for open image
files2=files1.resize((1000,550)) #for assign size
 
tk_image=ImageTk.PhotoImage(files2) #tk_imagee is a var name and ImageTk.PhotoImage is predefined
 
new_Label=tk.Label(win,image=tk_image) # here is image= is predefined
new_Label.pack()

con=Label(win,text="🙏...Contact...🙏",bg="white",fg="black",font=("Lucida Calligraphy",28,"bold"))
con.place(x=370,y=60)


name_var=StringVar()
name_var.set('Name...')
name = Entry(win, width=18,font=("Lucida Calligraphy",16,"bold"),textvariable=name_var) 
# Add text in Entry box 
name.place(x=350,y=200) 
# Use bind method 
name.bind("<FocusIn>",click) 
name.bind("<FocusOut>",leave) 

  
#2 Add Entry Box 
email_var=StringVar()
email_var.set('Email...')
email = Entry(win, width=18,font=("Lucida Calligraphy",16,"bold"),textvariable=email_var) 
# Add text in Entry box 
email.place(x=640,y=200) 
# Use bind method 
email.bind("<FocusIn>>",email_in) 
email.bind("<FocusOut>",lea) 
    
  
# 3Add Entry Box 
#sub = Entry(win, width=40,font=("Lucida Calligraphy",16,"bold")) 
sub_var=StringVar()
sub_var.set('Subject...')
sub = Entry(win, width=30,font=("Lucida Calligraphy",16,"bold"),textvariable=sub_var)  
# Add text in Entry box 
sub.place(x=350,y=250) 
# Use bind method 
sub.bind("<FocusIn>>", enter) 
sub.bind("<FocusOut>", go) 

# 4 Add Entry Box 
#msg= Entry(win, width=40,font=("Lucida Calligraphy",16,"bold"))
msg_var=StringVar()
msg_var.set('Message...')
msg = Entry(win, width=18,font=("Lucida Calligraphy",16,"bold"),textvariable=msg_var)   
# Add text in Entry box 
msg.place(x=350,y=300) 
  # Use bind method 
msg.bind("<FocusIn>>",on) 
msg.bind("<FocusOut>",off) 
  
c3=Button(win,bg="green",fg="white",text="Send",width=7,height=1,font=("Arial",14,"bold"),relief="flat",command=submit )
c3.place(x=700,y=350)
  
  
det=Label(win,text="india \n Phone -1234567890 \n Subject- contact to management \n Email- abc@gmail.com",bg="white",fg="black",font=("Lucida Calligraphy",12,"bold"))
det.place(x=600,y=430)



win.mainloop()