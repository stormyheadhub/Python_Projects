
import sqlite3
connection = sqlite3.connect("C:/Users/conta/OneDrive/Documents/GitHub/Python_Projects/sqlite_project.py")

c = connection.cursor()
c.execute("CREATE TABLE People(FirstName TEXT, LastName TEXT, Age INT)")




