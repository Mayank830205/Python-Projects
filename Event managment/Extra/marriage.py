from tkinter import *
from PIL import Image, ImageTk
import tkinter as tk
from tkinter import ttk
import os

def Home():
    win.destroy()
    
    os.system("python menubar.py") 

def Mydetail():
    win.destroy()
    os.system("python mydetail.py") 
    
    
def Merriage():
    win.destroy()
    os.system("python marriage.py") 
    
def Bday():
    win.destroy()
    os.system("python bdayhall.py") 

def Dance():
    win.destroy()
    os.system("python dancehall.py") 
    
    
def Viewfeedback():
    win.destroy()
    os.system("python viewfeedback.py") 
    
def Feedback():
    win.destroy()
    os.system("python Rating.py") 


win=Tk()



#win.geometry("1000x900")
win.state('zoomed')
win.config(bg="white")

'''style = ttk.Style()
style.theme_use("default")



style.configure("TreeView",
                background="black",
                fieldbackground='lightblue',
                foreground='black',
                rowheight=200
                )

style.configure("TreeView.Heading",
                background="black",
                fieldbackground='lightblue',
                foreground='white',
                font=("Arial",12,"bold"))'''




# Create a Text widget
#text_widget = tk.Text(win, wrap="word", width=50, height=15)
#text_widget.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

# Create a Scrollbar and attach it to the Text widget
'''scroll = tk.Scrollbar(win)
scroll.pack(side=tk.RIGHT, fill=tk.Y)

# Configure the Text widget and Scrollbar to work together
text_widget.config(yscrollcommand=scroll.set)
scroll.config(command=text_widget.yview)
'''

talk=Label(win,text="⭐EVENT MANAGMENT⭐",bg="white",fg="black",font=("Algerian",28,"bold"))
talk.place(x=20,y=30)

blank=Label(win,fg="white",bg="black",width=70,height=1,font=("Arial",22,"bold"))
blank.place(x=4,y=120)

b1=Button(win,bg="black",fg="white",text="Home",width=7,height=1,font=("Arial",14,"bold"),relief="flat",command=Home)
b1.place(x=15,y=120)

b2=Button(win,bg="black",fg="white",text="My Detail",width=7,height=1,font=("Arial",14,"bold"),relief="flat",command=Mydetail)
b2.place(x=120,y=120)

b3=Button(win,bg="black",fg="white",text="Merriage Hall",width=11,height=1,font=("Arial",14,"bold"),relief="flat", command=Merriage )
b3.place(x=230,y=120)

b4=Button(win,bg="black",fg="white",text="Birthday Hall",width=11,height=1,font=("Arial",14,"bold"),relief="flat",command=Bday )
b4.place(x=390,y=120)

b5=Button(win,bg="black",fg="white",text="Dance Hall",width=11,height=1,font=("Arial",14,"bold"),relief="flat",command=Dance )
b5.place(x=540,y=120)

b6=Button(win,bg="black",fg="white",text="View Feedback",width=11,height=1,font=("Arial",14,"bold"),relief="flat",command=Viewfeedback )
b6.place(x=690,y=120)

b7=Button(win,bg="black",fg="white",text="Feedback",width=9,height=1,font=("Arial",14,"bold"),relief="flat" ,command=Feedback)
b7.place(x=855,y=120)

b7=Button(win,bg="black",fg="white",text="Logout",width=9,height=1,font=("Arial",14,"bold"),relief="flat" )
b7.place(x=980,y=120)

style = ttk.Style()
style.theme_use("default")



style.configure("Treeview",
                background="blue",
                #fieldbackground='white',
                foreground='white',
                rowheight=200
                )

style.configure("Treeview.Heading",
                background="black",
                #fieldbackground='lightblue',
                foreground='white',
                font=("Arial",12,"bold"))

trv=ttk.Treeview(win, columns=("1","2","3","4","5","6"),height=60, show="headings")
trv.place(x=400,y=170)

trv.heading("1", text="Hall Name")
trv.heading("2", text="Hall Type")
trv.heading("3", text="Address")
trv.heading("4", text="Amount")
trv.heading("5", text="Contact No.")
trv.heading("6", text="Order Now")

trv.column("1", anchor="center",  width=180)
trv.column("2", anchor="center",  width=100)
trv.column("3", anchor="center",  width=180)
trv.column("4", anchor="center",  width=100)
trv.column("5", anchor="center",  width=100)
trv.column("6", anchor="center",  width=100)



trv.insert("", "end", values=("Mangalaxmi Mahal ","AC","Villore","80000/day","8989837761","booking"))

trv.insert("", "end", values=("Love Nest ","Non AC","Mumbai","90000/day","8989837761","booking"))

trv.insert("", "end", values=("Wedding Garden ","AC","New Delhi","100000/day","8989837761","book"))

trv.insert("", "end", values=("ITC Grand Central","AC","Mumbai","300000/day","8989837761",))

trv.insert("", "end", values=("Oberoi Udaivilas","Non AC","Udaipur","100000/day","8989837761","book"))

trv.insert("", "end", values=("Taj Falaknuma Palace ","AC","Hyderabad","90000/day","8989837761","book"))

trv.insert("", "end", values=("JW Marriott ","AC","Pune","70000/day","8989837761","book"))

trv.insert("", "end", values=("The Leela Goa ","AC","Goa","200000/day","8989837761","book"))

trv.insert("", "end", values=("Fort-Palace","AC","Alwar","80000/day","8989837761","book"))

trv.insert("", "end", values=("Maharaja Palace ","AC","Agra","80000/day","8989837761","book"))
#trv.pack(pady=10)







win.mainloop()