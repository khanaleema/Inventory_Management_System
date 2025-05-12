from models.base_product import Product
from datetime import datetime

class Grocery(Product):
    def __init__(self, product_id, name, price, quantity_in_stock, expiry_date):
        super().__init__(product_id, name, price, quantity_in_stock)
        self.expiry_date = expiry_date  # in 'YYYY-MM-DD' format

    def is_expired(self):
        return datetime.strptime(self.expiry_date, "%Y-%m-%d") < datetime.now()

    def __str__(self):
        return f"[Grocery] {self._name} | Expiry: {self.expiry_date} | Stock: {self._quantity_in_stock} | Price: {self._price}"
