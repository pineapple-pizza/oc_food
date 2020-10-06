# importing the requests library 
import requests 
  
# api-endpoint 
URL = "https://fr-en.openfoodfacts.org/category/snacks.json"
  
# sending get request and saving the response as response object 
r = requests.get(url = URL) 
  
# extracting data in json format 
data = r.json() 
  
products = data['products']

prod_name = ''
prod_image_url = ''
prod_nutri_score = ''

all_products = []

for i in range(len(products)):
      prod_name = products[i]['product_name']
      prod_image_url = products[i]['image_front_url']
      prod_nutri_score = products[i]['nutriments']['nutrition-score-fr']

      all_products = [products[i]['product_name'], products[i]['image_front_url'], products[i]['nutriments']['nutrition-score-fr']]

      # print(products[i]['product_name'], products[i]['nutriments']['nutrition-score-fr'], products[i]['image_front_url'])


# path param : "https://fr-en.openfoodfacts.org/" + "category" + products[i]['name'] + ".json"