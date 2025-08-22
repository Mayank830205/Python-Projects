from tkinter import *
from PIL import Image, ImageTk
import tkinter as tk
from tkinter import ttk
import pymysql as sql
from tkinter import messagebox
import os

def Home():
    win.destroy()
    
    os.system("python menubar.py") 

def About():
    win.destroy()
    os.system("python About.py") 
    
    
def Merriage():
    win.destroy()
    os.system("python marriage.py") 
    
def Bday():
    win.destroy()
    os.system("python bdayhall.py") 

def Dance():
    win.destroy()
    os.system("python dancehall.py") 
    
    
def Viewfeedback():
    win.destroy()
    os.system("python viewfeedback.py") 
    
def Feedback():
    win.destroy()
    os.system("python Rating.py") 

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

    
def submit():
    
    a=Cent.get()
    b=Dent.get()
    c=Newvar.get()
    d=Gent.get()
    #d=Eent.get()
    if (a=="") or (b=="") or (c=="") :
        messagebox.showwarning("Warning","Please provide a valid input!!!")
    else:
        cmd=f"insert into rating(Name, Hall_Name, Rating,Customer_Review) values('{Cent.get()}','{Dent.get()}', '{Newvar.get()}','{Gent.get()}')"
        conn,cur=db_connect()      
        cur.execute(cmd)
        conn.commit()
        messagebox.showinfo("Send","Send Successfully")
        win.destroy()
      
   
    
    #os.system("python submit.py") 

win=Tk()

win.state("zoomed")
#win.state('zoomed') #output hmesha full screen me open hoga
win.config(bg="white")
files1=Image.open("C:\\Users\\HP\\Desktop\\Event managment\\image\\gift.png")  # used for open image
files2=files1.resize((1300,700)) #for assign size
 
tk_image=ImageTk.PhotoImage(files2) #tk_imagee is a var name and ImageTk.PhotoImage is predefined
 
new_Label=tk.Label(win,image=tk_image) # here is image= is predefined
new_Label.pack() 



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

b7=Button(win,bg="black",fg="white",text="Logout",width=9,height=1,font=("Arial",14,"bold"),relief="flat" ,command=logout)
b7.place(x=980,y=120)






C=Label(win,text=" Name ",fg="black",bg="white",font=("Lucida Calligraphy",16,"bold"))
C.place(x=180,y=200)

Cent=Entry(win,bg="white",width=19,font=("Lucida Calligraphy",16,"bold"))
Cent.place(x=400,y=200)

D=Label(win,text="Hall Name",fg="black",bg="white",font=("Lucida Calligraphy",16,"bold"))
D.place(x=180,y=280)

Dent=Entry(win,bg="white",width=19,font=("Lucida Calligraphy",16,"bold"))
Dent.place(x=400,y=280)

'''E=Label(win,text="Choose Hall To Feedback",fg="black",bg="white",font=("Lucida Calligraphy",16,"bold"))
E.place(x=300,y=400)

Eent=Entry(win,bg="white",width=19,font=("Lucida Calligraphy",16,"bold"))
Eent.place(x=620,y=400)
'''

F=Label(win,text="Rating",fg="black",bg="white",font=("Lucida Calligraphy",16,"bold"))
F.place(x=180,y=360)

Newvar = StringVar()
cb=ttk.Combobox(win,textvariable=Newvar)
cb['values']=('very good','good','Ok-Ok','Not Bad','Bad')
cb['state']='readonly'

cb.place(x=400,y=360)


G=Label(win,text="Customer review",fg="black",bg="white",font=("Lucida Calligraphy",16,"bold"))
G.place(x=180,y=420)

Gent=Entry(win,bg="white",width=19,font=("Lucida Calligraphy",16,"bold"))
Gent.place(x=400,y=420)


Lg=Button(win,text="Submit",bg="green",fg="white",width=7,height=1,font=("Lucida Calligraphy",16,"bold"),command=submit )
Lg.place(x=800,y=560)





win.mainloop()