import mysql.connector
from datetime import date

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="Wyatt323232!"
)

# this is a check to make sure that the database exists and if not it gets created with the tables
def checkdatabase():
    mycursor = mydb.cursor()

    mycursor.execute("SHOW DATABASES LIKE 'todo';")
    databases = mycursor.fetchall()

    #checks if database is there 
    if not databases:
        mycursor.execute("CREATE DATABASE todo")
        mydb.database = "todo"  # select the new DB before creating table
        mycursor.execute("CREATE TABLE Reminders (dt DATE, tm TIME, What VARCHAR(255), `repeat` BIT)")

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

# adds thinsg to the Table so i can then i can test the gettoday function
# and so the user can add todos they want to use
def maketodo(val):
    mycursor = mydb.cursor()
    mydb.database = "todo"
    action = "INSERT INTO TODO VALUES(%s,%s, %s, %s)"
    mycursor.execute(action, val)
    mycursor.commit()
    print("Added new todo")

