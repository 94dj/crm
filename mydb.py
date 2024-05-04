import mysql.connector

database = mysql.connector.Connect(
    host = 'localhost',
    user = 'root',
    passwd = 'california@43'
)

curorObject = database.cursor()

curorObject.execute("CREATE DATABASE CRMDB")

print("all done!")