from tkinter import *
import tkinter as tk

win=Tk()
win.geometry("590x700")
win.config(bg="brown")

def rel():
    a=ent.get()
    b=ent1.get()
    if a>b:
        lbl3.config(text="a large")
    else:
        lbl3.config(text="b large")    

def show():
    a=ent.get()
    b=ent1.get()
    c=int (a) + int (b)
    Addent.config(text=c)
    
    d=int (a) - int (b)
    Subent.config(text=d)
    
    e=int (a) * int (b)
    Mulent.config(text=e)
    
    f=int (a) / int (b)
    Divent.config(text=f)
    
    g=int (a) % int (b)
    Modent.config(text=g)
  
def SC():
    a=ent.get()
    b=ent1.get()
    c=int(a)+int(b)
    Squent.config(text=c*c)
    Cubent.config(text=c*c*c)  
    
    
def AV():
    a=ent.get()
    b=ent1.get()
    c=(int(a)+int(b))/2
    Avgent.config(text=c)
 
def PR(): 
    a=ent.get()
    b=ent1.get()
    c=int(a)/int(b)*100
    Perent.config(text=c)    
  

#tittle :-
lbl=Label(win,text="❤ Mathematical Operation ❤", bg="brown" , fg="black", font=("arial",24,"bold"))
lbl.place(x=70,y=50)

#number 1:-
lbl1=Label(win,text="Number 1", bg="brown" , fg="white", font=("arial",17,"bold"))
lbl1.place(x=100,y=150)

ent=Entry(win,font=("arial",17,"bold"))
ent.place(x= 220 , y=150)

#number 2:-
lbl2=Label(win,text="Number 2", bg="brown" , fg="white", font=("arial",17,"bold"))
lbl2.place(x=100,y=200)

ent1=Entry(win,font=("arial",17,"bold"))
ent1.place(x= 220 , y=200)
 
 #relation :-
Relbtn=Button(win, text="Relation :-" , font=("arial",15,"bold") ,command=rel )
#lbl3=Label(win,text="Relation", bg="white" , fg="black", font=("arial",17,"bold"))
Relbtn.place(x=100,y=250)

lbl3=Label(win,bg="brown",font=("Arial",17,"bold"))
lbl3.place(x=220,y=250)

#arthemetic operation :-
Artbtn=Button(win, text="Arithmetic :-" , font=("arial",15,"bold") ,command=show )
Artbtn.place (x=100,y=300)

Add=Label(win,text="Sum",bg="brown",fg="white",font=("Arial",14,"bold"))
Add.place(x=100,y=350)

Addent=Label(win,fg="white",bg="brown",font=("Arial",17,"bold"))
Addent.place(x=200,y=350)

Sub=Label(win,text="Sub",bg="brown",fg="white",font=("Arial",14,"bold"))
Sub.place(x=100,y=390)

Subent=Label(win,fg="white",bg="brown",font=("Arial",17,"bold"))
Subent.place(x=200,y=390)

Mul=Label(win,text="Mul",bg="brown",fg="white",font=("Arial",14,"bold"))
Mul.place(x=100,y=430)

Mulent=Label(win,fg="white",bg="brown",font=("Arial",17,"bold"))
Mulent.place(x=200,y=430)

Div=Label(win,text="Div",bg="brown",fg="white",font=("Arial",14,"bold"))
Div.place(x=100,y=470)

Divent=Label(win,fg="white",bg="brown",font=("Arial",17,"bold"))
Divent.place(x=200,y=470)

Mod=Label(win,text="Mod",bg="brown",fg="white",font=("Arial",14,"bold"))
Mod.place(x=100,y=510)

Modent=Label(win,fg="white",bg="brown",font=("Arial",17,"bold"))
Modent.place(x=200,y=510)

#square & cube :-

SCbtn=Button(win, text="Square & Cube  :-" , font=("arial",15,"bold"), command=SC)
SCbtn.place (x=270,y=300)

Squ=Label(win,text="Square",bg="brown",fg="white",font=("Arial",14,"bold"))
Squ.place(x=270,y=350)

Squent=Label(win,fg="white",bg="brown",font=("Arial",17,"bold"))
Squent.place(x=370,y=350)

Cube=Label(win,text="Cube",bg="brown",fg="white",font=("Arial",14,"bold"))
Cube.place(x=270,y=390)

Cubent=Label(win,fg="white",bg="brown",font=("Arial",17,"bold"))
Cubent.place(x=370,y=390)

# average :-
Avgbtn=Button(win, text="Average :-" , font=("arial",13,"bold") , command=AV)
Avgbtn.place (x=270,y=430)
Avgent=Label(win,fg="white",bg="brown",font=("Arial",17,"bold"))
Avgent.place(x=270,y=470)

# persantage :-
Perbtn=Button(win, text="Persantage :-" , font=("arial",11,"bold"), command=PR)
Perbtn.place (x=270,y=515)
Perent=Label(win,fg="white",bg="brown",font=("Arial",14,"bold"))
Perent.place(x=400,y=515)
win.mainloop()