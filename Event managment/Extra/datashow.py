def show_record():
    conn,cur=db_connect()
    data=cur.execute("select * from booking")
    rows=cur.fetchall() #access krna
    with open('output.csv', 'w', newline='') as csv_file:
        csv_writer = csv.writer(csv_file)
        column_names = [desc[0] for desc in cur.description] # Column names
        csv_writer.writerow(column_names)
        csv_writer.writerows(rows)
    cur.close()
    conn.close()
    record=pd.read_csv('output.csv')
    rec=list(record.loc[0:])
    
    r_set=record.to_numpy().tolist() #record ko list me convert kiya hai
    #data=['ID','Name','Phone','Gender','Address']
    r_set.insert(0,rec)
    
    tree = ttk.Treeview(root, columns=("ID", "Name"), show="headings", height=25)

# Define the headings
    tree.heading("ID", text="ID")
    tree.heading("Name", text="Name")

# Insert data without using a loop
    tree.insert("", tk.END, values=(1, "Alice"))
    tree.insert("", tk.END, values=(2, "Bob"))
    tree.insert("", tk.END, values=(3, "Charlie"))
    tree.insert("", tk.END, values=(4, "Diana"))
    tree.insert("", tk.END, values=(5, "Eve"))

# Add the Treeview to the main window
    tree.pack(pady=10)

    
 '''main_frame=tk.Frame(win,height=400,width=400,bg='black',bd=2)
    for i in range(len(r_set)):
        for j in range(5):
            e=Entry(main_frame,width=19,bd=2,justify=CENTER)
            e.grid(row=i,column=j)
            e.insert(END,r_set[i][j])
    main_frame.place(x=208,y=80)'''