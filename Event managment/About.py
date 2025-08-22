from tkinter import *
from PIL import Image, ImageTk
import tkinter as tk
from tkinter import ttk


win=Tk()

win.geometry("900x600")
#win.state('zoomed')
win.config(bg="white")


files1=Image.open("C:\\Users\\HP\\Desktop\\Event managment\\image\\ab.png")  # used for open image
files2=files1.resize((900,600)) #for assign size
 
tk_image=ImageTk.PhotoImage(files2) #tk_imagee is a var name and ImageTk.PhotoImage is predefined
 
new_Label=tk.Label(win,image=tk_image) # here is image= is predefined
new_Label.place(x=0,y=10)

talk=Label(win,text="EVENT MANAGMENT",bg="white",fg="navy",font=("Algerian",28,"bold"))
talk.place(x=450,y=50)

about=Label(win,text="about",bg="white",fg="grey",font=("Algerian",18,"bold"))
about.place(x=570,y=100)

theory=Label(win,text="The Event Management System is a cutting-edge platform\n designed to simplify and enhance the planning and \n  execution of various events, including corporate meetings, weddings, \n parties, and other special occasions. \n This system acts as a one-stop solution for event \n organizers, clients, and \n vendors, offering seamless collaboration and streamlined operations. \nWith features like online event scheduling, vendor management, \n budget tracking, and \n automated notifications, the platform ensures that every \naspect of event planning is handled efficiently\n. Users can explore customizable packages, book \n services, and monitor event progress through an intuitive  \n interfaceThe system is built with a focus on \n user-friendliness, scalability, and security, making it \n accessible and reliable for individual users and businesses \n alike. By automating routine tasks and providing real-time \n updates, the platform reduces workload, \n minimizes errors, and ensures a smooth planning experience.",bg="white",fg="black",font=("Arial",12,"bold"))
theory.place(x=350,y=170)


win.mainloop()