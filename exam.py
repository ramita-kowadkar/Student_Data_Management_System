from tkinter import *
from tkinter import ttk
from tkinter import  messagebox
import pymysql

class Exam :
    def __init__(self,root):
        self.root = root
        self.root.title("Course Enrollment")
        self.root.geometry("1360x710+0+0")

        title = Label(self.root , text="Student Data Management System " , bd=10 , relief=GROOVE , font=("Times new roman",40,"bold"),bg="#9aecf9",fg="#030939")
        title.pack(side=TOP,fill=X)

        # ---------- All Variables ----------

        self.roll = StringVar()
        self.eid = StringVar()
        self.etype = StringVar()
        self.edate = StringVar()
        self.marks = IntVar()
        self.cid = StringVar()

    # ---------- Manage Frame ----------

        ManageFrame = Frame(self.root, bd=4, relief=RIDGE, bg="#030939")
        ManageFrame.place(x=20, y=100, width=560, height=590)

        m_title = Label(ManageFrame, text="Exam Enrolment ", bg="#030939", fg="white",font=("Times new roman", 30, "bold"))
        m_title.grid(row=0, columnspan=2, pady=20)

        self.lblroll = Label(ManageFrame, text="Roll No", bg="#030939", fg="white", font=("Times new roman", 20, "bold"))
        self.lblroll.grid(row=1, column=0, pady=10, padx=20, sticky="w")

        self.txtroll = Entry(ManageFrame, textvariable=self.roll, font=("Times new roman", 15, "bold"), bd=5, relief=GROOVE)
        self.txtroll.grid(row=1, column=1, pady=10, padx=20, sticky="w")

        self.lbleid = Label(ManageFrame, text="Exam Id", bg="#030939", fg="white", font=("Times new roman", 20, "bold"))
        self.lbleid.grid(row=2, column=0, pady=10, padx=20, sticky="w")

        self.txteid = Entry(ManageFrame, textvariable=self.eid, font=("Times new roman", 15, "bold"), bd=5, relief=GROOVE)
        self.txteid.grid(row=2, column=1, pady=10, padx=20, sticky="w")


    # ---------- Button Frame ----------

        ButtonFrame = Frame(ManageFrame, relief=RIDGE, bg="#030939")
        ButtonFrame.place(x=50, y=240, width=420)

        enroll = Button(ButtonFrame, text="Submit", width=10, font=("Times new roman", 15, "bold"), bg="lightgray",command=self.enrollStudents).grid(row=0, column=0, pady=10, padx=20, sticky="w")
        clear = Button(ButtonFrame, text="Clear", width=10, font=("Times new roman", 15, "bold"), bg="lightgray",command=self.clear).grid(row=0, column=1, pady=10, padx=20, sticky="w")
    # ---------- Details Frame ----------

        DetailsFrame = Frame(self.root, bd=4, relief=RIDGE, bg="#030939")
        DetailsFrame.place(x=600, y=100, width=720, height=590)

        lblCourses = Label(DetailsFrame , text="Exam Details", bg="#030939", fg="white", font=("Times new roman", 25, "bold"))
        lblCourses.pack()

        # ---------- Information Frame --------

        infoFrame = Frame(DetailsFrame, relief=RIDGE, bg="#030939")
        infoFrame.place(x=10, y=500, width=700, height=60)

        self.lblinfo = Label(infoFrame, text="", bg="#030939", fg="white", font=("Times new roman", 20, "bold"))
        self.lblinfo.grid(row=0, column=0, pady=10, padx=20, sticky="w")

    # ---------- Table Frame ----------

        TableFrame = Frame(DetailsFrame, bd=4, relief=RIDGE, bg="#030939")
        TableFrame.place(x=10, y=70, width=700, height=400)

        self.StudentTable = ttk.Treeview(TableFrame,columns=("EId","Etype","EDate","Marks","CId"))
        self.StudentTable.heading("EId", text="Exam Id")
        self.StudentTable.heading("Etype", text="Exam Type")
        self.StudentTable.heading("EDate", text="Exam Date")
        self.StudentTable.heading("Marks", text="Marks")
        self.StudentTable.heading("CId",text="Course Id")

        self.StudentTable["show"] = "headings"
        self.StudentTable.column("EId", width=70)
        self.StudentTable.column("Etype", width=170)
        self.StudentTable.column("EDate", width=50)
        self.StudentTable.column("Marks", width=50)
        self.StudentTable.column("CId", width=50)
        self.StudentTable.pack(fill=BOTH, expand=1)
        self.fetchData()

    def enrollStudents(self):
        self.lblinfo.config(text="")
        try :
            if self.txtroll.get() == "" or self.txteid.get() == "":
                self.lblinfo.config(text="Mandatory fields left empty !!")
                #messagebox.showerror("Error","Mandatory fields left empty !!")
            else:
                conn = pymysql.connect(host="LOCALHOST", user="root", password="", database="dbms")
                cur = conn.cursor()
                cur.execute("insert into takes values(%s,%s)", (self.txtroll.get(),self.txteid.get()))
                conn.commit()
                self.clear()
                conn.close()
                self.lblinfo.config(text="Record Inserted !!")
                #messagebox.showinfo("Success" , "Record inserted")
        except:
            self.lblinfo.config(text="Invalid Roll no / Exam id")
            #messagebox.showerror("Error","Invalid Roll no / Exam id ")

    def fetchData(self):
        self.lblinfo.config(text="")
        conn = pymysql.connect(host="LOCALHOST", user="root", password="", database="dbms")
        cur = conn.cursor()
        cur.execute("select * from exam")
        rows = cur.fetchall()
        if len(rows) != 0 :
            self.StudentTable.delete(*self.StudentTable.get_children())
            for row in rows:
                self.StudentTable.insert('',END,values=row)
            conn.commit()
        conn.close()

    def clear(self):
        self.lblinfo.config(text="")
        self.txtroll.delete(0, END)
        self.txteid.delete(0, END)

"""
root = Tk()
ob = Exam(root)
root.mainloop()
"""