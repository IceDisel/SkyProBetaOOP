from models.Product import Product


class Smartphone(Product):
    """
    Класс, представляющий смартфон.
    """
    def __init__(self, name_product: str, description_product: str, price: float, quantity_in_stock: int,
                 performance: str, model: str, memory: str, color: str):
        """
        Инициализация объекта класса Smartphone.
        :param name_product: Название смартфона.
        :param description_product: Описание смартфона.
        :param price: Цена смартфона.
        :param quantity_in_stock: Количество смартфона на складе.
        :param performance: Производительность смартфона.
        :param model: Модель смартфона.
        :param memory: Количество встроенной памяти смартфона.
        :param color: Цвет смартфона.
        """

        super().__init__(name_product, description_product, price, quantity_in_stock)

        self.performance = performance
        self.model = model
        self.memory = memory
        self.color = color
