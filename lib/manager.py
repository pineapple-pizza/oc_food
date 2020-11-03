from lib.queries import CREATE_CAT_TABLE, CREATE_PROD_TABLE, CREATE_CAT_PROD_TABLE, cat_products, QUERY_ADD_PROD, QUERY_ADD_CAT, QUERY_ADD_CAT_PROD, QUERY_GET_PRODS, QUERY_GET_PROD_NUTRI, QUERY_SEARCH_NAME, QUERY_GET_CATS, QUERY_COMPARE_SCORE, QUERY_UPDATE_PROD
from lib.database import mycursor, mydb, DB_NAME
import requests
from tabulate import tabulate

products_URL = "https://fr-en.openfoodfacts.org/category/oat-flakes.json"
categories_URL = "https://world.openfoodfacts.org/categories.json"

class Products:
    """op project Openfoodfacts products"""
    def __init__(self, prod_id, name, url, nutrition_grade):
        self.prod_id = prod_id
        self.name = name
        self.url = url
        self.nutriscore_score = nutrition_grade

    def add_product(products_URL):
        """add products with value (category name from openfoodfacts)"""
        results = requests.get("https://fr-en.openfoodfacts.org/category/" + products_URL + ".json") 
        data = results.json() 
        products = data['products']
        mycursor.execute("USE {}".format(DB_NAME))
        
        for i in range(len(products)):
            if products[i]['nutriscore_score'] and products[i]['image_front_url']:
                all_products = [(products[i]['product_name'], products[i]['image_front_url'], products[i]['nutriscore_score'])]
                mycursor.executemany(QUERY_ADD_PROD, all_products)
        mydb.commit()
        print(mycursor.rowcount, "records inserted")

    def get_products():
        """get request all products"""
        mycursor.execute("USE {}".format(DB_NAME))
        mycursor.execute(QUERY_GET_PRODS)
        myresult = mycursor.fetchall()

        print(tabulate(myresult, headers = mycursor.column_names, tablefmt='fancy_grid'))

    def get_prod(nutri):
        """get product with value (nutriscore)"""
        val = int(nutri)
        mycursor.execute("USE {}".format(DB_NAME))
        mycursor.execute(QUERY_GET_PROD_NUTRI+ str(nutri))
        myresult = mycursor.fetchall()

        print(tabulate(myresult, headers = mycursor.column_names, tablefmt='fancy_grid'))

    def search_by_name(value):
        """search product with value (name)"""
        val = str(value)
        mycursor.execute("USE {}".format(DB_NAME))
        mycursor.execute(QUERY_SEARCH_NAME, ("%" + val + "%",))
        myresult = mycursor.fetchall()

        print(tabulate(myresult, headers = mycursor.column_names, tablefmt='fancy_grid'))

    def compare_by_score(nutri):
        """compare products with value (nutriscore superior or egal value)"""
        val = int(nutri)
        mycursor.execute("USE {}".format(DB_NAME))
        mycursor.execute(QUERY_COMPARE_SCORE+ str(nutri))
        myresult = mycursor.fetchall()

        print(tabulate(myresult, headers = mycursor.column_names, tablefmt='fancy_grid'))

    def update_sub(first_id, second_id):
        """update substitut column with values (id 1, id 2)"""
        params = (int(first_id), int(second_id))

        mycursor.execute("USE {}".format(DB_NAME))
        mycursor.execute(QUERY_UPDATE_PROD, params)
        mydb.commit()

        print(mycursor.rowcount, "record(s) affected")

class Categories:
    """op project Openfoodfacts categories"""
    def __init__(self, cat_id, name):
        self.cat_id = cat_id
        self.name = name

    def add_categories(value):
        """add category with value"""
        val = str(value)
        mycursor.execute("USE {}".format(DB_NAME))
        mycursor.execute(QUERY_ADD_CAT, (val, ))
        mydb.commit()

        print(mycursor.rowcount, "records inserted")

    def get_categories():
        """get request all categories"""
        mycursor.execute("USE {}".format(DB_NAME))
        mycursor.execute(QUERY_GET_CATS)
        myresult = mycursor.fetchall()

        print(tabulate(myresult, headers = mycursor.column_names, tablefmt='fancy_grid'))

class Cat_products:
    """op project Openfoodfacts categories"""
    def __init__(self, cat_id, prod_id):
        self.cat_id = cat_id
        self.prod_id = prod_id

    def add_cat_prod():
        mycursor.execute("USE {}".format(DB_NAME))
        mycursor.executemany(QUERY_ADD_CAT_PROD, cat_products)
        mydb.commit()

        print(mycursor.rowcount, "records inserted")