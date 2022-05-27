from tkinter import *
from tkinter import ttk
from tkinter import  messagebox
import pymysql

class Courses :
    def __init__(self,root):
        self.root = root
        self.root.title("Course Enrollment")
        self.root.geometry("1360x710+0+0")

        title = Label(self.root , text="Course Enrollment" , bd=10 , relief=GROOVE , font=("Times new roman",40,"bold"),bg="#9aecf9",fg="#030939")
        title.pack(side=TOP,fill=X)

        # ---------- All Variables ----------

        self.roll = StringVar()
        self.cname = StringVar()
        self.cid = StringVar()

    # ---------- Manage Frame ----------

        ManageFrame = Frame(self.root, bd=4, relief=RIDGE, bg="#030939")
        ManageFrame.place(x=20, y=100, width=560, height=590)

        m_title = Label(ManageFrame, text="Manage Students Enrollment", bg="#030939", fg="white",font=("Times new roman", 30, "bold"))
        m_title.grid(row=0, columnspan=2, pady=20)

        self.lblRoll = Label(ManageFrame, text="Roll No", bg="#030939", fg="white",font=("Times new roman", 20, "bold"))
        self.lblRoll.grid(row=2, column=0, pady=10, padx=20, sticky="w")

        self.txtRoll = Entry(ManageFrame, textvariable=self.roll, font=("Times new roman", 15, "bold"), bd=5,
                             relief=GROOVE)
        self.txtRoll.grid(row=2, column=1, pady=10, padx=20, sticky="w")

        self.lblCName = Label(ManageFrame, text="Course Name", bg="#030939", fg="white",font=("Times new roman", 20, "bold"))
        self.lblCName.grid(row=3, column=0, pady=10, padx=20, sticky="w")

        self.txtCName = Entry(ManageFrame, textvariable=self.cname, font=("Times new roman", 15, "bold"), bd=5,relief=GROOVE)
        self.txtCName.grid(row=3, column=1, pady=10, padx=20, sticky="w")

        self.lblCId = Label(ManageFrame, text="Course Id", bg="#030939", fg="white",font=("Times new roman", 20, "bold"))
        self.lblCId.grid(row=4, column=0, pady=10, padx=20, sticky="w")

        self.txtCId = Entry(ManageFrame, textvariable=self.cid, font=("Times new roman", 15, "bold"), bd=5,relief=GROOVE)
        self.txtCId.grid(row=4, column=1, pady=10, padx=20, sticky="w")

    # ---------- Button Frame ----------

        ButtonFrame = Frame(ManageFrame, relief=RIDGE, bg="#030939")
        ButtonFrame.place(x=90, y=320, width=450)

        enroll = Button(ButtonFrame, text="Submit", width=10, font=("Times new roman", 15, "bold"), bg="lightgray",command=self.enrollStudents).grid(row=0, column=0, pady=10, padx=20, sticky="w")
        clear = Button(ButtonFrame, text="Clear", width=10, font=("Times new roman", 15, "bold"), bg="lightgray",command=self.clear).grid(row=0, column=1, pady=10, padx=20, sticky="w")

    # ---------- Details Frame ----------

        DetailsFrame = Frame(self.root, bd=4, relief=RIDGE, bg="#030939")
        DetailsFrame.place(x=600, y=100, width=720, height=590)

        lblCourses = Label(DetailsFrame , text="Courses", bg="#030939", fg="white", font=("Times new roman", 25, "bold"))
        lblCourses.pack()

    # ---------- Information Frame --------

        infoFrame = Frame(DetailsFrame, relief=RIDGE, bg="#030939")
        infoFrame.place(x=10, y=500, width=700, height=60)

        self.lblinfo = Label(infoFrame, text="", bg="#030939", fg="white", font=("Times new roman", 20, "bold"))
        self.lblinfo.grid(row=0, column=0, pady=10, padx=20, sticky="w")

    # ---------- Table Frame ----------

        TableFrame = Frame(DetailsFrame, bd=4, relief=RIDGE, bg="#030939")
        TableFrame.place(x=10, y=70, width=700, height=400)

        self.StudentTable = ttk.Treeview(TableFrame,columns=("CId","CName","Credits","Duration"))
        self.StudentTable.heading("CId", text="Course Id")
        self.StudentTable.heading("CName", text="Course Name")
        self.StudentTable.heading("Credits", text="Credits")
        self.StudentTable.heading("Duration", text="Duration")

        self.StudentTable["show"] = "headings"
        self.StudentTable.column("CId", width=70)
        self.StudentTable.column("CName", width=170)
        self.StudentTable.column("Credits", width=50)
        self.StudentTable.column("Duration", width=50)
        self.StudentTable.pack(fill=BOTH, expand=1)
        self.fetchData()

    def enrollStudents(self):
        self.lblinfo.config(text="")
        try :
            if self.txtRoll.get() == "" or self.txtCName.get() == "" or self.txtCId.get() == "":
                self.lblinfo.config(text="Mandatory fields left empty !!")
                #messagebox.showerror("Error","Mandatory fields left empty !!")
            else:
                conn = pymysql.connect(host="LOCALHOST", user="root", password="", database="dbms")
                cur = conn.cursor()
                cur.execute("insert into enrolled values(%s,%s,%s)", (self.txtRoll.get(),self.txtCId.get(),self.txtCName.get()))
                conn.commit()
                self.clear()
                conn.close()
                self.lblinfo.config(text="Record Inserted")
                #messagebox.showinfo("Success" , "Record inserted")
        except:
            self.lblinfo.config(text="Invalid Roll no / Course id")
            #messagebox.showerror("Error","Invalid Roll no / Course id ")

    def fetchData(self):
        self.lblinfo.config(text="")
        conn = pymysql.connect(host="LOCALHOST", user="root", password="", database="dbms")
        cur = conn.cursor()
        cur.execute("select * from courses")
        rows = cur.fetchall()
        if len(rows) != 0 :
            self.StudentTable.delete(*self.StudentTable.get_children())
            for row in rows:
                self.StudentTable.insert('',END,values=row)
            conn.commit()
        conn.close()

    def clear(self):
        self.lblinfo.config(text="")
        self.txtRoll.delete(0, END)
        self.txtCId.delete(0, END)
        self.txtCName.delete(0, END)

"""
root = Tk()
ob = Courses(root)
root.mainloop()
"""