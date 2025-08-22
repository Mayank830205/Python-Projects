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
        Hall_name="Tivoli Royal,Delhi"
    if a==1:     #if female select krenge to female lika aayega     
        Hall_name="Lamcy Banquet Hall,Bangalore"
    if a==2: 
        # if male  salect krenge to male likha aayega
        Hall_name="Sugar Business Hotel,Kochi"
    if a==3:     #if female select krenge to female lika aayega     
        Hall_name="Ajyavoo Mahal,Chennai"    
    if a==4: 
        # if male  salect krenge to male likha aayega
        Hall_name="Ajyavoo Mahal,Chennai"
    if a==5:     #if female select krenge to female lika aayega     
        Hall_name=" The JW Marriott,Pune"
    if a==6: 
        # if male  salect krenge to male likha aayega
        Hall_name="The Taj Krishna,Hyderabad "
    if a==7:     #if female select krenge to female lika aayega     
        Hall_name="The Oberoi Grand ,Kolkata"
    if a==8: 
        # if male  salect krenge to male likha aayega
        Hall_name="The Leela, Goa"
    if a==9:     #if female select krenge to female lika aayega     
        Hall_name="Wedding Opera,Delhi"

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
win.geometry("1260x700")
#win.state('zoomed')
win.config(bg="white")

files1=Image.open("C:\\Users\\HP\\Desktop\\Event managment\\image\\bday10.png")  
files2=files1.resize((200,200))  
tk_image=ImageTk.PhotoImage(files2) 
 
new_Label=tk.Label(win,image=tk_image) 
new_Label.place(x=20,y=120)

con=Label(win,text="...Birth Day Hall...",bg="white",fg="black",font=("Lucida Calligraphy",24,"bold"))
con.place(x=400,y=10)

tx=Label(win,text="..Select Hall For Booking ..",bg="white",fg="blue",font=("Lucida Calligraphy",11,"bold"))
tx.place(x=440,y=60)

img1=Image.open("C:\\Users\\HP\\Desktop\\Event managment\\image\\bda1.png")  
img2=img1.resize((200,200))  
tk_image1=ImageTk.PhotoImage(img2) 
 
new_Label1=tk.Label(win,image=tk_image1) 
new_Label1.place(x=270,y=120)

first=Image.open("C:\\Users\\HP\\Desktop\\Event managment\\image\\bday2.png")  
sec=first.resize((200,200))  
tk_image2=ImageTk.PhotoImage(sec) 
 
new_Label2=tk.Label(win,image=tk_image2) 
new_Label2.place(x=530,y=120)

first1=Image.open("C:\\Users\\HP\\Desktop\\Event managment\\image\\bday3.png")  
sec2=first1.resize((200,200))  
tk_image3=ImageTk.PhotoImage(sec2) 
 
new_Label3=tk.Label(win,image=tk_image3) 
new_Label3.place(x=785,y=120)

first2=Image.open("C:\\Users\\HP\\Desktop\\Event managment\\image\\bday4.png")  
sec3=first2.resize((200,200))  
tk_image4=ImageTk.PhotoImage(sec3) 
 
new_Label4=tk.Label(win,image=tk_image4) 
new_Label4.place(x=1035,y=120)


file1=Image.open("C:\\Users\\HP\\Desktop\\Event managment\\image\\bday5.png")  
file2=file1.resize((200,200))  
image=ImageTk.PhotoImage(file2) 
 
Label=tk.Label(win,image=image) 
Label.place(x=20,y=390)


ig1=Image.open("C:\\Users\\HP\\Desktop\\Event managment\\image\\bday6.png")  
ig2=ig1.resize((200,200))  
image1=ImageTk.PhotoImage(ig2) 
 
Label1=tk.Label(win,image=image1) 
Label1.place(x=270,y=390)

nxt=Image.open("C:\\Users\\HP\\Desktop\\Event managment\\image\\bday7.png")  
xt=nxt.resize((200,200))  
image2=ImageTk.PhotoImage(xt) 
 
Label2=tk.Label(win,image=image2) 
Label2.place(x=530,y=390)

nxt1=Image.open("C:\\Users\\HP\\Desktop\\Event managment\\image\\bday8.png")  
xt2=nxt1.resize((200,200))  
image3=ImageTk.PhotoImage(xt2) 
 
Label3=tk.Label(win,image=image3) 
Label3.place(x=785,y=390)

nxt2=Image.open("C:\\Users\\HP\\Desktop\\Event managment\\image\\bday9.png")  
xt3=nxt2.resize((200,200))  
image4=ImageTk.PhotoImage(xt3) 
 
Label4=tk.Label(win,image=image4) 
Label4.place(x=1035,y=390)
 
   # I and V capital
var=IntVar()
radio1=Radiobutton(win,text="Tivoli Royal,Delhi",value=0, variable= var,font=("arial",11,"bold")) 
radio1.place(x=20,y=120)


radio2=Radiobutton(win,text="Lamcy Banquet Hall,Bangalore",value=1, variable= var,font=("arial",10,"bold"))
radio2.place(x=270,y=120)


radio3=Radiobutton(win,text="Sugar Business Hotel,Kochi",value=2, variable= var,font=("arial",10,"bold")) 
radio3.place(x=530,y=120)


radio4=Radiobutton(win,text="Ajyavoo Mahal,Chennai",value=3, variable= var,font=("arial",11,"bold")) 
radio4.place(x=785,y=120)


radio5=Radiobutton(win,text="The Leela Palace,Mumbai",value=4, variable= var,font=("arial",10,"bold"))
radio5.place(x=1035,y=120)


radio6=Radiobutton(win,text="The JW Marriott,Pune",value=5, variable= var,font=("arial",11,"bold"))
radio6.place(x=20,y=390)


radio7=Radiobutton(win,text="The Taj Krishna,Hyderabad",value=6, variable= var,font=("arial",10,"bold")) 
radio7.place(x=270,y=390)


radio8=Radiobutton(win,text="The Oberoi Grand ,Kolkata",value=7, variable= var,font=("arial",10,"bold"))
radio8.place(x=530,y=390)


radio9=Radiobutton(win,text="The Leela, Goa",value=8, variable= var,font=("arial",11,"bold")) 
radio9.place(x=785,y=390)


radio10=Radiobutton(win,text="Wedding Opera,Delhi",value=9, variable= var,font=("arial",11,"bold"))
radio10.place(x=1035,y=390)






Lg=Button(win,text=" Book Now ",bg="green",fg="white",font=("Script MT Bold",11,"bold"),command=show )
Lg.place(x=1100,y=40)

win.mainloop()
 