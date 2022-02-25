# backend code goes here 
import sqlite3
from datetime import date




def create():
	# This creates the tables
	con = sqlite3.connect('WonderOfU.db')
	con.execute('''CREATE TABLE Project (Name varchar,id INTEGER PRIMARY KEY AUTOINCREMENT,Description varchar)''')
	con.execute('''CREATE TABLE Log(DOR date,Project_id int,Log varchar, Author_id int,id INTEGER PRIMARY KEY AUTOINCREMENT )''')
	con.execute('''CREATE TABLE Programmer(Name varchar, id INTEGER PRIMARY KEY AUTOINCREMENT, password varchar)''')
	con.commit()
	con.close()

def insertUser(Name,password):
	# This method creates a new user 
	con = sqlite3.connect('WonderOfU.db')
	con.execute("""INSERT INTO Programmer(Name,password) values(:name,:password)""",{"name":Name,"password":password})
	con.commit()
	con.close()	

def AddLog(Log, project, author):
	con = sqlite3.connect('WonderOfU.db')
	today = date.today()

	d1 = today.strftime("%d/%m/%Y")
	con.execute(""" INSERT INTO Log(DOR,Project_id,Log,Author_id) values(:dates,:project,:log,:author)""",{"dates":d1,"project":project,"log":Log,"author":author})
	con.commit()
	con.close()


def AddProject(Name,Description):
	con= sqlite3.connect('WonderOfU.db')
	con.execute(""" insert into Project(Name,Description) values(:name,:description)""",{"name":Name,"description":Description})
	con.commit()
	con.close()

#edit this function to display log for specific project along with the programmer name using join
def ShowLogs(project):
	con= sqlite3.connect('WonderOfU.db')
	data = con.execute('''Select  Log.DOR,Log.Log,Programmer.Name from Log join Project on Log.Project_id=Project.id join Programmer on Log.Author_id=Programmer.id where Project.id=:project  ''',{"project":project} ).fetchall()
	#data = list(data)
	con.commit()
	con.close()
	return data

def ShowProgrammers():
	con= sqlite3.connect('WonderOfU.db')
	data =con.execute('''Select * from Programmer''' ).fetchall()
	#data = list(data)
	con.commit()
	con.close()
	return data

def ShowProjects():
	con= sqlite3.connect('WonderOfU.db')
	data = con.execute('''Select * from Project''' ).fetchall()
	#data = list(data)
	con.commit()
	con.close()
	return data

def DeleteLog(id):
	con = sqlite3.connect('WonderOfU.db')
	con.execute("""delete from Log where  id=:id""",{"id":id})
	con.commit()
	con.close()


def UpdateUser(id,name,password):
	con = sqlite3.connect('WonderOfU.db')
	con.execute("""Update Programmer set Name=:name,password=:password where id=:id""",{"name":name,"password":password,"id":id} )
	con.commit()
	con.close()



def drop():
	con= sqlite3.connect('WonderOfU.db')
	con.execute('''drop table Project''' )
	con.execute('''drop table Programmer''' )
	con.execute('''drop table Log''' )
	con.commit()
	con.close()






