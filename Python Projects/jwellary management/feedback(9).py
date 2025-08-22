from tkinter import *
from PIL import Image, ImageTk
import tkinter as tk
from tkinter import ttk
import pymysql as sql
from tkinter import messagebox
import os

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

    
def submit():
    
    name = Cent.get()
    rating = Newvar.get()
    review = Gent.get()

    if (name=="") or (rating=="") or (review=="") :
        messagebox.showwarning("Warning","Please provide a valid input!!!")
    else:
        cmd = f"INSERT INTO rating(Name, Rating, Customer_Review) VALUES ('{name}', '{rating}', '{review}')"

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
files1=Image.open("C:\\Users\\HP\\Desktop\\JWELLARY MANAGEMENT\\image\\feedback.png")  # used for open image
files2=files1.resize((1250,600)) #for assign size
 
tk_image=ImageTk.PhotoImage(files2) #tk_imagee is a var name and ImageTk.PhotoImage is predefined
 
new_Label=tk.Label(win,image=tk_image) # here is image= is predefined
new_Label.place(x=10,y=150) 



talk=Label(win,text=" JWELERY COLLECTION ❤",bg="white",fg="black",font=("Algerian",30,"bold"))
talk.place(x=370,y=30)


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








C=Label(win,text=" Name ",fg="black",bg="white",font=("Lucida Calligraphy",16,"bold"))
C.place(x=180,y=200)

Cent=Entry(win,bg="white",width=19,font=("Lucida Calligraphy",16,"bold"))
Cent.place(x=400,y=200)



F=Label(win,text="Rating",fg="black",bg="white",font=("Lucida Calligraphy",16,"bold"))
F.place(x=180,y=280)

Newvar = StringVar()
cb=ttk.Combobox(win,textvariable=Newvar)
cb['values']=('very good','good','Ok-Ok','Not Bad','Bad')
cb['state']='readonly'
#Eent=Entry(win,bg="grey",width=20,font=("Rockwell Extra Bold",18,"bold"))
cb.place(x=400,y=280)
#Fent=Entry(win,bg="white",width=19,font=("Lucida Calligraphy",16,"bold"))
#Fent.place(x=620,y=400)

G=Label(win,text="Customer review",fg="black",bg="white",font=("Lucida Calligraphy",16,"bold"))
G.place(x=180,y=360)

Gent=Entry(win,bg="white",width=19,font=("Lucida Calligraphy",16,"bold"))
Gent.place(x=400,y=360)


Lg=Button(win,text="Submit",bg="green",fg="white",width=7,height=1,font=("Lucida Calligraphy",16,"bold"),command=submit )
Lg.place(x=800,y=560)



#Sg=Button(win,text="Cencel",width=6,height=1,font=("Lucida Calligraphy",16,"bold") )
#Sg.place(x=600,y=560)


win.mainloop()