from tkinter import *
import tkinter as tk      # tinker add kiya hai

def Sum():
    a=ent.get()
    b=ent1.get()
    
    # ager ham by default string print krana chahte hai to hame int  nhi lgana direct #lbl4.config(text=a+b) lgana hai
    
    c=int(a)+int(b)
    lbl4.config(text=c)
 
def Sub():
      a=ent.get()
      b=ent1.get()
      if b>a:
          d=int(b)-int(a)
          lbl4.config(text=d)
      else:
          d=int(a)-int(b)
          lbl4.config(text=d)
    
def Mul():
     a=ent.get()
     b=ent1.get()
     e=int(a)*int(b)
     lbl4.config(text=e)
    
def Div():
    a=ent.get()
    b=ent1.get()
    f=int(a)/int(b)
    lbl4.config(text=f)

def Mod():
    a=ent.get()
    b=ent1.get()
    g=int(a)%int(b)
    lbl4.config(text=g) 




win =Tk()       # tinker library ka  variable name declare kiya he "Tk" me hmesha T capital hoga
win.title("my program") # for tittle on screen


win.geometry("550x766")  #width X hieght
        #or
#win.maxsize(width=600,height=600)
#win.minsize(width=400,height=200)
     #//
     
win.config(bg="blue")

win.iconbitmap("Safe-icon.ico")

lbl1=Label(win,text="Number 1",bg="blue",fg="white",font=("Arial",18,"bold"))
lbl1.place(x=100,y=200)

ent=Entry(win,font=("Arial",18,"bold"))
ent.place(x=200,y=200)

lbl2=Label(win,text="Number 2",bg="blue",fg="white",font=("Arial",18,"bold"))
lbl2.place(x=100,y=300)

ent1=Entry(win,font=("Arial",18,"bold"))
ent1.place(x=200,y=300)

btn1=Button(win,text="Sum",width=5,height=1,font=("Arial",11,"bold") ,command=Sum)
btn1.place(x=90,y=400)

btn2=Button(win,text="Sub",width=5,height=1,font=("Arial",11,"bold") ,command=Sub)
btn2.place(x=160,y=400)
btn3=Button(win,text="Mul",width=5,height=1,font=("Arial",11,"bold") ,command=Mul)
btn3.place(x=230,y=400)
btn4=Button(win,text="Div",width=5,height=1,font=("Arial",11,"bold") ,command=Div)
btn4.place(x=300,y=400)
btn4=Button(win,text="Mod",width=5,height=1,font=("Arial",11,"bold") ,command=Mod)
btn4.place(x=370,y=400)

lbl3=Label(win,text="Output",bg="blue",fg="white",font=("Arial",18,"bold"))
lbl3.place(x=100,y=500)

lbl4=Label(win,bg="white",font=("Arial",18,"bold"))
lbl4.place(x=300,y=500)
win.mainloop()    #work like getch()