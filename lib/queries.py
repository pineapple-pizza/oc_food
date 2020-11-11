CREATE_DB = "CREATE DATABASE IF NOT EXISTS {} DEFAULT CHARACTER SET 'utf8'"

CREATE_CAT_TABLE = (
    "CREATE TABLE `Categories` ("
    " `cat_id` int(11) NOT NULL AUTO_INCREMENT,"
    " `name` varchar(500) DEFAULT '',"
    "PRIMARY KEY (cat_id)"
    ")"
)

CREATE_PROD_TABLE = (
    "CREATE TABLE `Products` ("
    " `prod_id` int(11) NOT NULL AUTO_INCREMENT,"
    " `name` varchar(500) DEFAULT '',"
    " `url` varchar(500) DEFAULT '',"
    " `nutrition_grade` varchar(500) DEFAULT '',"
    " `substitut` varchar(500) DEFAULT '',"
    "PRIMARY KEY (prod_id)"
    ")"
)

CREATE_CAT_PROD_TABLE = ("CREATE TABLE Cat_products (id INT NOT NULL AUTO_INCREMENT, cat_id INT NOT NULL, prod_id INT NOT NULL, FOREIGN KEY(cat_id) REFERENCES Categories(cat_id) ON DELETE CASCADE, FOREIGN KEY(prod_id) REFERENCES Products(prod_id) ON DELETE CASCADE, PRIMARY KEY (id));")

QUERY_ADD_CAT = "INSERT INTO Categories(name) VALUES(%s)"

QUERY_ADD_CAT_PROD = ("INSERT INTO Cat_products(cat_id, prod_id) VALUES(%s,%s)")

QUERY_GET_CAT_PRODS = "SELECT * FROM Cat_products"

QUERY_ADD_PROD = "INSERT INTO Products(name, url, nutrition_grade) VALUES (%s, %s, %s)"

QUERY_GET_PRODS = "SELECT * FROM Products"

QUERY_GET_PROD_NUTRI = "SELECT * FROM Products WHERE nutrition_grade="

QUERY_SEARCH_NAME = "SELECT * FROM Products WHERE name LIKE %s"

QUERY_COMPARE_SCORE = "SELECT * FROM Products WHERE nutrition_grade<="

QUERY_UPDATE_PROD = "UPDATE Products SET substitut = %s WHERE prod_id = %s"

QUERY_GET_CATS = "SELECT * FROM Categories"
