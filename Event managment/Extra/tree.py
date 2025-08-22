from tkinter import *
from PIL import Image, ImageTk
import tkinter as tk
from tkinter import ttk

win=Tk()

win.geometry("900x550")
#win.state('zoomed')
win.config(bg="white")

'''tree=ttk.Treeview(win)
tree.place(x=0,y=0)

tree.column(1,anchor=CENTER,stretch=NO,width=100)

tree.heading(1,text="Emailid")

image_path="C:\\Users\\HP\\Desktop\\Event managment\\white.png"
image= Image.open(image_path).resize((100,100))
photo=ImageTk.PhotoImage(image)

tree.insert("", "end",text="Item with Image",image=photo)
tree.image_ref=photo'''

style.configure("Treeview", background="black", foreground="black", rowheight=25, fieldbackground="lightyellow")

trv=ttk.Treeview(win, columns=(1,2,3),height=15, show="headings")

trv.column(1, anchor=CENTER, stretch=NO, width=100)
trv.column(2, anchor=CENTER, stretch=NO, width=100)
trv.column(2, anchor=CENTER, stretch=NO, width=100)

trv.heading(1, text="id")
trv.heading(2, text="name")
trv.heading(3, text="age")

trv.place(x=0,y=0)
trv.grid(row=0, column=0)

win.mainloop()