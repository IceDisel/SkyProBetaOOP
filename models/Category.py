from typing import Any, Iterator


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

    def __str__(self) -> str:
        """
        Строковое отображение количества всех продуктов в категории товаров
        :return:
        """
        return f"{self.name_category}, количество продуктов: {self.__len__()} шт."

    def __len__(self) -> int | float:
        """
        Вывод количества на складе всех продуктов категории
        :return: Количество продуктов
        """
        sum_quantity_in_stock = 0
        for product in self.__products:
            if product:
                sum_quantity_in_stock += product.quantity_in_stock
        return sum_quantity_in_stock

    @property
    def products_list(self) -> list:
        """
        Метод вывода товаров по шаблону
        :return: list
        """
        tmp_list = []
        for product in self.__products:
            if product:
                tmp_list.append(f"{product.name_product}, {product.price} руб. Остаток: {product.quantity_in_stock}")
        return tmp_list

    @products_list.setter
    def products_list(self, product) -> None:
        """
        Метод сеттер добавление продуктов в список
        :param product: объект экземпляра класса Product
        :return: None
        """
        self.__products.append(product)


class ProductsFromCategory:
    """
    Класс, который принимает на вход категорию и дает возможность использовать цикл
    for для прохода по всем товарам данной категории.
    """

    def __init__(self, category: Category) -> None:
        self.category = category

    def __iter__(self) -> Iterator[Any]:
        return iter(self.category.products_list)
