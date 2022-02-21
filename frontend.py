# tkinter code goes here
from tkinter import *
from tkinter import ttk   # tkinter library.
import random  # to generate random numbers.
import time
import datetime
from tkinter import messagebox
import backend


class Programmer:
    def __init__(self, root):
        self.root = root   # intialize the window of gui
        self.root.title("Programmer Log System")  # title of system
        # resolution + x-ais + y_axis start coordinate.
        self.root.geometry("1366x768+0+0")

        # defining variable for form inputs
        self.NameOfProgrammers = StringVar()
        self.IdOfProgrammers = StringVar()
        self.Password = StringVar()

        lbltitle = Label(self.root, bd=20, relief=RIDGE, text="PROGRAMMER'S LOG SYSTEM",
                         fg="red", bg="white", font=("times new roman", 50, "bold"))
        lbltitle.pack(side=TOP, fill=X)

        # creating 3 parts below the title form , buttons and details.
        Dataframe = Frame(self.root, bd=20, relief=RIDGE)
        Dataframe.place(x=0, y=130, width=1366, height=400)

        Dataframeleft = LabelFrame(Dataframe, bd=10, relief=RIDGE, padx=20,
                                   font=("arial", 12, "bold"), text="Programmer Info")
        Dataframeleft.place(x=0, y=5, width=980, height=350)

        DataFrameRight = LabelFrame(Dataframe, bd=10, relief=RIDGE, padx=10,
                                    font=("arial", 12, "bold"), text="Project Info")
        DataFrameRight.place(x=990, y=5, width=340, height=350)

        # =============================== Buttons frame =============================
        Buttonframe = Frame(self.root, bd=20, relief=RIDGE)
        Buttonframe.place(x=0, y=530, width=1366, height=70)

        # =============================== Details frame =============================
        Detailsframe = Frame(self.root, bd=20, relief=RIDGE)
        Detailsframe.place(x=0, y=600, width=1366, height=100)

        # ===============================  creating fields =============================
        # lblNameTablet = Label(Dataframeleft, text="First Name ",  font=("arial", 12, "bold"),
        #  padx=2, pady=6)
        # lblNameTablet.grid(row=0, column=0)

        # comNameTablet = ttk.Combobox(
        #    Dataframeleft, font=("arial", 12, "bold"), width=33)
        # comNameTablet["values"] = ('a', 'b', 'c')
        # comNameTablet.grid(row=0, column=1)

        # ===============================  creating fields =============================
        lblName = Label(Dataframeleft, font=("arial", 12, "bold"),
                        text="UserName", padx=2, pady=6)
        lblName.grid(row=0, column=0, sticky=W)
        txtName = Entry(Dataframeleft, textvariable=self.NameOfProgrammers, font=(
            "arial", 12, "bold"), width=35)
        txtName.grid(row=0, column=1)

        lblId = Label(Dataframeleft, font=("arial", 12, "bold"),
                      text="Id", padx=2, pady=6)
        lblId.grid(row=1, column=0, sticky=W)
        txtId = Entry(Dataframeleft, textvariable=self.IdOfProgrammers, font=(
            "arial", 12, "bold"), width=35)
        txtId.grid(row=1, column=1)

        lblPass = Label(Dataframeleft, font=("arial", 12, "bold"),
                        text="Password", padx=2, pady=6)
        lblPass.grid(row=2, column=0, sticky=W)
        txtPass = Entry(Dataframeleft, textvariable=self.Password,
                        font=("arial", 12, "bold"), width=35)
        txtPass.grid(row=2, column=1)

        # ===================================Datafrmae Right===============================
        self.textLog = Text(DataFrameRight, font=(
            "arial", 12, "bold"), width=23, height=16, padx=2, pady=6)
        self.textLog.grid(row=0, column=0)

        # ===================================Buttons Fields ==============================
        btnProgrammersInfo = Button(Buttonframe, command=self.iProgrammersInfo, text="Programmer", bg='green', fg='white', font=(
            "arial", 12, "bold"), width=21, height=1, padx=2, pady=6)
        btnProgrammersInfo.grid(row=0, column=0)

        btnLogInfo = Button(Buttonframe, text="LogInfo", bg='green', fg='white', font=(
            "arial", 12, "bold"), width=21, height=1, padx=2, pady=6)
        btnLogInfo.grid(row=0, column=1)

        btnUpdate = Button(Buttonframe, text="Update", bg='green', fg='white', font=(
            "arial", 12, "bold"), width=21, height=1, padx=2, pady=6)
        btnUpdate.grid(row=0, column=2)

        btnDelete = Button(Buttonframe, text="Delete", bg='green', fg='white', font=(
            "arial", 12, "bold"), width=21, height=1, padx=2, pady=6)
        btnDelete.grid(row=0, column=3)

        btnClear = Button(Buttonframe, text="Clear", bg='green', fg='white', font=(
            "arial", 12, "bold"), width=21, height=1, padx=2, pady=6)
        btnClear.grid(row=0, column=4)

        btnExit = Button(Buttonframe, text="Exit", bg='green', fg='white', font=(
            "arial", 12, "bold"), width=21, height=1, padx=2, pady=6)
        btnExit.grid(row=0, column=5)

        # =========================================Display Table==================================

        # =========================================Scroll Bar==================================
        scroll_x = ttk.Scrollbar(Detailsframe, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(Detailsframe, orient=VERTICAL)

        self.programmer_table = ttk.Treeview(Detailsframe, column=("name", "id", "a", "b"),
                                             xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)

        scroll_x = ttk.Scrollbar(command=self.programmer_table.xview)
        scroll_y = ttk.Scrollbar(command=self.programmer_table.yview)

        self.programmer_table.heading("name", text="Name")
        self.programmer_table["show"] = "headings"

        # setiing the width
        self.programmer_table.column("name", width=100)
        self.programmer_table.pack(fill=BOTH, expand=1)

    # ========================================== Functionality ====================

    def iProgrammersInfo(self):
        name = self.NameOfProgrammers.get()
        password = self.Password.get()
        print(self.NameOfProgrammers.get())
        print(self.Password.get())
        backend.insertUser(name, password)


root = Tk()
ob = Programmer(root)

root.mainloop()
