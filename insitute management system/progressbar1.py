from tkinter import *
import tkinter as tk
from PIL import Image,ImageTk
import os
win=Tk()

win.state("zoomed")
win.iconbitmap("D:\\insitute management system\\IMS project\\logouok.ico")
win.title(" U O K ")

image=Image.open("D:\\insitute management system\\IMS project\\probackground.png")
image=image.resize((1530,790))
tk_image=ImageTk.PhotoImage(image)
image_label=tk.Label(win,image=tk_image)
image_label.pack()

lbl=Label(win,text="Welcome To My",fg="black",bg="#F2F2F2",font=("Forte",60))
lbl.place(x=300,y=0)
lbl=Label(win,text="Project",fg="#919191",bg="#F2F2F2",font=("Forte",80))
lbl.place(x=310,y=76)
#progress bar
def update_progress(value):
    canvas.delete("progress")
    canvas.create_rectangle(0,0,value*1,bar_height,fill="blue",tags="progress")
    lbl.config(text=f"Loding.....{value//9}")
    if value<1000:
        
        win.after(2,update_progress,value+1)
    else:
        win.destroy()
        os.system("python afterprogerssbar.py")
        
bar_width=1000
bar_height=35
canvas=tk.Canvas(win,width=bar_width,height=bar_height,bg="#BFBFBF")
canvas.place(x=280,y=700)

lbl=Label(win,fg="blue",bg="white",font=("Arial Black",25,"bold"))
lbl.place(x=280,y=630)
update_progress(0)

win.geometry("300x300")
win.config(bg="black")

win.mainloop()