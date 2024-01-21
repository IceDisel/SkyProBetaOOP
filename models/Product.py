from models.Category import Category
from abc import ABC, abstractmethod

from models.ReportMixin import ReportMixin


class AbstractProduct(ABC):
    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def price(self):
        pass

    @abstractmethod
    def __add__(self, other):
        pass

    @abstractmethod
    def __str__(self):
        pass


class Product(AbstractProduct, ReportMixin):
    """
    Класс, представляющий продукт.
    """

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
        self.__price = price
        self.quantity_in_stock = quantity_in_stock
        Category.total_unique_products += 1

        super().__repr__(self.__dict__)

    def __add__(self, other) -> str | int | float:
        """
        Сложение объектов между собой
        :param other:
        :return:
        """
        try:
            if not isinstance(other, self.__class__):
                raise TypeError("Невозможно выполнить сложение с разными типами")
            return self.__price * self.quantity_in_stock + other.__price * other.quantity_in_stock
        except TypeError as e:
            return str(e)

    def __str__(self) -> str:
        """
        Строковое отображение количества продукта
        :return:
        """
        return f"{self.name_product}, {self.__price} руб. Остаток: {self.quantity_in_stock} шт."

    @property
    def price(self) -> float:
        """
        Метод геттер вывода цены
        :return: float
        """
        return self.__price

    @price.setter
    def price(self, new_price: float) -> None:
        """
        Метод сеттер изменения цены на товар
        :param new_price: Новая цена
        :return: Измененная цена
        """
        if new_price < self.__price:
            confirmation = input(f"Цена будет понижена на товар {self.name_product}. Вы согласны? (y/n): ")
            if confirmation.lower() == "y":
                self.__price = new_price
                print(f"Цена успешно понижена на товар {self.name_product}.")
            else:
                print("Действие отменено.")
        else:
            self.__price = new_price
            print(f"Цена успешно обновлена на товар {self.name_product}.")

    @staticmethod
    def add_product(name_product: str, description_product: str, price: float, quantity_in_stock: int):
        """
        Метод добавления нового товара.
        :param name_product: Название продукта.
        :param description_product: Описание продукта.
        :param price: Цена продукта.
        :param quantity_in_stock: Количество продукта на складе.
        :return: Экземпляр класса Product
        """
        try:
            if quantity_in_stock <= 0:
                raise ValueError
        except ValueError:
            print("Товар с нулевым количеством не может быть добавлен")
        else:
            return Product(name_product, description_product, price, quantity_in_stock)
