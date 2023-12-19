from models.Category import Category


class Product:
    name_product: str
    description_product: str
    price: float
    quantity_in_stock: str

    def __init__(self, name_product, description_product, price, quantity_in_stock):
        self.name_product = name_product
        self.description_product = description_product
        self.price = price
        self.quantity_in_stock = quantity_in_stock
        Category.total_unique_products += 1
