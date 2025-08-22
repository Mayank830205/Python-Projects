from tkinter import *
import tkinter as tk
import tkinter as tk



def show():
    print(var.get())
    
    '''a=var.get()
    if a==0:       # if male  salect krenge to male likha aayega
    gender="male"
    if a==1:     #if female select krenge to female lika aayega     
    gender="female"
    print(gender)'''
    
win=Tk()
var=IntVar()    # I and V capital
radio1=Radiobutton(win,text="Male",value=0, variable= var) # IntVar me jo variable denge vhi lenge     // value 0 hai by default male select rhega
radio1.place(x=10,y=20)

radio2=Radiobutton(win,text="Female",value=1, variable= var)
radio2.place(x=20,y=50)

btn=Button(win,text="Submit",command=show)
btn.place(x=10,y=90)

win.mainloop()