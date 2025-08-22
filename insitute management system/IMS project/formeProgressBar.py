from tkinter import *
import tkinter as tk
from PIL import Image,ImageTk
from tkinter import ttk
import os
win=Tk()

win.state("zoomed")
win.config(bg="white")
win.iconbitmap("D:\insitute management system\logouok.ico")
win.title(" U O K ")
#progress bar
def update_progress(value):
    canvas.delete("progress")
    canvas.create_rectangle(0,0,value*1,bar_height,fill="brown",tags="progress")
    lbl.config(text=f"Loding.....{value//11}")
    if value<1100:
        win.after(4,update_progress,value+1)
bar_width=1100
bar_height=26
canvas=tk.Canvas(win,width=bar_width,height=bar_height,bg="white")
canvas.place(x=210,y=665)
lbl=Label(win,fg="brown",bg="white",font=("Arial Black",20,"bold"))
lbl.place(x=210,y=620)
update_progress(0)
win.mainloop()