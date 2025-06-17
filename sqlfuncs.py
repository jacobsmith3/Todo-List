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
        mycursor.execute("CREATE TABLE Reminders (dt DATE, tm TIME, What VARCHAR(255), `repeat` CHAR(1))")

# gets the days todos 
def gettoday():
    # get todays date and then format it correctly
    today = date.today()
    formatted_date = today.strftime("%Y-%m-%d")
    print(today.strftime('%A'))
    
    # make the call to the sql server and database
    mycursor = mydb.cursor()
    mydb.database = "todo"
    mycursor.execute("SELECT * FROM Reminders WHERE dt = %s",(formatted_date,))
    for x in mycursor:
        extractinfo(x)

# adds thinsg to the Table so i can then i can test the gettoday function
# and so the user can add todos they want to use
def maketodo(val):
    mycursor = mydb.cursor()
    mydb.database = "todo"
    action = "INSERT INTO reminders VALUES(%s,%s, %s, %s)"
    mycursor.execute(action, val)
    mydb.commit()
    print("Added new todo!")

## clears a tabele so i can test features through the debug tool
def cleartable():
    mycursor = mydb.cursor()
    mydb.database = "todo"
    mycursor.execute("TRUNCATE TABLE reminders")

## extracts info from data quires and gives them to the console in a easier to 
##understand way
def extractinfo(data):
    date=str(data[1])
    test=date.split(':')
    test[0]=str(int(test[0]))
    print(str(data[0])+" --- "+test[0]+":"+test[1]+" --- "+data[2])
