CREATE_DB = ("CREATE DATABASE IF NOT EXISTS {} DEFAULT CHARACTER SET 'utf8'")

CREATE_CAT_TABLE = (
    "CREATE TABLE `Categories` ("
    " `cat_id` int(11) NOT NULL AUTO_INCREMENT,"
    " `name` varchar(500) NOT NULL,"
    " `url` varchar(500) NOT NULL,"
    "PRIMARY KEY (cat_id)"
    ")"
)

CREATE_PROD_TABLE = (
    "CREATE TABLE `Products` ("
    " `prod_id` int(11) NOT NULL AUTO_INCREMENT,"
    " `name` varchar(500) NOT NULL,"
    " `url` varchar(500) NOT NULL,"
    " `nutrition_grade` varchar(500) NULL,"
    "PRIMARY KEY (prod_id)"
    ")"
)

CREATE_CAT_PROD_TABLE = ("CREATE TABLE Cat_products (id INT NOT NULL AUTO_INCREMENT, cat_id INT NOT NULL, prod_id INT NOT NULL, FOREIGN KEY(cat_id) REFERENCES Categories(cat_id) ON DELETE CASCADE, FOREIGN KEY(prod_id) REFERENCES Products(prod_id) ON DELETE CASCADE, PRIMARY KEY (id));")

QUERY_ADD_CAT = ("INSERT INTO Categories(name, url) VALUES (%s,%s)")

QUERY_ADD_CAT_PROD = ("INSERT INTO Cat_products(cat_id, prod_id) VALUES (%s,%s)")

QUERY_ADD_PROD = ("INSERT INTO Products(name, url, nutrition_grade) VALUES (%s,%s,%s)")

products = [("coffee", "url_coffee.com", 1),
            ("tea", "url_tea.com", 2),
            ("milk", "url_milk.com", 1)]

categories = [("drinks", "url_drinks.com"),
            ("cornflakes", "url_cornflakes.com"),
            ("dog food", "url_dog_food.com")]

cat_products = [(1, 1),
                (1, 2),
                (1, 3)]