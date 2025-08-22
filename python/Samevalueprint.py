from tkinter import *
import tkinter as tk
def show():
    ent1.insert(0,ent.get())  # for copy value in another enty box

win=Tk()
win.geometry("400x400")  

ent=Entry(win)
ent.place(x=10,y=10)

ent1=Entry(win)
ent1.place(x=10,y=50)

btn=Button(win, text="submit", command=show)
btn.place (x=10,y=100)
win.mainloop()