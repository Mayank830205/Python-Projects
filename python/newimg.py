from tkinter import *
from PIL import Image, ImageTk
import tkinter as tk
from tkinter import ttk

win=Tk()
win.state('zoomed') #output hmesha full screen me open hoga
files1=Image.open("C:\\Users\\HP\\Desktop\\python\\NN.png")  # used for open image
files2=files1.resize((500,700)) #for assign size
 
tk_image=ImageTk.PhotoImage(files2) #tk_imagee is a var name and ImageTk.PhotoImage is predefined
 
new_Label=tk.Label(win,image=tk_image) # here is image= is predefined
new_Label.pack()   
 
#lbl1=Label(win,image=files2)
#lbl1.pack(fill = BOTH, expand = True) #fix image in full screen

win.mainloop()