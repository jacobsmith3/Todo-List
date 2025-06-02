import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="Wyatt323232!",
  database="TODO"
)

# this is a check to make sure that the database exists and if not it gets created with the tables
def checkdatabase():
    mycursor = mydb.cursor()

    mycursor.execute("SHOW DATABASES")

    #checks if database is there 
    if("Todo" not in mycursor):
        mycursor.execute("CREATE DATABASE mydatabase")
        mycursor.execute("CREATE TABLE Reminders (When DATETIME,What VARCHAR(255), repeat BIT)")


