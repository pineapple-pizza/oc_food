import sys

from lib.database import Database
from lib.manager import Products, Categories, Cat_products

def main():
    print('welcome to openfoodfacts')
    args = sys.argv[1:]
    argSecond = sys.argv[2:]
    argThird = sys.argv[3:]
    print('count of args : {}'.format(len(args)))

    for arg_second in argSecond:
        val = arg_second

    for arg_third in argThird:
        val_third = arg_third

    for arg in args:
        """creating the database"""
        if arg == 'db':
            Database.create_database() 
            print('passed argument : {}'.format(arg))

        """creating the tables"""
        if arg == 'tables':
            Database.create_tables() 
            print('passed argument : {}'.format(arg))

        """get request all categories"""
        if arg == 'all_cat':
            Categories.get_categories()
            print('passed argument : {}'.format(arg))

        """add category with value"""
        if arg == 'add_cat':
            Categories.add_categories(val)
            print('passed argument : {}'.format(arg_second))

        """add products with value (category name from openfoodfacts)"""
        if arg == 'add_products':
            Products.add_product(val)
            print('passed argument : {}'.format(arg_second))

        """get request all products"""
        if arg == 'all_products':
            Products.get_products()
            print('passed argument : {}'.format(arg))

        """get product with value (nutriscore)"""
        if arg == 'get_prod':
            Products.get_prod(val)
            print('passed argument : {}'.format(arg))
            print('nutriscore : {} '.format(arg_second))

        """search product with value (name)"""
        if arg == 'search':
            Products.search_by_name(val)
            print('passed argument : {}'.format(arg))
            print('search by name : {} '.format(arg_second))

        """compare products with value (nutriscore superior or egal value)"""
        if arg == 'compare':
            Products.compare_by_score(val)
            print('passed argument : {}'.format(arg))
            print('nutriscore : {} '.format(arg_second))

        """update substitut column with values (id 1, id 2)"""
        if arg == 'update':
            Products.update_sub(val, val_third)
            print('passed argument : {}'.format(arg))
            print('first id : {} '.format(arg_second))
            print('second id : {} '.format(arg_third))

if __name__ == '__main__':
    main()