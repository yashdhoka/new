import mysql.connector
import yaml

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="Master@12345",
  database="eficaz"
)

mycursor = mydb.cursor() 


query = "CREATE TABLE Persons (PersonID int, LastName varchar(255),FirstName varchar(255),Address varchar(255), City varchar(255));"

mycursor.execute(query)
mydb.commit()

print("",mycursor.rowcount, "record inserted.")

mycursor.close()
