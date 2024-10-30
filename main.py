from fastapi import FastAPI
# from indb import generate_products
from json_indb import JsonDB
from product import Product

app = FastAPI()

productDB = JsonDB(path='./data/products.json')

@app.get('/products')
def get_products():
    products = productDB.read_json()
    return { 'products': products }

@app.post('/products')
def create_products(product: Product):

    productDB.insert_json(product)

    return{'status': 'sucess'}