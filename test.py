products = [
    {"id": 1, "name": "Boots", "price": 10.0, "category": "Footwear"},
    {"id": 2, "name": "Cap", "price": 20.0, "category": "Clothing"},
    {"id": 3, "name": "Shirt", "price": 30.0, "category": "Clothing"},
    {"id": 4, "name": "Jacket", "price": 40.0, "category": "Clothing"},
    {"id": 5, "name": "Socks", "price": 50.0, "category": "Footwear"},
    {"id": 6, "name": "Sweater", "price": 60.0, "category": "Clothing"},
    {"id": 7, "name": "Gloves", "price": 70.0, "category": "Clothing"},
    {"id": 8, "name": "Scarf", "price": 80.0, "category": "Clothing"},
    {"id": 9, "name": "Belt", "price": 90.0, "category": "Clothing"},
    {"id": 10, "name": "Shoes", "price": 100.0, "category": "Footwear"},
    {"id": 11, "name": "Milk", "price": 10.0, "category": "Grocery"},
    {"id": 12, "name": "Bread", "price": 20.0, "category": "Grocery"},
    {"id": 13, "name": "Eggs", "price": 30.0, "category": "Grocery"},
    {"id": 14, "name": "Butter", "price": 40.0, "category": "Grocery"},
    
    ]

import json

# export the products list as a json file
with open('products.json', 'w') as outfile:
    json.dump(products, outfile)