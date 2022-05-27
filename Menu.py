from tkinter import *
from tkinter import ttk
from tkinter import  messagebox
import pymysql
from PIL import ImageTk,Image

from course import Courses
from exam import Exam
from fees import Fees
from students import Student


class Menu :
    def __init__(self,root):
        self.root = root
        self.root.title("Student Data Management System")
        self.root.geometry("1360x710+0+0")

        title = Label(self.root , text="Student Data Management System" , bd=10 , relief=GROOVE , font=("Times new roman",40,"bold"),bg="#030939",fg="#9aecf9")
        title.pack(side=TOP,fill=X)

        MainFrame = Frame(self.root,bd=4, relief=RIDGE, bg="#9aecf9")
        MainFrame.place(x=0, y=100, width=1360,height=580)

        """logoFrame = Frame(MainFrame, relief=RIDGE, bg="#9aecf9")
        logoFrame.place(x=100, y=120, width=300,height=300)

        self.bg = ImageTk.PhotoImage(file="logo.jpg")
        self.bg_image = Label(logoFrame, image=self.bg).place(x=0, y=0, relwidth=1, relheight=1)

        stdFrame = Frame(MainFrame, relief=RIDGE, bg="#9aecf9")
        stdFrame.place(x=900, y=120, width=400, height=300)

        self.bg1 = ImageTk.PhotoImage(file="std.png")
        self.bgimg1 = Label(stdFrame, image=self.bg1).place(x=0, y=0, relwidth=1, relheight=1)"""

        btnFrame = Frame(MainFrame, relief=RIDGE, bg="#9aecf9")
        btnFrame.place(x=470, y=70, width=360,height=400)

        b1 = Button(btnFrame , text="Students Details" , width=20 ,font=("Times new roman",20,"bold"),bg="#030939",fg="white",bd=5 , command=self.students).grid(row=1 , column=15 , padx=10 , pady=20,columnspan=10)
        b2 = Button(btnFrame , text="Course Enrolment" , width=20 ,font=("Times new roman",20,"bold"),bg="#030939",fg="white",bd=5 , command=self.enrolled).grid(row=3 , column=15 , padx=10 , pady=20,columnspan=10)
        b3 = Button(btnFrame , text="Fees Details" , width=20 ,font=("Times new roman",20,"bold"),bg="#030939",fg="white",bd=5 , command=self.fees).grid(row=5 , column=10 , padx=10 , pady=20,columnspan=10)
        b4 = Button(btnFrame , text="Exam Details" , width=20 ,font=("Times new roman",20,"bold"),bg="#030939",fg="white",bd=5 , command=self.takes).grid(row=7 , column=10 , padx=10 , pady=20,columnspan=10)

    def students(self):
        r1=Tk()
        Student(r1)


    def enrolled(self):
        r1 = Tk()
        Courses(r1)

    def fees(self):
        r1 = Tk()
        Fees(r1)

    def takes(self):
        r1 = Tk()
        Exam(r1)


"""root = Tk()
ob = Menu(root)
root.mainloop()"""






