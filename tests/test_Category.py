import pytest

from models.Category import Category


@pytest.fixture
def category_electronics() -> Category:
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
