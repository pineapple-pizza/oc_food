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

TABLES = {}

TABLES['Categories'] = (
    "CREATE TABLE `Categories` ("
    " `cat_id` int(11) NOT NULL AUTO_INCREMENT,"
    " `name` varchar(500) NOT NULL,"
    " `url` varchar(500) NOT NULL,"
    "PRIMARY KEY (cat_id)"
    ")"
)

categories = [("drinks", "url_drinks.com"),
            ("cornflakes", "url_cornflakes.com"),
            ("dog food", "url_dog_food.com")]

cat_products = [(1, 4),
            (1, 5),
            (1, 6)]

class Categories:
    """op project Openfoodfacts categories"""
    def __init__(self, cat_id, name, url):
        self.cat_id = cat_id
        self.name = name
        self.url = url

    def create_table():
        mycursor.execute("USE {}".format(DB_NAME))

        for table_name in TABLES:
            table_description = TABLES[table_name]
            try:
                print("Creating table ({}) ".format(table_name), end="")
                mycursor.execute(table_description)
            except mysql.connector.Error as err:
                    print(err.msg)

    def add_categories():
        query = "INSERT INTO Categories(name, url) VALUES (%s,%s)"
        mycursor.executemany(query, categories)
        mydb.commit()

        print(mycursor.rowcount, "records inserted")

    def add_cat_prod():
        query = "INSERT INTO Cat_products(cat_id, prod_id) VALUES (%s,%s)"
        mycursor.executemany(query, cat_products)
        mydb.commit()

        print(mycursor.rowcount, "records inserted")