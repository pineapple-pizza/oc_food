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

TABLES['Products'] = (
    "CREATE TABLE `Products` ("
    " `prod_id` int(11) NOT NULL AUTO_INCREMENT,"
    " `name` varchar(500) NOT NULL,"
    " `url` varchar(500) NOT NULL,"
    " `nutrition_grade` char(1) NULL,"
    "PRIMARY KEY (prod_id)"
    ")"
)

products = [("coffee", "url_coffee.com", 1),
              ("tea", "url_tea.com", 2),
              ("milk", "url_milk.com", 1)]

class Products:
    """op project Openfoodfacts products"""
    def __init__(self, prod_id, name, url, nutrition_grade):
        self.prod_id = prod_id
        self.name = name
        self.url = url
        self.nutrition_grade = nutrition_grade

    def create_table():
        mycursor.execute("USE {}".format(DB_NAME))

        for table_name in TABLES:
            table_description = TABLES[table_name]
            try:
                print("Creating table ({}) ".format(table_name), end="")
                mycursor.execute(table_description)
            except mysql.connector.Error as err:
                    print(err.msg)

    def add_product():
        # sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
        # val = ("John", "Highway 21")

        # mycursor.execute(sql, val)

        # mydb.commit()

        # print(mycursor.rowcount, "record inserted.")

        query = "INSERT INTO Products(name, url, nutrition_grade) VALUES (%s,%s,%s)"
        mycursor.executemany(query, products)
        mydb.commit()

        print(mycursor.rowcount, "records inserted")

        # for x, product in enumerate(products):
        #     # mycursor.execute("INSERT INTO Products (name, url, nutrition_grade) VALUES (%s, %s, %s)", product)
        #     last_id = mycursor.lastrowid
        #     mycursor.execute(query, (last_id,) + products[x])
        #     print("Products {} inserted!".format(DB_NAME))
        
        # mycursor.execute("SELECT * FROM Products")
        # for x in mycursor:
        #     print(x)


        # try:
        #     # Executing the SQL command
        #     mycursor.execute(query, products)
            
        #     # Commit your changes in the database
        #     mydb.commit()

        # except:
        #     # Rolling back in case of error
        #     mydb.rollback()

        # print("Data inserted")

        # # Closing the connection
        # mydb.close()