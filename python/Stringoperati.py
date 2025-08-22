from tkinter import *
import tkinter as tk

win=Tk()
win.geometry("590x700")
win.config(bg="pink")


def UP():
    a=ent.get()
    upr.config(text=a.upper())

def LW():
    a=ent.get()
    lwr.config(text=a.lower())


def DC():
    
    duplicate=[]
    for i in range (len(ent)):
        if ent.count(ent[i])==i:
            duplicate.append(ent[i])
            dub.config(text=duplicate)
    #if a.count
    
def PL():
    
     
    a=ent.get()
    if a==a[ :  : -1]:
        pal.config(text="palindrom")
    else:
        pal.config(text="not palindrom")
             
def LN():
    a=ent.get()
    lgt.config(text=len(a))    
 
def ID():
    a=ent.get()
    ind.config(text=a.index(a)) 
        
     
        
#tittle :-
lbl=Label(win,text="✌ String Operation ✌", bg="pink" , fg="black", font=("arial",24,"bold"))
lbl.place(x=100,y=50)

#name:-
lbl1=Label(win,text="Name", bg="pink" , fg="black", font=("arial",17,"bold"))
lbl1.place(x=100,y=150)

ent=Entry(win,font=("arial",17,"bold"))
ent.place(x= 220 , y=150)

#uppercase:-
uprbtn=Button(win, text="Uppercase :-" , font=("arial",15,"bold"),command=UP)
uprbtn.place(x=100,y=220)

upr=Label(win,bg="pink",font=("Arial",17,"bold"))
upr.place(x=300,y=220)

#lowercase :-
lwrbtn=Button(win, text="Lowercase :-" , font=("arial",15,"bold"),command=LW)
lwrbtn.place(x=100,y=300)

lwr=Label(win,bg="pink",font=("Arial",17,"bold"))
lwr.place(x=300,y=300)

#duplicate :-
dubbtn=Button(win, text="Duplicate :-" , font=("arial",15,"bold"),command=DC)
dubbtn.place(x=100,y=380)

dub=Label(win,bg="pink",font=("Arial",17,"bold"))
dub.place(x=300,y=380)

#palindrom or not :-
palbtn=Button(win, text="Palindrom Status :-" , font=("arial",15,"bold"),command=PL)
palbtn.place(x=100,y=450)

pal=Label(win,bg="pink",font=("Arial",17,"bold"))
pal.place(x=300,y=450)

#Find length :-
lgtbtn=Button(win, text="Find length:-" , font=("arial",15,"bold"),command=LN)
lgtbtn.place(x=100,y=520)

lgt=Label(win,bg="pink",font=("Arial",17,"bold"))
lgt.place(x=300,y=520)

#index value :-
indbtn=Button(win, text="Index Value:-" , font=("arial",15,"bold"), command=ID)
indbtn.place(x=100,y=600)

ind=Label(win,bg="pink",font=("Arial",17,"bold"))
ind.place(x=300,y=600)

win.mainloop()