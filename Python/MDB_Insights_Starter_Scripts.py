#You need top add an ODBC driver (called 'Python' here) to the ODBC Data Sources (64 Bit) application.  Used SQL Server driver for setup here
#In Anaconda prompt - conda install pyodbc, this is the ODBC connection module which will use the driver to connect to the system

import pyodbc

conn = pyodbc.connect('DSN=Python;SERVER=[ServerName];DATABASE=[DBName];UID=[UserName];PWD=[Password]') #you need to add in the correct details from your password management tool

import pandas as pd

query = "SELECT * FROM DWInternal.DimUser"

user_table = pd.read_sql_query(query, conn)

print(user_table.head())