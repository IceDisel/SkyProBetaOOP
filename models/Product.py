from models.Category import Category


class Product:
    """
    Класс, представляющий продукт.
    """
    name_product: str
    """Название продукта."""

    description_product: str
    """Описание продукта."""

    price: float
    """Цена продукта."""

    quantity_in_stock: int
    """Количество продукта на складе."""

    def __init__(self, name_product: str, description_product: str, price: float, quantity_in_stock: int) -> None:
        """
        Инициализация объекта класса Product.
        :param name_product: Название продукта.
        :param description_product: Описание продукта.
        :param price: Цена продукта.
        :param quantity_in_stock: Количество продукта на складе.
        """
        self.name_product = name_product
        self.description_product = description_product
        self.price = price
        self.quantity_in_stock = quantity_in_stock
        Category.total_unique_products += 1
