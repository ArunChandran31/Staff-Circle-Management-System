from tkinter import*
from tkinter import ttk
from PIL import ImageTk
# import mysql.connector
from tkinter import messagebox
class staff:


    def __init__(self,root):
        self.root=root
        self.root.title("staff management system")
        self.root.geometry("1350x700+0+0")
        self.root.configure(bg="lightgray")
        self.root.resizable(False,False)

        #TITLE
        title=Label(self.root, text="S T A F F - C I R C L E",bd= 10, relief=GROOVE,font=("Bahnschrift SemiBold Condensed",25,"bold"),bg="lightgray",fg="black")
        title.pack(side=TOP,fill=X)

        #SUBTITLE
        title=Label(self.root, text="MANAGING ENVIRONMENT",bd= 6, relief=GROOVE,font=("Bahnschrift SemiBold Condensed",14,"bold"),bg="lightgray",fg="black")
        title.pack(side=TOP,fill=X)


        #Variables
        self.id_no_var=StringVar()
        self.name_var=StringVar()
        self.designation_var=StringVar()
        self.gender_var=StringVar()
        self.email_var=StringVar()
        self.phone_no_var=StringVar()
        self.search_by=StringVar()
        self.search_txt=StringVar()


        #manage box
        ManageFrame=Frame(self.root, bd=4, relief=RIDGE, bg="lightgray")
        ManageFrame.place(x=20,y=100,width=450,height=580)

        #title of manage box
        mtitle=Label(ManageFrame,text="MANAGE",font=("Bahnschrift SemiBold Condensed",18,"bold"),bg="lightgray",fg="black")
        mtitle.grid(row=0,columnspan=2,pady=20)


        #Employee idno.
        #subtitle
        lbl_id_no=Label(ManageFrame,text="ID NO",font=("Bahnschrift SemiBold Condensed",18,"bold"),bg="lightgray",fg="black")
        lbl_id_no.grid(row=1,column=0,pady=10,padx=20,sticky="w")

        #entry box for idno
        txtid_no=Entry(ManageFrame,textvariable=self.id_no_var,font=("Bahnschrift SemiBold Condensed",15,"bold"),width=30,bd=5,relief=RIDGE)
        txtid_no.grid(row=1,column=1,pady=10,padx=25,sticky="w")


        #Employee name.
        #subtitle
        lbl_name=Label(ManageFrame,text="EMP. NAME",font=("Bahnschrift SemiBold Condensed",18,"bold"),bg="lightgray",fg="black")
        lbl_name.grid(row=2,column=0,pady=10,padx=20,sticky="w")

        #entry box for name
        txtname=Entry(ManageFrame,textvariable=self.name_var,font=("Bahnschrift SemiBold Condensed",15,"bold"),width=30,bd=5,relief=RIDGE)
        txtname.grid(row=2,column=1,pady=10,padx=25,sticky="w")


        #Employee Designation
        #subtitle
        lbl_des=Label(ManageFrame,text="DES:",font=("Bahnschrift SemiBold Condensed",18,"bold"),bg="lightgray",fg="black")
        lbl_des.grid(row=6,column=0,pady=10,padx=25,sticky="w")

        #entry box for designation
        txtdes=Entry(ManageFrame,textvariable=self.designation_var,font=("Bahnschrift SemiBold Condensed",15,"bold"),width=30,bd=5,relief=RIDGE)
        txtdes.grid(row=6,column=1,pady=10,padx=25,sticky="w")


        #Employee gender.
        #subtitle
        lbl_gender=Label(ManageFrame,text="GENDER:",font=("Bahnschrift SemiBold Condensed",18,"bold"),bg="lightgray",fg="black")
        lbl_gender.grid(row=4,column=0,pady=10,padx=20,sticky="w")

        #entry box for gender (cannot write on the entry box, can only choose from three options using combo box function)
        combo_gender=ttk.Combobox(ManageFrame,textvariable=self.gender_var,font=("Bahnschrift SemiBold Condensed",14,"bold"),width=28,state='readonly')
        combo_gender["values"]=("MALE","FEMALE","OTHER")
        combo_gender.grid(row=4,column=1,padx=25,pady=10)


        #Employee phone no.
        #subtitle
        lbl_phone_no=Label(ManageFrame,text="PHONE NO:",font=("Bahnschrift SemiBold Condensed",18,"bold"),bg="lightgray",fg="black")
        lbl_phone_no.grid(row=3,column=0,pady=10,padx=20,sticky="w")

        #entry box for phone no
        txtphone_no=Entry(ManageFrame,textvariable=self.phone_no_var,font=("Bahnschrift SemiBold Condensed",15,"bold"),width=30,bd=5,relief=RIDGE)
        txtphone_no.grid(row=3,column=1,pady=10,padx=25,sticky="w")


        #Employee email.
        #subtitle
        lbl_Email=Label(ManageFrame,text="EMAIL ID:",font=("Bahnschrift SemiBold Condensed",18,"bold"),bg="lightgray",fg="black")
        lbl_Email.grid(row=5,column=0,pady=10,padx=20,sticky="w")

        #entry box for email
        txtEmail=Entry(ManageFrame,textvariable=self.email_var,font=("Bahnschrift SemiBold Condensed",15,"bold"),width=30,bd=5,relief=RIDGE)
        txtEmail.grid(row=5,column=1,pady=10,padx=25,sticky="w")


        #Employee address.
        #subtitle
        lbl_address=Label(ManageFrame,text="ADDRESS:",font=("Bahnschrift SemiBold Condensed",18,"bold"),bg="lightgray",fg="black")
        lbl_address.grid(row=7,column=0,pady=10,padx=20,sticky="w")

        #entry box for address
        self.txtaddress=Text(ManageFrame,width=50,height=4,font=("Bahnschrift SemiBold Condensed",10,"bold"))
        self.txtaddress.grid(row=7,column=1,pady=11,padx=20,sticky="w")


        #buttons for different functions
        #frame for button box
        btn_Frame=Frame(ManageFrame,bd=4,relief=RIDGE,bg="lightgray")
        btn_Frame.place(x=10,y=500,width=420)

        #function for button
        #function of add button
        addbtn=Button(btn_Frame,cursor="hand2",text="ADD",width=10,command=self.add_staff).grid(row=0,column=0,padx=10,pady=10)
        #function of update button
        updtbtn=Button(btn_Frame,cursor="hand2",text="UPDATE",width=10,command=self.update_data).grid(row=0,column=1,padx=10,pady=10)
        #function of delete button
        delbtn=Button(btn_Frame,cursor="hand2",text="DELETE",width=10,command=self.delete_data).grid(row=0,column=2,padx=10,pady=10)
        #function of clear button
        clrbtn=Button(btn_Frame,cursor="hand2",text="CLEAR",width=10,command=self.clear).grid(row=0,column=3,padx=10,pady=10)


        #DETAIL BOX AND VIEW BOX
        #frame for detail box
        DetailFrame=Frame(self.root, bd=4, relief=RIDGE, bg="lightgray")
        DetailFrame.place(x=500,y=100,width=830,height=580)


        #lable that show the text 'search by'
        lbl_search=Label(DetailFrame,text="SEARCH BY:",bg="lightgray",fg="black",font=("Bahnschrift SemiBold Condensed",18,"bold"))
        lbl_search.grid(row=0,column=0,padx=20,pady=10,sticky="w")


        #combobox function that displays list of details so that the user can choose to search
        combo_search=ttk.Combobox(DetailFrame,textvariable=self.search_by,width=15,font=("Bahnschrift SemiBold Condensed",15,"bold"),state='readonly')
        combo_search['values']=("idno","name","designation","phoneno")
        combo_search.grid(row=0,column=1,padx=19,pady=10)

        #entry box for entering the detail, which search the full details of the staff  using the keyword entered by the user
        txtsearch=Entry(DetailFrame,textvariable=self.search_txt,font=("Bahnschrift SemiBold Condensed",15,"bold"),width=30,bd=5,relief=RIDGE)
        txtsearch.grid(row=0,column=2,padx=20,pady=10,sticky="w")

        #buttons for search and showall function
        searchbtn=Button(DetailFrame,cursor="hand2",text="SEARCH",width=10,command=self.search_data).grid(row=0,column=3,padx=10,pady=10)
        showallbtn=Button(DetailFrame,cursor="hand2",text="SHOW ALL",width=10,command=self.fetch_data).grid(row=0,column=4,padx=10,pady=10)


        #table
        Table_Frame=Frame(DetailFrame,bd=4,relief=RIDGE,bg="lightgray")
        Table_Frame.place(x=10,y=70,width=800,height=500)

        #this is the frame shows the full details of the staffs
        #this function is used for scrolling (i.e., move the page up, down, right and left)
        scroll_x=Scrollbar(Table_Frame,orient=HORIZONTAL)
        scroll_y=Scrollbar(Table_Frame,orient=VERTICAL)
        self.Staff_Table=ttk.Treeview(Table_Frame,columns=("idno","name","designation","gender","phoneno","email","address"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.Staff_Table.xview)
        scroll_y.config(command=self.Staff_Table.yview)
        self.Staff_Table.heading("idno",text="ID NO.")
        self.Staff_Table.heading("name",text="NAME")
        self.Staff_Table.heading("designation",text="DESIGNATION")
        self.Staff_Table.heading("gender",text="GENDER")
        self.Staff_Table.heading("phoneno",text="PHONE NO")
        self.Staff_Table.heading("email",text="EMAIL")
        self.Staff_Table.heading("address",text="ADDRESS")
        self.Staff_Table['show']='headings'
        self.Staff_Table.column("idno",width=100)
        self.Staff_Table.column("name",width=150)
        self.Staff_Table.column("designation",width=150)
        self.Staff_Table.column("gender",width=100)
        self.Staff_Table.column("phoneno",width=150)
        self.Staff_Table.column("email",width=200)
        self.Staff_Table.column("address",width=400)
        self.Staff_Table.pack(fill=BOTH,expand=1)
        self.Staff_Table.bind("<ButtonRelease-1>",self.get_cursor)
        self.fetch_data()

    #defining add function
    def add_staff(self):
        if self.id_no_var.get() == "" or self.name_var.get()=="":
            messagebox.showerror("ERROR","ALL FIELDS ARE REQUIRED!")
        else:
            conn=mysql.connector.connect(host="localhost",user="root",passwd="31012004",database="mydatabase")
            cur=conn.cursor()
            cur.execute("insert into staff values(%s,%s,%s,%s,%s,%s,%s)",(self.id_no_var.get(),
                                                                          self.name_var.get(),
                                                                          self.designation_var.get(),
                                                                          self.gender_var.get(),
                                                                          self.phone_no_var.get(),
                                                                          self.email_var.get(),
                                                                          self.txtaddress.get('1.0',END)
                                                                          ))
            conn.commit()
            self.fetch_data()
            self.clear()
            conn.close()
            messagebox.showinfo("SUCCESS","RECORD ADDED")


    #defining show all  function
    def fetch_data(self):
        conn=mysql.connector.connect(host="localhost",user="root",passwd="arun3114",database="mydatabase")
        cur=conn.cursor()
        cur.execute("select * from staff")
        rows=cur.fetchall()
        if len(rows)!=0:
            self.Staff_Table.delete(*self.Staff_Table.get_children())
            for row in rows:
                self.Staff_Table.insert('',END,values=row)
            conn.commit()
        conn.close()


    #defining clear function
    def clear(self):
        self.id_no_var.set("")
        self.name_var.set("")
        self.designation_var.set("")
        self.gender_var.set("")
        self.phone_no_var.set("")
        self.email_var.set("")
        self.txtaddress.delete("1.0",END)


    #on clicking the particular data of a particular staff the full details get automatically filled in the entry box
    def get_cursor(self,ev):
        cursor_row=self.Staff_Table.focus()
        contents=self.Staff_Table.item(cursor_row)
        row=contents['values']
        self.id_no_var.set(row[0])
        self.name_var.set(row[1])
        self.designation_var.set(row[2])
        self.gender_var.set(row[3])
        self.phone_no_var.set(row[4])
        self.email_var.set(row[5])
        self.txtaddress.delete("1.0",END)
        self.txtaddress.insert(END,row[6])


    #defining update function
    def update_data(self):
        conn=mysql.connector.connect(host="localhost",user="root",passwd="arun3114",database="mydatabase")
        cur=conn.cursor()
        cur.execute("update staff set name=%s,designation=%s,gender=%s,phoneno=%s,email=%s,address=%s where idno=%s",(
                                                                        self.name_var.get(),
                                                                        self.designation_var.get(),
                                                                        self.gender_var.get(),
                                                                        self.phone_no_var.get(),
                                                                        self.email_var.get(),
                                                                        self.txtaddress.get('1.0',END),
                                                                        self.id_no_var.get()
                                                                        ))


        conn.commit()
        self.fetch_data()
        self.clear()
        conn.close()
        messagebox.showinfo("SUCCESS","RECORD UPDATED")


    #defining delete function
    def delete_data(self):
        conn=mysql.connector.connect(host="localhost",user="root",passwd="arun3114",database="mydatabase")
        cur=conn.cursor()
        cur.execute("delete from staff where idno=%s",self.id_no_var.get())
        conn.commit()
        conn.close()
        self.fetch_data()
        self.clear()
        messagebox.showinfo("SUCCESS","RECORD DELETED")


    #defining search function
    def search_data(self):
        conn=mysql.connector.connect(host="localhost",user="root",passwd="arun3114",database="mydatabase")
        cur=conn.cursor()
        cur.execute("select * from staff where "+str(self.search_by.get())+" LIKE '%"+str(self.search_txt.get())+"%'")
        rows=cur.fetchall()
        if len(rows)!=0:
            self.Staff_Table.delete(*self.Staff_Table.get_children())
            for row in rows:
                self.Staff_Table.insert('',END,values=row)
            conn.commit()
        conn.close()


root=Tk()
ob=staff(root)
root.iconbitmap(r'F:/Staff circle test/scimage/logo.ico')
root.mainloop()
