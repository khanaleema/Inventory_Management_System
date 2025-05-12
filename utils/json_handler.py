import json
from models.electronics import Electronics
from models.grocery import Grocery
from models.clothing import Clothing
from exceptions.custom_exceptions import InvalidProductDataError

def save_to_file(inventory, filename):
    data = []
    for p in inventory.list_all_products():
        item = p.__dict__.copy()
        item['type'] = p.type
        data.append(item)

    with open(filename, 'w') as f:
        json.dump(data, f, indent=4)

def load_from_file(inventory, filename):
    with open(filename, 'r') as f:
        data = json.load(f)

    for item in data:
        try:
            type_ = item.pop('type')
            if type_ == 'Electronics':
                product = Electronics(**item)
            elif type_ == 'Grocery':
                product = Grocery(**item)
            elif type_ == 'Clothing':
                product = Clothing(**item)
            else:
                raise InvalidProductDataError(f"Unknown type: {type_}")
            inventory.add_product(product)
        except Exception as e:
            raise InvalidProductDataError(str(e))
