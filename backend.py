# backend code goes here 
import sqlite3




def create():
	# This creates the tables
	con = sqlite3.connect('WonderOfU.db')
	con.execute('''CREATE TABLE Project (Name varchar,id int,Description varchar)''')
	con.commit()
	con.close()



def drop():
	con= sqlite3.connect('WonderOfU.db')
	con.execute('''drop table Project''' )
	con.commit()
	con.close()


def show():
	con=sqlite3.connect('WonderOfU.db')
	x=con.execute('''Select * from Project''')
	print(x)
	con.commit()
	con.close()



def insert():
	con=sqlite3.connect('WonderOfU.db')
	con.execute('''insert into Project values('Praysdhif',5,'dfasfsd')''')
	con.commit()
	con.close()




