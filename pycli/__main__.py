import sys
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="root"
)

from lib.database import Database
from lib.manager import Products, Categories, Cat_products

def main():
    print('welcome to openfoodfacts')
    args = sys.argv[1:]
    argSecond = sys.argv[2:]
    print('count of args : {}'.format(len(args)))

    for arg_second in argSecond:
        val = arg_second

    for arg in args:
        if arg == 'tables':
            Database.create_tables() 
            print('passed argument : {}'.format(arg))
        if arg == 'all_cat':
            Categories.get_categories()
            print('passed argument : {}'.format(arg))
        if arg == 'add_cat':
            Categories.add_categories()
            print('passed argument : {}'.format(arg))
        if arg == 'add_products':
            Products.add_product()
            print('passed argument : {}'.format(arg))
        if arg == 'all_products':
            Products.get_products()
            print('passed argument : {}'.format(arg))
        if arg == 'get_prod':
            Products.get_prod(val)
            print('passed argument : {}'.format(arg))
            print('nutriscore : {} '.format(arg_second))
        if arg == 'search':
            Products.search_by_name(val)
            print('passed argument : {}'.format(arg))
            print('search by name : {} '.format(arg_second))

if __name__ == '__main__':
    main()