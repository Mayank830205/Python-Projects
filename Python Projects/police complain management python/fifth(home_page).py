from tkinter import *
from PIL import Image, ImageTk
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import os

def Home():
    #win.destroy()
    
    os.system("python fifth(home_page).py") 

def About():
    #win.destroy()
    os.system("python nine(about).py") 
    
    
def report():
    #win.destroy()
    os.system("python seven(report).py") 
    
def management():
    #win.destroy()
    os.system("python eight(management).py") 

def maping():
    #win.destroy()
    os.system("python six(crime_maping).py") 
    
    
 
    
    


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




talk=Label(win,text="POLICE DEPARTMENT  👮‍♂️",bg="white",fg="black",font=("Algerian",30,"bold"))
talk.place(x=370,y=30)

blank=Label(win,fg="white",bg="black",width=70,height=1,font=("Arial",22,"bold"))
blank.place(x=4,y=120)

b1=Button(win,bg="black",fg="white",text="Home",width=7,height=1,font=("Arial",14,"bold"),relief="flat",command=Home)
b1.place(x=15,y=120)

b2=Button(win,bg="black",fg="white",text="About",width=7,height=1,font=("Arial",14,"bold"),relief="flat",command=About)
b2.place(x=140,y=120)

b3=Button(win,bg="black",fg="white",text="Crime Reporting",width=14,height=1,font=("Arial",14,"bold"),relief="flat", command=report )
b3.place(x=260,y=120)

b4=Button(win,bg="black",fg="white",text="Case Management",width=14,height=1,font=("Arial",14,"bold"),relief="flat",command=management )
b4.place(x=480,y=120)

b5=Button(win,bg="black",fg="white",text="Crime Mapping",width=11,height=1,font=("Arial",14,"bold"),relief="flat",command=maping )
b5.place(x=730,y=120)




b7=Button(win,bg="black",fg="white",text="Logout",width=9,height=1,font=("Arial",14,"bold"),relief="flat" ,command=logout)
b7.place(x=910,y=120)




files1=Image.open("C:\\Users\\HP\\Desktop\\police complain management python\\image\\hom.png")  # used for open image
files2=files1.resize((1215,480)) #for assign size
 
tk_image=ImageTk.PhotoImage(files2) #tk_imagee is a var name and ImageTk.PhotoImage is predefined
 
new_Label=tk.Label(win,image=tk_image) # here is image= is predefined
new_Label.place(x=30,y=165) 



#evt=Label(win,text="⭐EVENT MANAGMENT⭐",bg="white",fg="black",font=("Algerian",28,"bold"))
#evt.place(x=20,y=30)



win.mainloop()