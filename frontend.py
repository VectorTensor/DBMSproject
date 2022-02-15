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
        self.root.geometry("1280x720+0+0")
        lbltitle = Label(self.root, bd=20, relief=RIDGE, text="PROGRAMMEER'S LOG SYSTEM",
                         fg="red", bg="white", font=("times new roman", 50, "bold"))
        lbltitle.pack(side=TOP, fill=X)


root = Tk()
ob = Programmer(root)
root.mainloop()
