from models.base_product import Product

class Clothing(Product):
    def __init__(self, product_id, name, price, quantity_in_stock, size, material):
        super().__init__(product_id, name, price, quantity_in_stock)
        self.size = size
        self.material = material

    def __str__(self):
        return f"[Clothing] {self._name} | Size: {self.size} | Material: {self.material} | Stock: {self._quantity_in_stock} | Price: {self._price}"
