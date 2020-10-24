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
    "PRIMARY KEY (prod_id)"
    ")"
)

CREATE_CAT_PROD_TABLE = ("CREATE TABLE Cat_products (id INT NOT NULL AUTO_INCREMENT, cat_id INT NOT NULL, prod_id INT NOT NULL, FOREIGN KEY(cat_id) REFERENCES Categories(cat_id) ON DELETE CASCADE, FOREIGN KEY(prod_id) REFERENCES Products(prod_id) ON DELETE CASCADE, PRIMARY KEY (id));")

QUERY_ADD_CAT = "INSERT INTO Categories(name) VALUES(%s)"

QUERY_ADD_CAT_PROD = ("INSERT INTO Cat_products(cat_id, prod_id) VALUES(%s,%s)")

QUERY_ADD_PROD = "INSERT INTO Products(name, url, nutrition_grade) VALUES (%s, %s, %s)"

cat_products = [(2, 1),
                (2, 2),
                (2, 3),
                (2, 4),
                (2, 5),
                (2, 6),
                (2, 7),
                (2, 8),
                (2, 9),
                (2, 10),
                (2, 11),
                (2, 12),
                (2, 13),
                (2, 14),
                (2, 15),
                (2, 16),
                (2, 17),
                (2, 18),
                (1, 19),
                (1, 20),
                (1, 21),
                (1, 22),
                (1, 23),
                (1, 24),
                (1, 25),
                (1, 26),
                (1, 27),
                (1, 28),
                (1, 29),
                (1, 30),
                (1, 31),
                (1, 32),
                (1, 33),]