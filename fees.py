from tkinter import *
from tkinter import ttk
from tkinter import  messagebox
import pymysql

class Fees :
    def __init__(self,root):
        self.root = root
        self.root.title("Course Enrollment")
        self.root.geometry("1360x710+0+0")

        title = Label(self.root , text="Student Data Management System " , bd=10 , relief=GROOVE , font=("Times new roman",40,"bold"),bg="#9aecf9",fg="#030939")
        title.pack(side=TOP,fill=X)

        # ---------- All Variables ----------

        self.TId = StringVar()
        self.amt = IntVar()
        self.scholarship = IntVar()
        self.income = IntVar()
        self.roll = StringVar()

    # ---------- Manage Frame ----------

        ManageFrame = Frame(self.root, bd=4, relief=RIDGE, bg="#030939")
        ManageFrame.place(x=20, y=100, width=560, height=590)

        m_title = Label(ManageFrame, text="Manage Students Fees", bg="#030939", fg="white",font=("Times new roman", 30, "bold"))
        m_title.grid(row=0, columnspan=2, pady=20)

        self.lblRoll = Label(ManageFrame, text="Roll No", bg="#030939", fg="white", font=("Times new roman", 20, "bold"))
        self.lblRoll.grid(row=1, column=0, pady=10, padx=20, sticky="w")

        self.txtRoll = Entry(ManageFrame, textvariable=self.roll, font=("Times new roman", 15, "bold"), bd=5, relief=GROOVE)
        self.txtRoll.grid(row=1, column=1, pady=10, padx=20, sticky="w")

        self.lblName = Label(ManageFrame, text="Transaction Id", bg="#030939", fg="white", font=("Times new roman", 20, "bold"))
        self.lblName.grid(row=2, column=0, pady=10, padx=20, sticky="w")

        self.txtTid = Entry(ManageFrame, textvariable=self.TId, font=("Times new roman", 15, "bold"), bd=5, relief=GROOVE)
        self.txtTid.grid(row=2, column=1, pady=10, padx=20, sticky="w")

        self.lblamt = Label(ManageFrame, text="Amount", bg="#030939", fg="white", font=("Times new roman", 20, "bold"))
        self.lblamt.grid(row=3, column=0, pady=10, padx=20, sticky="w")

        self.txtamt = Entry(ManageFrame, textvariable=self.amt, font=("Times new roman", 15, "bold"), bd=5,relief=GROOVE)
        self.txtamt.grid(row=3, column=1, pady=10, padx=20, sticky="w")

        self.lblsch = Label(ManageFrame, text="Scholarship", bg="#030939", fg="white", font=("Times new roman", 20, "bold"))
        self.lblsch.grid(row=4, column=0, pady=10, padx=20, sticky="w")

        self.txtsch = Entry(ManageFrame, textvariable=self.scholarship, font=("Times new roman", 15, "bold"), bd=5, relief=GROOVE)
        self.txtsch.grid(row=4, column=1, pady=10, padx=20, sticky="w")

        self.lblinc = Label(ManageFrame, text="Income", bg="#030939", fg="white", font=("Times new roman", 20, "bold"))
        self.lblinc.grid(row=5, column=0, pady=10, padx=20, sticky="w")

        self.txtinc = Entry(ManageFrame, textvariable=self.income, font=("Times new roman", 15, "bold"), bd=5, relief=GROOVE)
        self.txtinc.grid(row=5, column=1, pady=10, padx=20, sticky="w")

    # ---------- Button Frame ----------

        ButtonFrame = Frame(ManageFrame, relief=RIDGE, bg="#030939")
        ButtonFrame.place(x=70, y=420, width=420)

        enroll = Button(ButtonFrame, text="Submit", width=10,font=("Times new roman", 15, "bold"),bg="lightgray", command=self.enrollStudents).grid(row=0, column=0, pady=10, padx=20, sticky="w")
        clear = Button(ButtonFrame , text="Clear", width=10,font=("Times new roman", 15, "bold"),bg="lightgray",command=self.clear).grid(row=0, column=1, pady=10, padx=20, sticky="w")

    # ---------- Details Frame ----------

        DetailsFrame = Frame(self.root, bd=4, relief=RIDGE, bg="#030939")
        DetailsFrame.place(x=600, y=100, width=720, height=590)

        lblCourses = Label(DetailsFrame , text="Fees Details", bg="#030939", fg="white", font=("Times new roman", 25, "bold"))
        lblCourses.pack()

    # ---------- Information Frame --------

        infoFrame = Frame(DetailsFrame, relief=RIDGE, bg="#030939")
        infoFrame.place(x=10, y=500, width=700, height=60)

        self.lblinfo = Label(infoFrame, text="", bg="#030939", fg="white", font=("Times new roman", 20, "bold"))
        self.lblinfo.grid(row=0, column=0, pady=10, padx=20, sticky="w")

    # ---------- Table Frame ----------

        TableFrame = Frame(DetailsFrame, bd=4, relief=RIDGE, bg="#030939")
        TableFrame.place(x=10, y=70, width=700, height=400)

        self.StudentTable = ttk.Treeview(TableFrame,columns=("TId","Amount","Income","Scholarship","Roll_No"))
        self.StudentTable.heading("TId", text="Transaction Id")
        self.StudentTable.heading("Amount", text="Amount")
        self.StudentTable.heading("Income", text="Income")
        self.StudentTable.heading("Scholarship", text="Scholarship")
        self.StudentTable.heading("Roll_No",text="Roll No")

        self.StudentTable["show"] = "headings"
        self.StudentTable.column("TId", width=70)
        self.StudentTable.column("Amount", width=170)
        self.StudentTable.column("Income", width=50)
        self.StudentTable.column("Scholarship", width=50)
        self.StudentTable.column("Roll_No", width=50)
        self.StudentTable.pack(fill=BOTH, expand=1)
        self.fetchData()

    def enrollStudents(self):
        self.lblinfo.config(text="")
        try :
            if self.txtRoll.get() == "" or self.txtTid.get() == "":
                self.lblinfo.config(text="Mandatory fields left empty !!")
                #messagebox.showerror("Error","Mandatory fields left empty !!")
            else:
                conn = pymysql.connect(host="LOCALHOST", user="root", password="", database="dbms")
                cur = conn.cursor()
                cur.execute("insert into fees values(%s,%s,%s,%s,%s)", (self.txtTid.get(),self.txtamt.get(),self.txtamt.get(),self.txtsch.get(),self.txtRoll.get()))
                conn.commit()
                self.clear()
                self.fetchData()
                conn.close()
                self.lblinfo.config(text="Record inserted")
                #messagebox.showinfo("Success" , "Record inserted")
        except:
            self.lblinfo.config(text="Invalid Roll no / Transaction id")
            #messagebox.showerror("Error","Invalid Roll no / Transaction id ")

    def fetchData(self):
        self.lblinfo.config(text="")
        conn = pymysql.connect(host="LOCALHOST", user="root", password="", database="dbms")
        cur = conn.cursor()
        cur.execute("select * from fees")
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
        self.txtamt.delete(0, END)
        self.txtsch.delete(0, END)
        self.txtinc.delete(0, END)
        self.txtTid.delete(0, END)


"""
root = Tk()
ob = Fees(root)
root.mainloop()
"""