from tkinter import *
from PIL import Image,ImageTk
import tkinter as tk
from tkinter import ttk
win=Tk()
win.state('zoomed')

image=Image.open("D:\\insitute management system\\page.png")
image=image.resize((1500,800))
tk_image=ImageTk.PhotoImage(image)
image_label=tk.Label(win,image=tk_image)
image_label.pack()

#file=PhotoImage(file="D:\insitute management system\page.png")
#lbl=Label(win,image=file,width=1460,height=970)
#lbl.place(x=0,y=0)


win.mainloop()