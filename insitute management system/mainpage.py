from tkinter import *
import tkinter as tk
from PIL import Image,ImageTk
from tkinter import ttk
import os
win=Tk()
win.state("zoomed")
win.config(bg="white")
win.iconbitmap("D:\\insitute management system\\IMS project\\logouok.ico")
win.title(" U O K ")

image=Image.open("D:\\insitute management system\\IMS project\\imageuok.png")
image=image.resize((1530,788))
tk_image=ImageTk.PhotoImage(image)
image_label=tk.Label(win,image=tk_image)
image_label.pack()

lbl=Label(win,bg="black",width=218,height=5)
lbl.place(x=0,y=0)

image0=Image.open("D:\\insitute management system\\IMS project\\logouok.png")
image0=image0.resize((135,135))
tk_image0=ImageTk.PhotoImage(image0)
image_label=tk.Label(win,bg="black",image=tk_image0)
image_label.place(x=1394,y=0)

image1=Image.open("D:\\insitute management system\\IMS project\\Addmissionpng.png")
image1=image1.resize((60,60))
tk_image1=ImageTk.PhotoImage(image1)
image_label=tk.Label(win,image=tk_image1)
image_label.place(x=8,y=8)

image2=Image.open("D:\\insitute management system\\IMS project\\Feespng.png")
image2=image2.resize((60,60))
tk_image2=ImageTk.PhotoImage(image2)
image_label=tk.Label(win,image=tk_image2)
image_label.place(x=120,y=8)

image3=Image.open("D:\\insitute management system\\IMS project\\studentdeitailspng.png")
image3=image3.resize((60,60))
tk_image3=ImageTk.PhotoImage(image3)
image_label=tk.Label(win,image=tk_image3)
image_label.place(x=230,y=8)

image4=Image.open("D:\\insitute management system\\IMS project\\Teacherpng.png")
image4=image4.resize((60,60))
tk_image4=ImageTk.PhotoImage(image4)
image_label=tk.Label(win,image=tk_image4)
image_label.place(x=340,y=8)

image5=Image.open("D:\\insitute management system\\IMS project\\Removestudentpng.png")
image5=image5.resize((60,60))
tk_image5=ImageTk.PhotoImage(image5)
image_label=tk.Label(win,image=tk_image5)
image_label.place(x=450,y=8)

image6=Image.open("D:\\insitute management system\\IMS project\\images (4).png")
image6=image6.resize((60,60))
tk_image6=ImageTk.PhotoImage(image6)
image_label=tk.Label(win,image=tk_image6)
image_label.place(x=560,y=8)

image7=Image.open("D:\\insitute management system\\IMS project\\Receiptt.png")
image7=image7.resize((60,60))
tk_image7=ImageTk.PhotoImage(image7)
image_label=tk.Label(win,image=tk_image7)
image_label.place(x=670,y=8)

image8=Image.open("D:\\insitute management system\\IMS project\\logoutpng.png")
image8=image8.resize((60,60))
tk_image8=ImageTk.PhotoImage(image8)
image_label=tk.Label(win,image=tk_image8)
image_label.place(x=770,y=8)

menu_bar=Menu(win)
win.config(menu=menu_bar)

def admission():
    win.destroy()
    os.system("python admission.py")
def fees():
    win.destroy()
    os.system("python fees8.py")
def indi():
    win.destroy()
    os.system("python indivdualstudent.py")
def sete():
    win.destroy()
    os.system("python searchteacher12.py")
def adte():
    win.destroy()
    os.system("python infoteacher11.py")
def rem():
    win.destroy()
    os.system("python deletestudent13.py")
def seall():
    win.destroy()
    os.system("python SearchAllRecord.py")
def update():
    win.destroy()
    os.system("python updaterecord.py")
def receipt():
    win.destroy()
    os.system("python Receipt.py")
def logout():
    win.destroy()
    os.system("python afterprogerssbar.py")
def about():
    win.destroy()
    os.system("python Aboutpage.py")

file_menu=Menu(menu_bar,tearoff=0)
menu_bar.add_cascade(label='  Addmission         ',menu=file_menu)
file_menu.add_command(label='New Addmission',command=admission)

edit_menu=Menu(menu_bar,tearoff=0)
menu_bar.add_cascade(label='        Fees      ',menu=edit_menu)
edit_menu.add_command(label='Fees Details',command=fees)

student_menu=Menu(menu_bar,tearoff=0)
menu_bar.add_cascade(label='         Student Details   ',menu=student_menu)
student_menu.add_command(label='Individual  student Details',command=indi)
student_menu.add_separator()
student_menu.add_command(label='Saerch all student records',command=seall)
student_menu.add_separator()
student_menu.add_command(label='Update student records',command=update)

teacher_menu=Menu(menu_bar,tearoff=0)
menu_bar.add_cascade(label='         Teacher   ',menu=teacher_menu)
teacher_menu.add_command(label='Add Teacher Information',command=adte)
teacher_menu.add_separator()
teacher_menu.add_command(label='Search teacher details',command=sete)

Remove_menu=Menu(menu_bar,tearoff=0)
menu_bar.add_cascade(label='         Remove Records',menu=Remove_menu)
Remove_menu.add_command(label='Delete Records',command=rem)

about_menu=Menu(menu_bar,tearoff=0)
menu_bar.add_cascade(label='         About Us        ',menu=about_menu)
about_menu.add_command(label='About Your Institute',command=about)

Receipt_menu=Menu(menu_bar,tearoff=0)
menu_bar.add_cascade(label='         Receipt       ',menu=Receipt_menu)
Receipt_menu.add_command(label='Institute final receipt',command=receipt)

logout_menu=Menu(menu_bar,tearoff=0)
menu_bar.add_cascade(label='         Logout         ',menu=logout_menu)
logout_menu.add_command(label='Logout Your Account',command=logout)
win.mainloop()