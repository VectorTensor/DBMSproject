# backend code goes here 
import sqlite3




def create():
	# This creates the tables
	con = sqlite3.connect('WonderOfU.db')
	con.execute('''CREATE TABLE Project (Name varchar,id INTEGER PRIMARY KEY AUTOINCREMENT,Description varchar)''')
	con.execute('''CREATE TABLE Log(DOR date,Project_id int,Log varchar, Author_id int )''')
	con.execute('''CREATE TABLE Programmer(Name varchar, id INTEGER PRIMARY KEY AUTOINCREMENT, password varchar)''')
	con.commit()
	con.close()

def insertUser(Name,password):
	# This method creates a new user 
	con = sqlite3.connect('WonderOfU.db')
	con.execute("""INSERT INTO Programmer(Name,password) values(:name,:password)""",{"name":Name,"password":password})
	con.commit()
	con.close()	

	# call this method to check the credentials	
def IsUser(Name,password):
	con = sqlite3.connect("WonderOfU.db")
	datas=con.execute("""SELECT * from Programmer where Name=:name""",{"name":Name})
	x=(list(datas))

	
	if (len(x)>0):

		for data in x:
		
			if (data[2]== password):

				con.commit()
				con.close()	
# Set name 
				return True
	
	con.commit()
	con.close()	
	return False

def AddProject(Name,Description):
	con= sqlite3.connect('WonderOfU.db')
	con.execute(""" insert into Project(Name,Description) values(:name,:description)""",{"name":Name,"description":Description})
	con.commit()
	con.close()


def drop():
	con= sqlite3.connect('WonderOfU.db')
	con.execute('''drop table Project''' )
	con.execute('''drop table Programmer''' )
	con.execute('''drop table Log''' )
	con.commit()
	con.close()



def insert():
	con=sqlite3.connect('WonderOfU.db')
	con.execute('''insert into Project values('Praysdhif',5,'dfasfsd')''')
	con.commit()
	con.close()




