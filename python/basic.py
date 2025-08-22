from tkinter import *
import tkinter as tk      # tinker add kiya hai

def show():
    a=ent.get()
    b=ent1.get()
    
    # ager ham by default string print krana chahte hai to hame int  nhi lgana direct #lbl4.config(text=a+b) lgana hai
    
    c=int(a)+int(b)
    lbl4.config(text=c)

win =Tk()       # tinker library ka  variable name declare kiya he "Tk" me hmesha T capital hoga
win.title("my program") # for tittle on screen


win.geometry("550x766")  #width X hieght
        #or
#win.maxsize(width=600,height=600)
#win.minsize(width=400,height=200)
     #//
     
win.config(bg="blue")

win.iconbitmap("Safe-icon.ico")

lbl1=Label(win,text="Name",bg="blue",fg="white",font=("Arial",18,"bold"))
lbl1.place(x=100,y=200)

ent=Entry(win,font=("Arial",18,"bold"))
ent.place(x=200,y=200)

lbl2=Label(win,text="Marks",bg="blue",fg="white",font=("Arial",18,"bold"))
lbl2.place(x=100,y=300)

ent1=Entry(win,font=("Arial",18,"bold"))
ent1.place(x=200,y=300)

btn=Button(win,text="Save",width=15,height=1,font=("Arial",18,"bold") ,command=show)
btn.place(x=150,y=400)

lbl3=Label(win,text="Output",bg="blue",fg="white",font=("Arial",18,"bold"))
lbl3.place(x=100,y=500)

lbl4=Label(win,bg="white",font=("Arial",18,"bold"))
lbl4.place(x=300,y=500)
win.mainloop()    #work like getch()