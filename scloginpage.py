from tkinter import*
from PIL import ImageTk
from tkinter import messagebox
from datetime import datetime
import os
class Login:
    def __init__(self,root):
        self.root=root
        self.root.title("Staff Circle Login")
        self.root.geometry("1199x650+100+50")
        self.root.resizable(False,False)

        
        ##background image 
        self.bg=ImageTk.PhotoImage(file="C:/Staff Circle/images/bg.jpg")
        self.bg_image=Label(self.root,image=self.bg).place(x=0,y=0,relwidth=1,relheight=1)


        ##login frame
        Frame_login=Frame(self.root,bg="lightgrey")
        Frame_login.place(x=390,y=180,height=300,width=430)


        #title
        title=Label(Frame_login,text="ADMIN LOGIN",font=("Eurostile Bold",26,"bold"),fg="black",bg="lightgrey").place(x=95,y=30)


        #Detail box for username and password
        #username box
        lbl_user=Label(Frame_login,text="Username",font=("Eurostile Bold",16,"bold"),fg="black",bg="lightgrey").place(x=66,y=100)
        self.txt_user=Entry(Frame_login,font=("times new roman",15),bg="white")
        self.txt_user.place(x=66,y=140,width=300,height=35)

        #password box
        lbl_pass=Label(Frame_login,text="Password",font=("Eurostile Bold",16,"bold"),fg="black",bg="lightgrey").place(x=66,y=185)
        self.txt_pass=Entry(Frame_login,font=("times new roman",15),show='*',bg="white")
        self.txt_pass.place(x=66,y=225,width=300,height=35)


        #login button
        login_btn=Button(self.root,command=self.login_function,cursor="hand2",text="Login",bg="lightgray",fg="black",bd=1,font=("Eurostile Bold",17)).place(x=530,y=455,width=150)

        #time
        now = datetime.now()

        dt_string = now.strftime("%B %d, %Y - %H:%M:%S")
        current_time = Label(root, text=str(dt_string)).place(x=1050, y=620)

    #working of the login function (login button) with messagebox that displays message
    def login_function(self):
        if self.txt_user.get()=="" or self.txt_pass.get()=="":
            messagebox.showerror("Error","All fields are required",parent=self.root)
        elif self.txt_pass.get()!="12345" or self.txt_user.get()!="Arun":
            messagebox.showerror("Error","Invalid Username or Password",parent=self.root)
        else:
            messagebox.showinfo("Welcome",f"Logined as Admin:{self.txt_user.get()}",parent=self.root)
            self.root.destroy()
            #this function closes the login page and opens the working page
            import scwork


   
root=Tk()
obj=Login(root)
#logo 
root.iconbitmap(r'C:/Staff Circle/images/logo.ico')
root.mainloop()
