from models.base_product import Product

class Electronics(Product):
    def __init__(self, product_id, name, price, quantity_in_stock, warranty_years, brand):
        super().__init__(product_id, name, price, quantity_in_stock)
        self.warranty_years = warranty_years
        self.brand = brand

    def __str__(self):
        return f"[Electronics] {self._name} | Brand: {self.brand} | Warranty: {self.warranty_years} years | Stock: {self._quantity_in_stock} | Price: {self._price}"
