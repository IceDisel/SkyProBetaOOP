import pytest

from models.Category import Category
from models.Product import Product


@pytest.fixture
def product_notebook() -> Product:
    return Product("Ноутбук Acer Nitro 5", "Игровой ноутбук с экраном 144Hz",
                   150_000, 3)


def test_init(product_notebook: Product) -> None:
    """
    Тест инициализации аргументов класса Product
    :param product_notebook:
    :return:
    """
    assert product_notebook.name_product == "Ноутбук Acer Nitro 5"
    assert product_notebook.description_product == "Игровой ноутбук с экраном 144Hz"
    assert product_notebook.price == 150_000
    assert product_notebook.quantity_in_stock == 3

    assert Category.total_unique_products == 1
