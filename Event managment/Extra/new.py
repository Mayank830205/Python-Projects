from tkinter import *
from PIL import Image, ImageTk
import tkinter as tk

# Create the main window
win = tk.Tk()
win.title("Scrollbar Example")

# Create a Text widget
text_widget = tk.Text(win, wrap="word", width=50, height=15)
text_widget.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

# Create a Scrollbar and attach it to the Text widget
scroll = tk.Scrollbar(win)
scroll.pack(side=tk.RIGHT, fill=tk.Y)

# Configure the Text widget and Scrollbar to work together
text_widget.config(yscrollcommand=scroll.set)
scroll.config(command=text_widget.yview)

# Add some content to the Text widget
for i in range(1, 101):
    text_widget.insert(tk.END, f"This is line number {i}\n")

# Start the GUI loop
win.mainloop()
