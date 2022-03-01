# tkinter code goes here
from tkinter import *
from tkinter import ttk   # tkinter library.
from tkinter import messagebox
import backend


class Display:
    def __init__(self, root, data, *args):
        self.root = root   # intialize the window of gui
        self.columnList = []

        for arg in args:
            self.columnList.append(arg)

        # resolution + x-ais + y_axis start coordinate.
        self.root.geometry("1024x720+0+0")

        Detailsframe = Frame(self.root, bd=20, relief=RIDGE)
        Detailsframe.place(x=0, y=0, width=1000, height=700)

        scroll_x = ttk.Scrollbar(Detailsframe, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(Detailsframe, orient=VERTICAL)

        self.display_table = ttk.Treeview(Detailsframe, column=self.columnList,
                                          xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)

        scroll_x = ttk.Scrollbar(command=self.display_table.xview)
        scroll_y = ttk.Scrollbar(command=self.display_table.yview)

        for columns in self.columnList:
            self.display_table.heading(columns, text=columns)
            self.display_table.column(columns, anchor="center")
        self.display_table["show"] = "headings"

    # setting the width

        self.display_table.pack(fill=BOTH, expand=1)

        for i in data:
            self.display_table.insert("", END, values=i,)


class Programmer:
    def __init__(self, root):
        self.root = root   # intialize the window of gui
        self.root.title("Programmer Log System")  # title of system
        # resolution + x-ais + y_axis start coordinate.
        self.root.geometry("1366x768+0+0")

        # defining variable for form inputs
        self.NameOfProgrammers = StringVar()
        self.Password = StringVar()
        self.ProjectName = StringVar()
        self.AuthorName = StringVar()
        self.InsertId = StringVar()

        lbltitle = Label(self.root, bd=20, relief=RIDGE, text="PROGRAMMER'S LOG SYSTEM",
                         fg="red", bg="white", font=("times new roman", 50, "bold"))
        lbltitle.pack(side=TOP, fill=X)

        # creating 3 parts below the title form , buttons and details.
        Dataframe = Frame(self.root, bd=20, relief=RIDGE)
        Dataframe.place(x=0, y=130, width=1366, height=400)

        Dataframeleft = LabelFrame(Dataframe, bd=10, relief=RIDGE, padx=20,
                                   font=("arial", 12, "bold"), text="Programmer Info")
        Dataframeleft.place(x=0, y=5, width=500, height=350)

        DataFrameRight = LabelFrame(Dataframe, bd=10, relief=RIDGE, padx=10,
                                    font=("arial", 12, "bold"), text="Project Log")
        DataFrameRight.place(x=950, y=5, width=370, height=350)

        DataFrameMid = LabelFrame(Dataframe, bd=10, relief=RIDGE, padx=10,
                                  font=("arial", 12, "bold"), text="Project Info")
        DataFrameMid.place(x=510, y=5, width=430, height=350)

        # =============================== Buttons frame =============================
        Buttonframe = Frame(self.root, bd=20, relief=RIDGE)
        Buttonframe.place(x=0, y=530, width=1366, height=200)

        # =============================== Details frame =============================

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

        lblPass = Label(Dataframeleft, font=("arial", 12, "bold"),
                        text="Password", padx=2, pady=6)
        lblPass.grid(row=2, column=0, sticky=W)
        txtPass = Entry(Dataframeleft, textvariable=self.Password,
                        font=("arial", 12, "bold"), width=35)
        txtPass.grid(row=2, column=1)

        # ===================================Datafrmae Right===============================
        lblAuthorName = Label(DataFrameRight, font=("arial", 12, "bold"),
                              text="AuthorName", padx=2, pady=6)
        lblAuthorName.grid(row=0, column=0, sticky=W)
        txtAuthorName = Entry(DataFrameRight, textvariable=self.AuthorName, font=(
            "arial", 12, "bold"), width=25)
        txtAuthorName.grid(row=0, column=1)

        lblNameProj = Label(DataFrameRight, font=("arial", 12, "bold"),
                            text="ProjectName", padx=2, pady=6)
        lblNameProj.grid(row=1, column=0, sticky=W)
        txtNameProj = Entry(DataFrameRight, textvariable=self.ProjectName, font=(
            "arial", 12, "bold"), width=25)
        txtNameProj.grid(row=1, column=1)

        lblLogDesc = Label(DataFrameRight, font=("arial", 12, "bold"),
                           text="Log", padx=2, pady=6)
        lblLogDesc.grid(row=2, column=0, sticky=W)
        self.textLog = Text(DataFrameRight, font=(
            "arial", 12, "bold"), width=25, height=5, padx=2, pady=6)
        self.textLog.grid(row=2, column=1)

        # ===================================Datafrmae Mid===============================
        lblNameProj = Label(DataFrameMid, font=("arial", 12, "bold"),
                            text="ProjectName", padx=2, pady=6)
        lblNameProj.grid(row=0, column=0, sticky=W)
        txtNameProj = Entry(DataFrameMid, textvariable=self.ProjectName, font=(
            "arial", 12, "bold"), width=30)
        txtNameProj.grid(row=0, column=1)

        lblProjDesc = Label(DataFrameMid, font=("arial", 12, "bold"),
                            text="Description", padx=2, pady=6)
        lblProjDesc.grid(row=1, column=0, sticky=W)
        self.projDesc = Text(DataFrameMid, font=(
            "arial", 12, "bold"), width=30, height=5, padx=2, pady=6)
        self.projDesc.grid(row=2, column=1)

        # ===================================Buttons Fields ==============================
        btnProgrammersInfo = Button(Dataframeleft, command=self.iProgrammersInfo, text="Insert", bg='green', fg='white', font=(
            "arial", 12, "bold"), width=10, height=0, padx=2, pady=6)
        btnProgrammersInfo.grid(row=10, column=0)

        btnProgrammerInfoShow = Button(Dataframeleft, command=self.displayProgrammer, text="Info", bg='green', fg='white', font=(
            "arial", 12, "bold"), width=10, height=0, padx=2, pady=6)
        btnProgrammerInfoShow.grid(row=10, column=1)

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

        btnProjInfo = Button(DataFrameMid, text="Insert", command=self.iProjectInfo, bg='green', fg='white', font=(
            "arial", 12, "bold"), width=10, height=0, padx=2, pady=6)
        btnProjInfo.grid(row=4, column=0)

        btnProjInfoShow = Button(DataFrameMid, text="Show", command=self.displayProject, bg='green', fg='white', font=(
            "arial", 12, "bold"), width=10, height=0, padx=2, pady=6)
        btnProjInfoShow.grid(row=4, column=1)

        btnLogInfo = Button(DataFrameRight, command=self.iLogInfo, text="Insert", bg='green', fg='white', font=(
            "arial", 12, "bold"), width=10, height=0, padx=2, pady=6)
        btnLogInfo.grid(row=10, column=0)
        btnLogInfo = Button(DataFrameRight, command=self.displayLog, text="Show", bg='green', fg='white', font=(
            "arial", 12, "bold"), width=10, height=0, padx=2, pady=6)
        btnLogInfo.grid(row=10, column=1)

        # =========================================Display Table==================================

        # =========================================Scroll Bar==================================

    # ========================================== Functionality ====================

    def iProgrammersInfo(self):
        name = self.NameOfProgrammers.get()
        password = self.Password.get()
        print(self.NameOfProgrammers.get())
        print(self.Password.get())
        backend.insertUser(name, password)
        root1 = Tk()
        ob1 = Display(root1, "Name", "ID")

    def iProjectInfo(self):
        projName = self.ProjectName.get()
        projDesc = self.projDesc.get("1.0", END)
        print(projName)
        print(projDesc)
        backend.AddProject(projName, projDesc)

    def iLogInfo(self):
        authorName = self.AuthorName.get()
        projLog = self.textLog.get("1.0", END)
        projName = self.ProjectName.get()
        print(authorName)
        print(projLog)
        print(projName)
        backend.AddLog(projLog, projName, authorName)

    def displayProgrammer(self):
        data = backend.ShowProgrammers()
        print(data)
        root1 = Tk()
        ob1 = Display(root1, data, "Name", "ID", "Password")

    def displayProject(self):
        data = backend.ShowProjects()
        print(data)
        root1 = Tk()
        ob1 = Display(root1, data, "ProjectName", "Project_ID", "Description")

    def displayLog(self):
        data = backend.ShowLogInfo()
        print(data)
        root1 = Tk()
        ob1 = Display(root1, data, "Log Date",
                      "Project_ID", "Log", "Author_ID")

    def joinLog(self):
        id = self.InsertId.get()
        data = backend.ShowLogs(id)
        print(data)
        root1 = Tk()
        ob1 = Display(root1, data, "Log Date",
                      "Log", "Programmer Name")


root = Tk()
ob = Programmer(root)
root.mainloop()
