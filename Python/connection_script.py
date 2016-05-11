#You need top add an ODBC driver (called 'Python' here) to the ODBC Data Sources (64 Bit) application.  Used SQL Server driver for setup here
#In Anaconda prompt - conda install pyodbc, this is the ODBC connection module which will use the driver to connect to the system

import pyodbc

import pandas as pd

data = pd.read_csv("login_stuff.csv") #you need to create your own local csv file of this - remember to gitignore the file to avoid pushing login credentials to github!

server_name = data["server"][0]
database_name = data["database"][0]
username = data["username"][0]
password = data["password"][0]

credentials = "DSN=Python;SERVER={0};DATABASE={1};UID={2};PWD={3}".format(server_name, database_name, username, password)
conn = pyodbc.connect(credentials) #you need to add in the correct details from your password management tool

print(conn)