from tkinter import *
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

def show():
    
    print("E-id is : ",ent.get())
    print("Name is : ",ent1.get())
    #print("E-id is : ",ent.get())
    #print(var.get())
    a=var.get()
    if a==0: 
        # if male  salect krenge to male likha aayega
        gender="male"
    if a==1:     #if female select krenge to female lika aayega     
        gender="female"
    print("gender is = ", gender)
    #print(var1.get())
    #c=cb.get()
    print("Address is : ",Addent.get())
    print(cb.get())
    b=c1.get()
    c=c2.get()
    if b==0 and c==0: 
        
        course="None"
    if b==1 and c==0:     
        course="BCA"
    if b==0 and c==1:
        course="MCA"
    if b==1 and c==1:
        course="BCA, MCA"        
    #print(gender)
    print("course is = ", course)
    messagebox.showinfo('info','submit successfully')
    clear()   #for clear data 

def clear():
    #a=ent.get()
    entvar.set(" ")
    entvar1.set(" ")
    entvar2.set(" ")
    #ent.insert(0," ")
 
#close window (distroy () ) :-
   
def clo():
   res= messagebox.askquestion('close',"do you want close")
   if res=="yes":
       win.destroy()     
win=Tk()
win.title("my program") # for tittle on screen


win.geometry("600x766")  #width X hieght
win.config(bg="BLACK")

lbl1=Label(win,text="E-ID",bg="black",fg="white",font=("Arial",18,"bold"))
lbl1.place(x=100,y=100)

entvar=StringVar()
ent=Entry(win,font=("Arial",18,"bold"),textvariable=entvar)
ent.place(x=200,y=100)

lbl2=Label(win,text="Name",bg="black",fg="white",font=("Arial",18,"bold"))
lbl2.place(x=100,y=200)

entvar1=StringVar()
ent1=Entry(win,font=("Arial",18,"bold"),textvariable=entvar1)
ent1.place(x=200,y=200)

lbl3=Label(win,text="Gender",bg="black",fg="white",font=("Arial",18,"bold"))
lbl3.place(x=100,y=300)
 
var=IntVar()
radio1=Radiobutton(win,text="Male",value=0, variable= var) # IntVar me jo variable denge vhi lenge     // value 0 hai by default male select rhega
radio1.place(x=250,y=300)

radio2=Radiobutton(win,text="Female",value=1, variable= var)
radio2.place(x=380,y=300)

lbl4=Label(win,text="Course",bg="black",fg="white",font=("Arial",18,"bold"))
lbl4.place(x=100,y=400)
 
c1=IntVar()
chack1=Checkbutton(win,text="BCA", variable= c1) # IntVar me jo variable denge vhi lenge     // value 0 hai by default male select rhega
chack1.place(x=250,y=400)

c2=IntVar()
chack2=Checkbutton(win,text="MCA", variable= c2)
chack2.place(x=380,y=400)

Add=Label(win,text="Address",bg="black",fg="white",font=("Arial",18,"bold"))
Add.place(x=100,y=500)

entvar2=StringVar()
Addent=Entry(win,font=("Arial",18,"bold"),textvariable=entvar2)
Addent.place(x=200,y=500)

Sub=Label(win,text="Subject",bg="black",fg="white",font=("Arial",18,"bold"))
Sub.place(x=100,y=600)
Newvar = StringVar()   # line no 3 ,9, 59 , 60, 61,62,63 combobox ke liye use ho rhi he
cb=ttk.Combobox(win,textvariable=Newvar)
cb['values']=('Hindi','Eng','Sci','Sst','Math')
cb['state']='readonly'
cb.place(x=240,y=600)

btn1=Button(win,text="Close",width=8,height=1,font=("Arial",10,"bold"),command=clo)
btn1.place(x=500,y=400)

btn=Button(win,text="Submit",width=8,height=1,font=("Arial",10,"bold") ,command=show)
btn.place(x=480,y=500)

#btn1=Button(win,text="Clear",width=8,height=1,font=("Arial",10,"bold"),command=clear)
#btn1.place(x=450,y=600)

win.mainloop()