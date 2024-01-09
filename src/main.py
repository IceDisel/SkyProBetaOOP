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

    category = Category("Электроника", "Компьютерная электроника и сотовые телефоны")

    product1 = Product("Смартфон Samsung Galaxy Note 9", "Мощный сотовый телефон с хорошей камерой",
                       90_000, 11)
    product2 = Product("Ноутбук Acer Nitro 5", "Игровой ноутбук с экраном 144Hz",
                       150_000, 3)

    print("""Задание 1
Создать два класса наследуясь от Product\n""")

    print(smart1)
    print(grass1)

    print("\n====================================")
    print("""\nЗадание 2
Доработать функционал сложения, чтобы можно было складывать товары только из одинаковых классов продуктов.\n""")

    print(product2 + grass1)
    print(smart1 + grass1)
    print(type(product1 + product2))
    print(product1 + smart1)

    print("\n====================================")
    print("""\nЗадание 3
Доработайте метод добавления продукта в категорию таким образом,
чтобы не было возможности добавить вместо продукта или его наследников любой другой объект.\n""")

    category.products_list = product2
    category.products_list = product1
    category.products_list = [1, 2, 3]
    category.products_list = smart1
    category.products_list = dict
    category.products_list = grass1

    pr = ProductsFromCategory(category)
    for item in pr:
        print(item)


if __name__ == '__main__':
    main()
