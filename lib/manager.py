from lib.queries import cat_products, QUERY_ADD_PROD, QUERY_ADD_CAT, QUERY_ADD_CAT_PROD
from lib.database import mycursor, mydb
import requests

products_URL = "https://fr-en.openfoodfacts.org/category/oat-flakes.json"
categories_URL = "https://world.openfoodfacts.org/categories.json"

class Products:
    """op project Openfoodfacts products"""
    def __init__(self, prod_id, name, url, nutrition_grade):
        self.prod_id = prod_id
        self.name = name
        self.url = url
        self.nutriscore_score = nutrition_grade

    def add_product():
        results = requests.get(url = products_URL) 
        data = results.json() 
        products = data['products']

        for i in range(len(products)):
            if products[i]['nutriscore_score'] and products[i]['image_front_url']:
                all_products = [(products[i]['product_name'], products[i]['image_front_url'], products[i]['nutriscore_score'])]
                mycursor.executemany(QUERY_ADD_PROD, all_products)
        mydb.commit()
        print(mycursor.rowcount, "records inserted")

    def get_products():
        mycursor.execute("SELECT * FROM Products")
        myresult = mycursor.fetchall()

        for x in myresult:
            print(x)

    def get_prod(nutri):
        val = int(nutri)
        mycursor.execute("SELECT * FROM Products WHERE nutrition_grade="+ str(nutri))
        myresult = mycursor.fetchall()

        for x in myresult:
            print(x)

    def search_by_name(value):
        val = str(value)
        mycursor.execute("SELECT * FROM Products WHERE name LIKE %s", ("%" + val + "%",))
        myresult = mycursor.fetchall()

        for x in myresult:
            print(x)

class Categories:
    """op project Openfoodfacts categories"""
    def __init__(self, cat_id, name):
        self.cat_id = cat_id
        self.name = name

    def add_categories():
        # cat_test = [("oat-flakes"), ("wheat-breads")]

        # cat_results = requests.get(url = categories_URL)
        # data = cat_results.json()
        # categories = data['tags']

        # for i in range(len(categories)):
        #     if categories[i]['name'] == "oat-flakes":
        #         cat_test = [(categories[i]['name'])]

        #         mycursor.executemany(QUERY_ADD_CAT, cat_test)
        #         print(cat_test)
        oat = ('oat-flakes')
        bread = ('wheat-breads')
        mycursor.execute(QUERY_ADD_CAT, (bread, ))
        mydb.commit()

        print(mycursor.rowcount, "records inserted")

    def get_categories():
        mycursor.execute("SELECT * FROM Categories")
        myresult = mycursor.fetchall()

        for x in myresult:
            print(x)

class Cat_products:
    """op project Openfoodfacts categories"""
    def __init__(self, cat_id, prod_id):
        self.cat_id = cat_id
        self.prod_id = prod_id

    def add_cat_prod():
        mycursor.executemany(QUERY_ADD_CAT_PROD, cat_products)
        mydb.commit()

        print(mycursor.rowcount, "records inserted")