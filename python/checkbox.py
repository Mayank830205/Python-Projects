from tkinter import *
import tkinter as tk      # tinker add kiya hai
from tkinter import ttk

def show():
    
    a=ent.get()
    b=ent1.get()
    c=cb.get()
    
    
    # ager ham by default string print krana chahte hai to hame int  nhi lgana direct #lbl4.config(text=a+b) lgana hai
    if c=="Sum":
        c=int(a)+int(b)
        lbl4.config(text=c)
    elif c=="Sub":
        c=int(a)-int(b)
        lbl4.config(text=c)
    elif c=="Mul":
        c=int(a)*int(b)
        lbl4.config(text=c)   
    elif c=="Div":
        c=int(a)/int(b)
        lbl4.config(text=c)
    elif c=="Mod":
        c=int(a)%int(b)
        lbl4.config(text=c)
    else :
        lbl4.config(text="invalid")    
win =Tk()       # tinker library ka  variable name declare kiya he "Tk" me hmesha T capital hoga
win.title("my program") # for tittle on screen


win.geometry("590x766")  #width X hieght
        #or
#win.maxsize(width=600,height=600)
#win.minsize(width=400,height=200)
     #//
     
win.config(bg="BLACK")

win.iconbitmap("Safe-icon.ico")

lbl=Label(win,text="PERFORM ARITHMETIC OPERATION", bg="black",fg="red",font=("Rockwell Extra Bold",17,"bold","underline"))
lbl.place(x=60,y=100)

lbl1=Label(win,text="Number 1",bg="black",fg="white",font=("Calibri",18,"bold"))
lbl1.place(x=100,y=200)

ent=Entry(win,font=("Calibri",18,"bold"))
ent.place(x=230,y=200)

lbl2=Label(win,text="Number 2",bg="black",fg="white",font=("Calibri",18,"bold"))
lbl2.place(x=100,y=300)

ent1=Entry(win,font=("Calibri",18,"bold"))
ent1.place(x=230,y=300)

Newvar = StringVar()   # line no 3 ,9, 59 , 60, 61,62,63 combobox ke liye use ho rhi he
cb=ttk.Combobox(win,textvariable=Newvar)
cb['values']=('Sum','Sub','Mul','Div','Mod')
cb['state']='readonly'
cb.place(x=200,y=400)

btn=Button(win,text="Print",width=15,height=1,font=("Calibri",18,"bold") ,command=show)
btn.place(x=150,y=450)

lbl3=Label(win,text="Output",bg="black",fg="white",font=("Calibri",18,"bold"))
lbl3.place(x=100,y=570)

lbl4=Label(win,bg="white",font=("Calibri",18,"bold"))
lbl4.place(x=300,y=570)
win.mainloop()    #work like getch()