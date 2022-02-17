# pygame code goes here
from tkinter import *
from tkinter import ttk   # tkinter library.
import random  # to generate random numbers.
import time
import datetime
from tkinter import messagebox
import sqlite3


class Programmer:
    def __init__(self, root):
        self.root = root   # intialize the window of gui
        self.root.title("Programmer Log System")  # title of system
        # resolution + x-ais + y_axis start coordinate.
        self.root.geometry("1366x768+0+0")
        lbltitle = Label(self.root, bd=20, relief=RIDGE, text="PROGRAMMEER'S LOG SYSTEM",
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


root = Tk()
ob = Programmer(root)
root.mainloop()
