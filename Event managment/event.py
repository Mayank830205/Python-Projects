from tkinter import *
from PIL import Image, ImageTk
import tkinter as tk
from tkinter import ttk


win=Tk()

win.geometry("950x500")
#win.state('zoomed')

win.config(bg="white")

talk=Label(win,text="EVENT MANAGMENT",bg="white",fg="navy",font=("Algerian",28,"bold"))
talk.place(x=280,y=30)

about=Label(win,text="your silence will event management",bg="white",fg="grey",font=("Algerian",11,"bold"))
about.place(x=290,y=85)

files1=Image.open("C:\\Users\\HP\\Desktop\\Event managment\\image\\mrg.png")  # used for open image
files2=files1.resize((200,200)) #for assign size
 
tk_image1=ImageTk.PhotoImage(files2) #tk_imagee is a var name and ImageTk.PhotoImage is predefined
 
new_Label1=tk.Label(win,image=tk_image1) # here is image= is predefined
new_Label1.place(x=150,y=140) 

mrg1=Label(win,text=" Merriage Event",bg="white",fg="black",font=("Algerian",16,"bold"))
mrg1.place(x=150,y=350)  

mrg2=Label(win,text="Founded : 12 Dec 2002",bg="white",fg="grey",font=("Algerian",10,"bold"))
mrg2.place(x=160,y=380)  

sec1=Image.open("C:\\Users\\HP\\Desktop\\Event managment\\image\\bday.png")  # used for open image
sec2=sec1.resize((200,200)) #for assign size
 
tk_image2=ImageTk.PhotoImage(sec2) #tk_imagee is a var name and ImageTk.PhotoImage is predefined
 
new_Label2=tk.Label(win,image=tk_image2) # here is image= is predefined
new_Label2.place(x=370,y=190) 

bdy1=Label(win,text=" BirthDay Event",bg="white",fg="black",font=("Algerian",16,"bold"))
bdy1.place(x=370,y=400)  

bdy2=Label(win,text="Founded : 2002",bg="white",fg="grey",font=("Algerian",10,"bold"))
bdy2.place(x=400,y=420)  


third1=Image.open("C:\\Users\\HP\\Desktop\\Event managment\\image\\dance.png")  # used for open image
third2=third1.resize((200,200)) #for assign size
 
tk_image3=ImageTk.PhotoImage(third2) #tk_imagee is a var name and ImageTk.PhotoImage is predefined
 
new_Label3=tk.Label(win,image=tk_image3) # here is image= is predefined
new_Label3.place(x=590,y=140) 

dnc1=Label(win,text="Dance Show Event",bg="white",fg="black",font=("Algerian",15,"bold"))
dnc1.place(x=590,y=350)  

dnc2=Label(win,text="Founded : 2 Dec 2007",bg="white",fg="grey",font=("Algerian",10,"bold"))
dnc2.place(x=610,y=380)  


win.mainloop()