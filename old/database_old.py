import mysql.connector

config = {
  'host' : "localhost",
  'user' : "root",
  'password' : "root",
  'database' : "testdb"
}

mydb = mysql.connector.connect(**config)

mycursor = mydb.cursor()

DB_NAME = 'testdb'

def create_database():
    mycursor.execute(
        "CREATE DATABASE IF NOT EXISTS {} DEFAULT CHARACTER SET 'utf8'".format(DB_NAME))
    print("Database {} created!".format(DB_NAME))