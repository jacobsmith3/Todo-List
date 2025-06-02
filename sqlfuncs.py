import mysql.connector
from datetime import date

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
        mycursor.execute("CREATE DATABASE Todo")
        mycursor.execute("CREATE TABLE Reminders (dt DATE,tm TIME,What VARCHAR(255), repeat BIT)")

# gets the days todos 
def gettoday():
    # get todays date and then format it correctly
    today = date.today()
    formatted_date = today.strftime("%Y-%m-%d")
    
    # make the call to the sql server and database
    mycursor = mydb.cursor()
    mycursor.execute("SELECT * FROM Reminders WHERE dt = "+ formatted_date)
    for x in mycursor:
        print(x)