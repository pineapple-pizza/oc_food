import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="root"
)

from lib.database import *
from lib.manager import Products, Categories, Cat_products

# Database.create_tables()

Products.add_product()
# Categories.add_categories()
# Cat_products.add_cat_prod()
