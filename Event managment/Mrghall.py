from tkinter import *
from PIL import Image, ImageTk
import tkinter as tk
from tkinter import ttk
import os
import pymysql as sql

def db_connect():
    conn=sql.connect(host='localhost',port=3306,user='root',password='',database='Event')
    cur=conn.cursor()
    return conn,cur

def show():
    a=var.get()
    if a==0: 
        # if male  salect krenge to male likha aayega
        Hall_name="City Palace in Udaipur"
    if a==1:     #if female select krenge to female lika aayega     
        Hall_name="Rambagh palace in jaipur"
    if a==2: 
        # if male  salect krenge to male likha aayega
        Hall_name="Palace Grounds in Bangalore"
    if a==3:     #if female select krenge to female lika aayega     
        Hall_name="Umaid Bhawan in Jodhpur"    
    if a==4: 
        # if male  salect krenge to male likha aayega
        Hall_name="The Leela Palace in New Delhi"
    if a==5:     #if female select krenge to female lika aayega     
        Hall_name=" The Oberoi Udaivilas in Udaipur"
    if a==6: 
        # if male  salect krenge to male likha aayega
        Hall_name="Taj Mahal Palace In Mumbai "
    if a==7:     #if female select krenge to female lika aayega     
        Hall_name="The ITC Mughal in Agra"
    if a==8: 
        # if male  salect krenge to male likha aayega
        Hall_name="The JW Marriott in Pune"
    if a==9:     #if female select krenge to female lika aayega     
        Hall_name="The Zuri White Sands in Goa"

    conn,cur=db_connect()
    cmd1 =f"delete from hall"
    cur.execute(cmd1)
    conn.commit()
    
    cmd=f"insert into hall(hallname) values('{Hall_name}')"
    cur.execute(cmd)
    conn.commit()
    
    win.destroy()
    
    os.system("python Booking.py") 
 
win=Tk()
#win.geometry("1260x700")
win.state('zoomed')
win.config(bg="white")

files1=Image.open("C:\\Users\\HP\\Desktop\\Event managment\\image\\wed1.png")  
files2=files1.resize((200,200)) 
 
tk_image=ImageTk.PhotoImage(files2) 
 
new_Label=tk.Label(win,image=tk_image) 
new_Label.place(x=20,y=120)

con=Label(win,text="...Wedding Hall...",bg="white",fg="black",font=("Lucida Calligraphy",24,"bold"))
con.place(x=400,y=10)

tx=Label(win,text="..Select Hall For Booking ..",bg="white",fg="blue",font=("Lucida Calligraphy",11,"bold"))
tx.place(x=440,y=60)

img1=Image.open("C:\\Users\\HP\\Desktop\\Event managment\\image\\wed2.png")  
img2=img1.resize((200,200)) 
 
tk_image1=ImageTk.PhotoImage(img2) 
 
new_Label1=tk.Label(win,image=tk_image1) 
new_Label1.place(x=270,y=120)

first=Image.open("C:\\Users\\HP\\Desktop\\Event managment\\image\\wed3.png")  
sec=first.resize((200,200)) 
 
tk_image2=ImageTk.PhotoImage(sec) 
 
new_Label2=tk.Label(win,image=tk_image2) 
new_Label2.place(x=530,y=120)

first1=Image.open("C:\\Users\\HP\\Desktop\\Event managment\\image\\wed4.png")  
sec2=first1.resize((200,200)) 
 
tk_image3=ImageTk.PhotoImage(sec2) 
 
new_Label3=tk.Label(win,image=tk_image3) 
new_Label3.place(x=785,y=120)

first2=Image.open("C:\\Users\\HP\\Desktop\\Event managment\\image\\wed5.png")  
sec3=first2.resize((200,200)) 
 
tk_image4=ImageTk.PhotoImage(sec3) 
 
new_Label4=tk.Label(win,image=tk_image4) 
new_Label4.place(x=1035,y=120)


file1=Image.open("C:\\Users\\HP\\Desktop\\Event managment\\image\\wed6.png")  
file2=file1.resize((200,200)) 
 
image=ImageTk.PhotoImage(file2) 
 
Label=tk.Label(win,image=image) 
Label.place(x=20,y=390)


ig1=Image.open("C:\\Users\\HP\\Desktop\\Event managment\\image\\wed7.png")  
ig2=ig1.resize((200,200)) 
 
image1=ImageTk.PhotoImage(ig2) 
 
Label1=tk.Label(win,image=image1) 
Label1.place(x=270,y=390)

nxt=Image.open("C:\\Users\\HP\\Desktop\\Event managment\\image\\wed8.png")  
xt=nxt.resize((200,200)) 
 
image2=ImageTk.PhotoImage(xt) 
 
Label2=tk.Label(win,image=image2) 
Label2.place(x=530,y=390)

nxt1=Image.open("C:\\Users\\HP\\Desktop\\Event managment\\image\\wed9.png")  
xt2=nxt1.resize((200,200)) 
 
image3=ImageTk.PhotoImage(xt2) 
 
Label3=tk.Label(win,image=image3) 
Label3.place(x=785,y=390)

nxt2=Image.open("C:\\Users\\HP\\Desktop\\Event managment\\image\\wed10.png")  
xt3=nxt2.resize((200,200)) 
 
image4=ImageTk.PhotoImage(xt3) 
 
Label4=tk.Label(win,image=image4) 
Label4.place(x=1035,y=390)

var=IntVar()    # I and V capital
radio1=Radiobutton(win,text="City Palace in Udaipur",value=1, variable= var,font=("arial",11,"bold")) 
radio1.place(x=20,y=120)

radio2=Radiobutton(win,text="Rambagh palace in jaipur",value=2, variable= var,font=("arial",11,"bold"))
radio2.place(x=270,y=120)

radio3=Radiobutton(win,text="Palace Grounds in Bangalore",value=3, variable= var,font=("arial",10,"bold")) 
radio3.place(x=530,y=120)

radio4=Radiobutton(win,text="Umaid Bhawan in Jodhpur",value=4, variable= var,font=("arial",10,"bold")) 
radio4.place(x=785,y=120)

radio5=Radiobutton(win,text="The Leela Palace in New Delhi",value=5, variable= var,font=("arial",10,"bold"))
radio5.place(x=1035,y=120)

radio6=Radiobutton(win,text="The Oberoi Udaivilas in Udaipur",value=6, variable= var,font=("arial",10,"bold"))
radio6.place(x=20,y=390)

radio7=Radiobutton(win,text="Taj Mahal Palace In Mumbai",value=7, variable= var,font=("arial",10,"bold")) 
radio7.place(x=270,y=390)

radio8=Radiobutton(win,text="The ITC Mughal in Agra",value=8, variable= var,font=("arial",11,"bold"))
radio8.place(x=530,y=390)

radio9=Radiobutton(win,text="The JW Marriott in Pune",value=9, variable= var,font=("arial",11,"bold")) 
radio9.place(x=785,y=390)

radio10=Radiobutton(win,text="The Zuri White Sands in Goa",value=10, variable= var,font=("arial",10,"bold"))
radio10.place(x=1035,y=390)






Lg=Button(win,text=" Book Now ",bg="green",fg="white",font=("Script MT Bold",11,"bold"),command=show )
Lg.place(x=1100,y=40)


win.mainloop()
 