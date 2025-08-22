from tkinter import *
from PIL import Image, ImageTk
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
from tkinter import messagebox
import pymysql as sql
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
    


def submit():
    messagebox.showinfo("Submit","Submit Successfully")
    
def db_connect():
    conn=sql.connect(host='localhost',port=3306,user='root',password='',database='jwellery')
    cur=conn.cursor()
    return conn,cur

    
def submit():
    a=Cent.get()
    b=Newvar2.get()
    c=Gent.get()
    #d=Eent.get()
    if (a=="") or (b=="") or (c=="") :
        messagebox.showwarning("Warning","Please provide a valid input!!!")
    else:
        cmd=f"insert into payment(Customer_Name, Payment_method, Amount) values('{Cent.get()}', '{Newvar2.get()}','{Gent.get()}')"
        conn,cur=db_connect()      
        cur.execute(cmd)
        conn.commit()
        messagebox.showinfo("Send","Send Successfully")
        win.destroy()
    
win=Tk()

#win.geometry("1000x700")
win.state('zoomed')
win.config(bg="white")

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




files1=Image.open("C:\\Users\\HP\\Desktop\\JWELLARY MANAGEMENT\\image\\feed.png")  # used for open image
files2=files1.resize((1150,466)) #for assign size
 
tk_image=ImageTk.PhotoImage(files2) #tk_imagee is a var name and ImageTk.PhotoImage is predefined
 
new_Label=tk.Label(win,image=tk_image) # here is image= is predefined
new_Label.place(x=50,y=170) 


Blank=Label(win,bg="white",fg="black",width=38,height=12,font=("Arial",22,"bold"))
Blank.place(x=260,y=197)


C=Label(win,text="Customer Name",bg="white",fg="black",font=("Script MT Bold",19,"bold"))
C.place(x=350,y=250)

Cent=Entry(win,bg="white",width=20,font=("Script MT Bold",19,"bold"))
Cent.place(x=350,y=300)




F=Label(win,text="Payment Method",bg="white",fg="black",font=("Script MT Bold",19,"bold"))
F.place(x=350,y=350)
Newvar2 = StringVar()
F=ttk.Combobox(win,textvariable=Newvar2)
F['values']=('UPI','Credit card','Debit Card')
F['state']='readonly'
F.place(x=350,y=400)

G=Label(win,text="Amount",bg="white",fg="black",font=("Script MT Bold",19,"bold"))
G.place(x=350,y=450)

Gent=Entry(win,bg="white",width=20,font=("Script MT Bold",19,"bold"))
Gent.place(x=350,y=500)



Lg=Button(win,text="Submit",bg="green",fg="white",font=("Rockwell Extra Bold",14,"bold"),command=submit )
Lg.place(x=780,y=550)


win.mainloop()