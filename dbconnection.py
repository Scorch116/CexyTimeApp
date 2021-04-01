import mysql.connector



mydb = mysql.connector.connect(
    host="localhost",
    user="admin",
    passwd="admin",
    database ="cexydatabase"
)

mycursor =mydb.cursor()

#mycursor.execute("CREATE TABLE Person (empno varchar(5) PRIMARY KEY, name varchar(20), stafflvl varchar(2), gender varchar(10), address varchar(50));")
#print("Table Created")
#mycursor.execute("DROP TABLE Person;")
#print("table dropped")



#mycursor.execute("INSERT INTO Person (empno, name,stafflvl, gender,address) VALUES ('h123', 'Ed McGrath','3','Male','7 Roger casement park')")
#db.commit()#will commit changes made to database

#mycursor.execute("SELECT * FROM Person;")

#for x in mycursor:
 #   print(x)

#def insertD():
   # mycursor.execute("INSERT INTO Person (empn, name,stafflvl, gender,address) VALUES ('%s','%s','%s','%s','%s')")
    #db.commit()#will commit changes made to database



