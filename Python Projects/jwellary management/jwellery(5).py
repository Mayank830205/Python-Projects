from tkinter import *
from PIL import Image, ImageTk
import tkinter as tk
from tkinter import ttk
import os
import pymysql as sql

def db_connect():
    conn=sql.connect(host='localhost',port=3306,user='root',password='',database='jwellery')
    cur=conn.cursor()
    return conn,cur


def show():
    win.destroy()
    os.system("python booking(6).py") 
    
 
win=Tk()
win.geometry("1260x700")
#win.state('zoomed')
win.config(bg="white")

files1=Image.open("C:\\Users\\HP\\Desktop\\JWELLARY MANAGEMENT\\image\\img10.png")  
files2=files1.resize((200,200))  
tk_image=ImageTk.PhotoImage(files2) 
 
new_Label=tk.Label(win,image=tk_image) 
new_Label.place(x=20,y=120)

con=Label(win,text="...JWELERY COLLECTION...",bg="white",fg="black",font=("Lucida Calligraphy",24,"bold"))
con.place(x=370,y=10)

tx=Label(win,text="..Select Jwellery For Booking ..",bg="white",fg="blue",font=("Lucida Calligraphy",11,"bold"))
tx.place(x=480,y=60)

img1=Image.open("C:\\Users\\HP\\Desktop\\JWELLARY MANAGEMENT\\image\\img9.png")  
img2=img1.resize((200,200))  
tk_image1=ImageTk.PhotoImage(img2) 
 
new_Label1=tk.Label(win,image=tk_image1) 
new_Label1.place(x=270,y=120)

first=Image.open("C:\\Users\\HP\\Desktop\\JWELLARY MANAGEMENT\\image\\img8.png")  
sec=first.resize((200,200))  
tk_image2=ImageTk.PhotoImage(sec) 
 
new_Label2=tk.Label(win,image=tk_image2) 
new_Label2.place(x=530,y=120)

first1=Image.open("C:\\Users\\HP\\Desktop\\JWELLARY MANAGEMENT\\image\\img7.png")  
sec2=first1.resize((200,200))  
tk_image3=ImageTk.PhotoImage(sec2) 
 
new_Label3=tk.Label(win,image=tk_image3) 
new_Label3.place(x=785,y=120)

first2=Image.open("C:\\Users\\HP\\Desktop\\JWELLARY MANAGEMENT\\image\\img6.png")  
sec3=first2.resize((200,200))  
tk_image4=ImageTk.PhotoImage(sec3) 
 
new_Label4=tk.Label(win,image=tk_image4) 
new_Label4.place(x=1035,y=120)


file1=Image.open("C:\\Users\\HP\\Desktop\\JWELLARY MANAGEMENT\\image\\img5.png")  
file2=file1.resize((200,200))  
image=ImageTk.PhotoImage(file2) 
 
Label=tk.Label(win,image=image) 
Label.place(x=20,y=390)


ig1=Image.open("C:\\Users\\HP\\Desktop\\JWELLARY MANAGEMENT\\image\\img4.png")  
ig2=ig1.resize((200,200))  
image1=ImageTk.PhotoImage(ig2) 
 
Label1=tk.Label(win,image=image1) 
Label1.place(x=270,y=390)

nxt=Image.open("C:\\Users\\HP\\Desktop\\JWELLARY MANAGEMENT\\image\\img1.png")  
xt=nxt.resize((200,200))  
image2=ImageTk.PhotoImage(xt) 
 
Label2=tk.Label(win,image=image2) 
Label2.place(x=530,y=390)

nxt1=Image.open("C:\\Users\\HP\\Desktop\\JWELLARY MANAGEMENT\\image\\img2.png")  
xt2=nxt1.resize((200,200))  
image3=ImageTk.PhotoImage(xt2) 
 
Label3=tk.Label(win,image=image3) 
Label3.place(x=785,y=390)

nxt2=Image.open("C:\\Users\\HP\\Desktop\\JWELLARY MANAGEMENT\\image\\img3.png")  
xt3=nxt2.resize((200,200))  
image4=ImageTk.PhotoImage(xt3) 
 
Label4=tk.Label(win,image=image4) 
Label4.place(x=1035,y=390)
 
   # I and V capital
var=IntVar()
radio1=Radiobutton(win,text="5.8 Lakh /-",value=0, variable= var,font=("arial",11,"bold")) 
radio1.place(x=20,y=120)


radio2=Radiobutton(win,text="7.3 Lakh /-",value=1, variable= var,font=("arial",10,"bold"))
radio2.place(x=270,y=120)


radio3=Radiobutton(win,text=" 6.2 Lakh /-",value=2, variable= var,font=("arial",10,"bold")) 
radio3.place(x=530,y=120)


radio4=Radiobutton(win,text="12.3 Lakh /-",value=3, variable= var,font=("arial",11,"bold")) 
radio4.place(x=785,y=120)


radio5=Radiobutton(win,text="14.0 Lakh /-",value=4, variable= var,font=("arial",10,"bold"))
radio5.place(x=1035,y=120)


radio6=Radiobutton(win,text="24.3 Lakh /- ",value=5, variable= var,font=("arial",11,"bold"))
radio6.place(x=20,y=390)


radio7=Radiobutton(win,text="17.3 Lakh /- ",value=6, variable= var,font=("arial",10,"bold")) 
radio7.place(x=270,y=390)


radio8=Radiobutton(win,text=" 2.9 Lakh /-",value=7, variable= var,font=("arial",10,"bold"))
radio8.place(x=530,y=390)


radio9=Radiobutton(win,text="9.3 Lakh /-",value=8, variable= var,font=("arial",11,"bold")) 
radio9.place(x=785,y=390)


radio10=Radiobutton(win,text="14.3 Lakh /-",value=9, variable= var,font=("arial",11,"bold"))
radio10.place(x=1035,y=390)






Lg=Button(win,text=" Book Now ",bg="green",fg="white",font=("Script MT Bold",11,"bold"),command=show )
Lg.place(x=1100,y=40)

win.mainloop()
 