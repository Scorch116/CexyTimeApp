import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="admin",
    passwd="admin",
    database ="cexydatabase"
)

mycursor =db.cursor()

mycursor.execute("CREATE TABLE Person (empno varchar(5), name varchar(20), stafflvl varchar(2), gender varchar(10), address varchar(50));")