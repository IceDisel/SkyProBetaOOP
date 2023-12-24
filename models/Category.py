from typing import Any


class Category:
    """
    Класс, представляющий категорию продуктов.
    """

    total_categories = 0
    """Общее количество категорий."""

    total_unique_products = 0
    """Общее количество уникальных продуктов."""

    def __init__(self, name_category: str, description_category: str, product: Any = None) -> None:
        """
        Инициализация объекта класса Category.
        :param name_category: Название категории.
        :param description_category: Описание категории.
        """
        self.name_category = name_category
        self.description_category = description_category
        self.__products = []
        self.__products.append(product)
        Category.total_categories += 1

    @property
    def products_list(self) -> list:
        tmp_list = []
        for product in self.__products:
            if product:
                tmp_list.append(f"{product.name_product}, {product.price} руб. Остаток: {product.quantity_in_stock}")
        return tmp_list

    @products_list.setter
    def products_list(self, product) -> None:
        self.__products.append(product)
