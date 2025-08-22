from tkinter import *
import tkinter as tk
from PIL import Image,ImageTk
from tkinter import ttk
win=Tk()
win.state("zoomed")
win.config(bg="white")
win.iconbitmap("D:\insitute management system\logouok.ico")
win.title(" U O K ")

menu_bar=Menu(win)
win.config(menu=menu_bar)

file_menu=Menu(menu_bar,tearoff=0)
menu_bar.add_cascade(label='Addmission',menu=file_menu)
file_menu.add_command(label='New Addmission')
#file_menu.add_separator()
#file_menu.add_command(label='',font=(1))

edit_menu=Menu(menu_bar,tearoff=0)
menu_bar.add_cascade(label='Fees',menu=edit_menu)
edit_menu.add_command(label='Undo')
edit_menu.add_separator()
edit_menu.add_command(label='Redo')

win.mainloop()