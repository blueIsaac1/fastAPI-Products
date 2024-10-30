from pydantic import BaseModel
from product import Product
import json

class JsonDB(BaseModel):
    path: str

    def read_json(self):
        f = open(self.path)
        data = json.loads(f.read())
        f.close()
        return data
    
    def insert_json(self, product: Product):
        data = self.read_json()
        data['products'].append(product.dict())
        f = open(self.path, 'w')
        f.write(json.dumps(data))
        f.close()