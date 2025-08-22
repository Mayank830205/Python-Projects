from tkinter import *
from PIL import Image, ImageTk
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import os

def Home():
    #win.destroy()
    
    os.system("python menubar.py") 

def About():
    #win.destroy()
    os.system("python About.py") 
    
    
def Merriage():
    #win.destroy()
    os.system("python Mrghall.py") 
    
def Bday():
    #win.destroy()
    os.system("python bdayhall.py") 

def Dance():
    #win.destroy()
    os.system("python dancehall.py") 
    
    
def Viewfeedback():
    #win.destroy()
    os.system("python viewfeedback.py") 
    
def Feedback():
    #win.destroy()
    os.system("python Rating.py") 

def Customer():
    #win.destroy()
    os.system("python Customeroder.py") 
    
    
def Event():
    #win.destroy()
    os.system("python event.py")     
    
def Contact():
    #win.destroy()
    os.system("python contact.py") 
    
    


def logout():
    # Display a confirmation message
    confirm = messagebox.askyesno("Logout", "Are you sure you want to logout?")
    if confirm:
        # Close the application or redirect to login screen
        win.destroy()  # This closes the Tkinter window
        # Alternatively, you can redirect to the login screen by calling another function

# Main application logic
#if __name__ == "__main__":
    
    


win=Tk()

#win.geometry("1000x900")
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

b6=Button(win,bg="black",fg="white",text="View Feedback",width=11,height=1,font=("Arial",14,"bold"),relief="flat",command=Viewfeedback )
b6.place(x=690,y=120)

b7=Button(win,bg="black",fg="white",text="Feedback",width=9,height=1,font=("Arial",14,"bold"),relief="flat" ,command=Feedback)
b7.place(x=855,y=120)

b7=Button(win,bg="black",fg="white",text="Logout",width=9,height=1,font=("Arial",14,"bold"),relief="flat" ,command=logout)
b7.place(x=980,y=120)


blank2=Label(win,fg="white",bg="black",width=70,height=1,font=("Arial",22,"bold"))
blank2.place(x=4,y=180)

c1=Button(win,bg="black",fg="white",text="Customer Booking",width=16,height=1,font=("Arial",14,"bold"),relief="flat",command=Customer )
c1.place(x=10,y=180)

c2=Button(win,bg="black",fg="white",text="Event Management",width=17,height=1,font=("Arial",14,"bold"),relief="flat",command=Event )
c2.place(x=210,y=180)

c3=Button(win,bg="black",fg="white",text="Contact",width=8,height=1,font=("Arial",14,"bold"),relief="flat",command=Contact )
c3.place(x=420,y=180)

files1=Image.open("C:\\Users\\HP\\Desktop\\Event managment\\image\\wel.png")  # used for open image
files2=files1.resize((1100,380)) #for assign size
 
tk_image=ImageTk.PhotoImage(files2) #tk_imagee is a var name and ImageTk.PhotoImage is predefined
 
new_Label=tk.Label(win,image=tk_image) # here is image= is predefined
new_Label.place(x=100,y=250) 



#evt=Label(win,text="⭐EVENT MANAGMENT⭐",bg="white",fg="black",font=("Algerian",28,"bold"))
#evt.place(x=20,y=30)



win.mainloop()