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
        
        Hall_name="Sangeet Vidya Niketan, Delhi"
    if a==1:      
        Hall_name="The Leela Palace,Mumbai"
    if a==2: 
       
        Hall_name="Delhi Dance Academy,Bangalore"
    if a==3:     
        Hall_name="The Music Academy,Chennai"    
    if a==4: 
        
        Hall_name="Ravindra Bharathi,Hyderabad"
    if a==5:     
        Hall_name="Bal Gandharva Rang Mandir,Pune"
    if a==6: 
        
        Hall_name="Jawahar Kala Kendra,Jaipur"
    if a==7:    
        Hall_name="Kala Academy,Goa"
    if a==8: 
       
        Hall_name="Tagore Theatre,Chandigarh"
    if a==9:     
        Hall_name="Rabindra Sadan,Kolkata"

    conn,cur=db_connect()
    cmd1 =f"delete from hall"
    cur.execute(cmd1)
    conn.commit()
    
    cmd=f"insert into hall(hallname) values('{Hall_name}')"
    cur.execute(cmd)
    conn.commit()
    
    
    win.destroy()
    os.system("python Booking.py") 


'''def show():
    win.destroy()
    
    os.system("python Booking.py")''' 
 
win=Tk()
win.geometry("1260x700")
#win.state('zoomed')
win.config(bg="white")

files1=Image.open("C:\\Users\\HP\\Desktop\\Event managment\\image\\dnc10.png")  
files2=files1.resize((200,200)) 
 
tk_image=ImageTk.PhotoImage(files2) 
 
new_Label=tk.Label(win,image=tk_image) 
new_Label.place(x=20,y=120)

con=Label(win,text="...Dance Hall...",bg="white",fg="black",font=("Lucida Calligraphy",24,"bold"))
con.place(x=400,y=10)

tx=Label(win,text="..Select Hall For Booking ..",bg="white",fg="blue",font=("Lucida Calligraphy",10,"bold"))
tx.place(x=440,y=60)

img1=Image.open("C:\\Users\\HP\\Desktop\\Event managment\\image\\dnc1.png")  
img2=img1.resize((200,200)) 
 
tk_image1=ImageTk.PhotoImage(img2) 
 
new_Label1=tk.Label(win,image=tk_image1) 
new_Label1.place(x=270,y=120)

first=Image.open("C:\\Users\\HP\\Desktop\\Event managment\\image\\dnc2.png")  
sec=first.resize((200,200)) 
 
tk_image2=ImageTk.PhotoImage(sec) 
 
new_Label2=tk.Label(win,image=tk_image2) 
new_Label2.place(x=530,y=120)

first1=Image.open("C:\\Users\\HP\\Desktop\\Event managment\\image\\dnc3.png")  
sec2=first1.resize((200,200)) 
 
tk_image3=ImageTk.PhotoImage(sec2) 
 
new_Label3=tk.Label(win,image=tk_image3) 
new_Label3.place(x=785,y=120)

first2=Image.open("C:\\Users\\HP\\Desktop\\Event managment\\image\\dnc4.png")  
sec3=first2.resize((200,200)) 
 
tk_image4=ImageTk.PhotoImage(sec3) 
 
new_Label4=tk.Label(win,image=tk_image4) 
new_Label4.place(x=1035,y=120)


file1=Image.open("C:\\Users\\HP\\Desktop\\Event managment\\image\\dnc5.png")  
file2=file1.resize((200,200)) 
 
image=ImageTk.PhotoImage(file2) 
 
Label=tk.Label(win,image=image) 
Label.place(x=20,y=390)


ig1=Image.open("C:\\Users\\HP\\Desktop\\Event managment\\image\\dnc6.png")  
ig2=ig1.resize((200,200)) 
 
image1=ImageTk.PhotoImage(ig2) 
 
Label1=tk.Label(win,image=image1) 
Label1.place(x=270,y=390)

nxt=Image.open("C:\\Users\\HP\\Desktop\\Event managment\\image\\dnc7.png")  
xt=nxt.resize((200,200)) 
 
image2=ImageTk.PhotoImage(xt) 
 
Label2=tk.Label(win,image=image2) 
Label2.place(x=530,y=390)

nxt1=Image.open("C:\\Users\\HP\\Desktop\\Event managment\\image\\dnc8.png")  
xt2=nxt1.resize((200,200)) 
 
image3=ImageTk.PhotoImage(xt2) 
 
Label3=tk.Label(win,image=image3) 
Label3.place(x=785,y=390)

nxt2=Image.open("C:\\Users\\HP\\Desktop\\Event managment\\image\\dnc9.png")  
xt3=nxt2.resize((200,200)) 
 
image4=ImageTk.PhotoImage(xt3) 
 
Label4=tk.Label(win,image=image4) 
Label4.place(x=1035,y=390)
    # I and V capital
var=IntVar()
radio1=Radiobutton(win,text="Sangeet Vidya Niketan, Delhi",value=1, variable= var,font=("arial",10,"bold")) 
radio1.place(x=20,y=120)

radio2=Radiobutton(win,text="The Leela Palace,Mumbai",value=2, variable= var,font=("arial",10,"bold"))
radio2.place(x=270,y=120)

radio3=Radiobutton(win,text="Delhi Dance Academy,Bangalore",value=3, variable= var,font=("arial",9,"bold")) 
radio3.place(x=530,y=120)

radio4=Radiobutton(win,text="The Music Academy,Chennai",value=4, variable= var,font=("arial",10,"bold")) 
radio4.place(x=785,y=120)

radio5=Radiobutton(win,text="Ravindra Bharathi,Hyderabad",value=5, variable= var,font=("arial",9,"bold"))
radio5.place(x=1035,y=120)

radio6=Radiobutton(win,text="Bal Gandharva Rang Mandir,Pune",value=6, variable= var,font=("arial",9,"bold"))
radio6.place(x=20,y=390)

radio7=Radiobutton(win,text="Jawahar Kala Kendra,Jaipur",value=7, variable= var,font=("arial",9,"bold")) 
radio7.place(x=270,y=390)

radio8=Radiobutton(win,text="Kala Academy,Goa",value=8, variable= var,font=("arial",10,"bold"))
radio8.place(x=530,y=390)

radio9=Radiobutton(win,text="Tagore Theatre,Chandigarh",value=9, variable= var,font=("arial",10,"bold")) 
radio9.place(x=785,y=390)


radio10=Radiobutton(win,text="Rabindra Sadan,Kolkata",value=10, variable= var,font=("arial",10,"bold"))
radio10.place(x=1035,y=390)






Lg=Button(win,text=" Book Now ",bg="green",fg="white",font=("Script MT Bold",10,"bold") ,command=show )
Lg.place(x=1100,y=40)


win.mainloop()
 