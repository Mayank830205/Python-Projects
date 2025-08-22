def select_file():
    file_path = filedialog.askopenfilename(
        filetypes=[("Image files", "ab.png bday.png bg.png black.png cup.png"), ("All files", "*.*")]
    )
    if file_path:
        file_label.config(text=file_path.split("C:\\Users\\HP\\Desktop\\Event managment\\image")[-1])





D=Label(win,text="Hall Image",bg="white",fg="black",font=("Rockwell Extra Bold",18,"bold"))
D.place(x=350,y=300)

file_button = ttk.Button(win, text="Choose File", command=select_file)
file_button.grid(row=0, column=1, padx=10, pady=10)
#Dent=Entry(win,bg="white",width=20,font=("Rockwell Extra Bold",18,"bold"))
file_button.place(x=570,y=310)

# Label to display the selected file name
file_label = ttk.Label(win, text="No file selected")
file_label.grid(row=0, column=2, padx=10, pady=10)
file_label.place(x=650,y=310)

