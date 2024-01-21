import pytest

from models.Category import Category
from models.LawnGrass import LawnGrass
from models.Smartphone import Smartphone

smart1 = Smartphone("Смартфон Samsung Galaxy S23 Ultra 5G", "Мощный сотовый телефон с хорошей камерой",
                    124_990, 7, "Snapdragon 8 Gen 2 for Galaxy", "SM-S918B",
                    "оперативная 12 ГБ, встроенная 512 ГБ", "черный фантом")

grass1 = LawnGrass("Низкорослый газон Greenlab 4 кг", "Газонная трава способствует очищению воздуха от токсинов",
                   2384, 70, "Германия", "на 5-й день", "зеленый")


@pytest.fixture(scope='function')
def category_electronics() -> Category:
    Category.total_unique_products = 0
    return Category("Электроника", "Компьютерная электроника и сотовые телефоны")


def test_init(category_electronics: Category) -> None:
    """
    Тест инициализации аргументов класса Category
    :param category_electronics:
    :return:
    """
    assert category_electronics.name_category == "Электроника"
    assert category_electronics.description_category == "Компьютерная электроника и сотовые телефоны"

    assert Category.total_categories == 1


def test_average_price_products(category_electronics: Category) -> None:
    """
    Тест метода average_price_products в классе Category
    :param category_electronics:
    :return: None
    """
    assert category_electronics.average_price_products() == "Средний ценник всех товаров = 0"

    category_electronics.products_list = smart1
    category_electronics.products_list = grass1
    assert category_electronics.average_price_products() == "Средний ценник всех товаров = 13530.0"
