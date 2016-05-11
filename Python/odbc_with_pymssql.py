#You need top add an ODBC driver (called 'Python' here) to the ODBC Data Sources (64 Bit) application.  Used SQL Server driver for setup here
#In Anaconda prompt - pip install pyodbc, this is the ODBC connection module which will use the driver to connect to the system
#In Anaconda prompt - pip install pymssql==2.1.1, This module will enable you to write SQL in-line with Python - v.2.1.1 still works at time of writing where 2.1.2 has issues on import.

import pyodbc

conn = pyodbc.connect('DSN=Python;SERVER={Servername};DATABASE={Databasename};UID={username};PWD={password}') #you need to add in the correct details from your password management tool

#At this point you should be connected to the database.  Now we need to bring in pymssql for querying the data

print(conn)

import pymssql

cursor = conn.cursor()

results = cursor.execute('SELECT TOP 10 dimUserId FROM DWInternal.DimUser') #Fill in the string to complete the query and we're good to go

results_list = results.fetchall() #executing the select statement does not bring back the results - fetchall() brings these back which we can then print

print(results_list)