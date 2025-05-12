from exceptions.custom_exceptions import DuplicateProductIDError
from models.grocery import Grocery

class Inventory:
    def __init__(self):
        self._products = {}

    def add_product(self, product):
        if product.product_id in self._products:
            raise DuplicateProductIDError(f"Product ID {product.product_id} already exists.")
        self._products[product.product_id] = product

    def remove_product(self, product_id):
        if product_id in self._products:
            del self._products[product_id]

    def search_by_name(self, name):
        return [p for p in self._products.values() if name.lower() in p.name.lower()]

    def search_by_type(self, product_type):
        return [p for p in self._products.values() if p.type.lower() == product_type.lower()]

    def list_all_products(self):
        return list(self._products.values())

    def sell_product(self, product_id, quantity):
        if product_id in self._products:
            self._products[product_id].sell(quantity)

    def restock_product(self, product_id, quantity):
        if product_id in self._products:
            self._products[product_id].restock(quantity)

    def total_inventory_value(self):
        return sum(p.get_total_value() for p in self._products.values())

    def remove_expired_products(self):
        to_remove = [pid for pid, prod in self._products.items() if isinstance(prod, Grocery) and prod.is_expired()]
        for pid in to_remove:
            del self._products[pid]
