from models.Category import Category, ProductsFromCategory
from models.LawnGrass import LawnGrass
from models.Product import Product
from models.Smartphone import Smartphone


# Данный код является для проверки программы!!!
def main() -> None:
    smart1 = Smartphone("Смартфон Samsung Galaxy S23 Ultra 5G", "Мощный сотовый телефон с хорошей камерой",
                        124_990, 7, "Snapdragon 8 Gen 2 for Galaxy", "SM-S918B",
                        "оперативная 12 ГБ, встроенная 512 ГБ", "черный фантом")

    grass1 = LawnGrass("Низкорослый газон Greenlab 4 кг", "Газонная трава способствует очищению воздуха от токсинов",
                       2384, 70, "Германия", "на 5-й день", "зеленый")

    product1 = Product("Смартфон Samsung Galaxy Note 9", "Мощный сотовый телефон с хорошей камерой",
                       90_000, 11)
    product2 = Product.add_product("Ноутбук Acer Nitro 5", "Игровой ноутбук с экраном 144Hz",
                                   150_000, 0)

    category = Category("Электроника", "Компьютерная электроника и сотовые телефоны")

    category.products_list = smart1
    category.products_list = grass1
    # category.products_list = product1
    # category.products_list = product2

    print(category.average_price_products())

    category1 = Category("Автомобили", "Автомобили с пробегом")

    print(category1.average_price_products())


if __name__ == '__main__':
    main()
