from lib.queries import products, categories, cat_products, QUERY_ADD_PROD, QUERY_ADD_CAT, QUERY_ADD_CAT_PROD
from lib.database import mycursor, mydb
from test_get import *

PRODUCTS = [(prod_name, prod_image_url, prod_nutri_score)]

class Products:
    """op project Openfoodfacts products"""
    def __init__(self, prod_id, name, url, nutrition_grade):
        self.prod_id = prod_id
        self.name = name
        self.url = url
        self.nutrition_grade = nutrition_grade

    def add_product():
        mycursor.executemany(QUERY_ADD_PROD, PRODUCTS)
        mydb.commit()

        print(mycursor.rowcount, "records inserted")

class Categories:
    """op project Openfoodfacts categories"""
    def __init__(self, cat_id, name, url):
        self.cat_id = cat_id
        self.name = name
        self.url = url

    def add_categories():
        mycursor.executemany(QUERY_ADD_CAT, categories)
        mydb.commit()

        print(mycursor.rowcount, "records inserted")

class Cat_products:
    """op project Openfoodfacts categories"""
    def __init__(self, cat_id, prod_id):
        self.cat_id = cat_id
        self.prod_id = prod_id

    def add_cat_prod():
        mycursor.executemany(QUERY_ADD_CAT_PROD, cat_products)
        mydb.commit()

        print(mycursor.rowcount, "records inserted")