from lib.database import *

create_database()

products = [("coffee_cat", "coffee", "url_coffee.com"),
              ("tea_cat", "tea", "url_tea.com"),
              ("milk_cat", "milk", "url_milk.com")]

categories = [("espresso", "url_espresso.com", "nut_grade_espresso", "coffee"),
            ("green tea", "url_green_tea.com", "nut_grade_greentea", "tea"),
            ("almond milk", "url_almond_milk.com", "nut_grade_almondmilk", "milk")]

Q1 = "CREATE TABLE Products (id int PRIMARY KEY AUTO_INCREMENT, name varchar(500), url varchar(500), nutrition_grade varchar(500), category VARCHAR(500))"

Q2 = "CREATE TABLE Categories (catId int PRIMARY KEY, FOREIGN KEY(catId) REFERENCES Products(id), prod_cat VARCHAR(500), name varchar(500), url varchar(500))"

Q3 = "INSERT INTO Products (prod_cat, name, url) VALUES (%s, %s, %s)"
Q4 = "INSERT INTO Categories (productId, name, url, nutrition_grade, category) VALUES (%s, %s, %s, %s, %s)"

for x, product in enumerate(products):
  mycursor.execute(Q3, product)
  last_id = mycursor.lastrowid
  mycursor.execute(Q4, (last_id,) + categories[x])

mydb.commit()

mycursor.execute("SELECT * FROM Categories")
for x in mycursor:
  print(x)

mycursor.execute("SELECT * FROM Products")
for x in mycursor:
  print(x)

# mycursor.execute("SHOW TABLES")

# for tb in mycursor:
#   print(tb)