from tkinter import *
from tkinter import messagebox
from PIL import ImageTk
from Menu import Menu

class Login:
    def __init__(self,root):
        self.root=root
        self.root.title("Login")
        self.root.geometry("1360x710+0+0")
        #self.root.resizable(False,False)

        # ---------- Background Image ----------
        self.bg = ImageTk.PhotoImage(file="clg.jpg")
        self.bg_image = Label(self.root,image=self.bg).place(x=0 , y=0 , relwidth=1 , relheight=1)

        # ---------- Login Frame ----------
        loginFrame = Frame(self.root , bg="#dffaf9")
        loginFrame.place(x=100 , y=150 , height=400 , width=535)

        title = Label(loginFrame , text="Login Here" , font=("Impact",35,"bold") , fg="#030939" , bg="#dffaf9").place(x=90,y=30)
        desc = Label(loginFrame , text="Faculty / Admin Login Area" , font=("Goudy old style",15,"bold") , fg="#030939" , bg="#dffaf9").place(x=90,y=100)

        lblUser = Label(loginFrame , text="Username" , font=("Goudy old style",15,"bold") , fg="#030939" , bg="#dffaf9").place(x=90,y=140)
        self.txtUser = Entry(loginFrame , font=("times new roman",15) , bg="lightgray")
        self.txtUser.place(x=90,y=170,width=350,height=35)

        lblPassword = Label(loginFrame, text="Password", font=("Goudy old style", 15, "bold"), fg="#030939", bg="#dffaf9").place(x=90, y=220)
        self.txtPassword = Entry(loginFrame, font=("times new roman", 15), bg="lightgray" , show="*")
        self.txtPassword.place(x=90, y=250, width=350, height=35)

        loginBtn = Button(self.root , text="Login" , fg="#dffaf9" , bg="#030939" , font=("times new roman",20) , command=self.loginFtn).place(x=250,y=470,width=180,height=40)

    def loginFtn(self):
        if self.txtPassword.get()=="" or self.txtUser.get()=="":
            messagebox.showerror("Error","All fields are required",parent=self.root)
        elif self.txtUser.get() != "Admin12345" or self.txtPassword.get() != "admin@5":
            messagebox.showerror("Error","Invalid Username/Password",parent=self.root)
        else:
            self.txtPassword.delete(0 , END)
            self.txtUser.delete(0 , END)
            messagebox.showinfo("Welcome","Successful Login")
            r1=Tk()
            Menu(r1)


root = Tk()
obj = Login(root)
root.mainloop()