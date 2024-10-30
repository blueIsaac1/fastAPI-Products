from product import Product
import json

def generate_products():
#   list_products = []
#   for x in range(1, 11):
#     p = Product(name = f"Product: {x}", price = 5.0 * x)
#     list_products.append(p)
#   return list_products
    f = open("./data/products.json")
    data = json.loads(f.read())
    f.close()
    return data