import mysql.connector

from lib.queries import CREATE_DB, CREATE_CAT_TABLE, CREATE_PROD_TABLE, CREATE_CAT_PROD_TABLE

config = {
  'host' : "localhost",
  'user' : "root",
  'password' : "root",
  'database' : "openfoodfacts"
}

mydb = mysql.connector.connect(**config)

mycursor = mydb.cursor()

TABLES = {
  'Categories' : CREATE_CAT_TABLE,
  'Products' : CREATE_PROD_TABLE,
  'Cat_products' : CREATE_CAT_PROD_TABLE
}

DB_NAME = 'openfoodfacts'

class Database:
    """op project Openfoodfacts database"""
    def __init__(self, db_name):
        self.db_name = name

    def create_database():
        mycursor.execute(CREATE_DB.format(DB_NAME))
        print("Database {} created!".format(DB_NAME))

    def create_tables():
        mycursor.execute("USE {}".format(DB_NAME))

        for table_name in TABLES:
            table_description = TABLES[table_name]
            try:
                print("Creating table ({}) ".format(table_name), end="")
                mycursor.execute(table_description)
            except mysql.connector.Error as err:
                    print(err.msg)
