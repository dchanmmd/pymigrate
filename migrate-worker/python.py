import json
from os import path

base_path = path.abspath(path.dirname(__file__))

product_path = path.join(base_path, 'product-product.json')

with open(product_path, 'r', encoding='utf-8') as file:
    product = json.load(file)
    print('class Odoo_ProductProduct(BaseModel):')
    for name, info in product.items():
        t = info['type'].strip().lower()
        pytype = (
            'int' if t == 'integer' else
            'float' if t == 'float' or t == 'monetary' else
            'bool' if t == 'boolean' else 
            'str' if t == 'char' or t == 'text' or t == 'html' else 
            'datetime' if t.find('date') >= 0
            else f"Any # {t}"
        )
        print(f"    {name}: {pytype}")