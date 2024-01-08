from models.Product import Product


class LawnGrass(Product):
    """
    Класс, представляющий траву.
    """
    def __init__(self, name_product: str, description_product: str, price: float, quantity_in_stock: int,
                 manufacturer_country: str, germination_period: str, color: str):
        """
        Инициализация объекта класса LawnGrass.
        :param name_product: Название товара или тип травы.
        :param description_product: Описание товара.
        :param price: Цена товара.
        :param quantity_in_stock: Количество товара на складе.
        :param manufacturer_country: Страна-производитель.
        :param germination_period: Срок прорастания.
        :param color: Цвет товара.
        """
        super().__init__(name_product, description_product, price, quantity_in_stock)

        self.manufacturer_country = manufacturer_country
        self.germination_period = germination_period
        self.color = color
