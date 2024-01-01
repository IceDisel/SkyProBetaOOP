from models.Category import Category, ProductsFromCategory
from models.Product import Product
from src.functions import read_json_file
from src.settings import PATH_JSON


# Данный код является для проверки программы!!!
def main() -> None:
    category = Category("Электроника", "Компьютерная электроника и сотовые телефоны")

    product1 = Product("Смартфон Samsung Galaxy Note 9", "Мощный сотовый телефон с хорошей камерой",
                       90_000, 11)
    product2 = Product("Ноутбук Acer Nitro 5", "Игровой ноутбук с экраном 144Hz",
                       150_000, 3)

    category.products_list = product2
    category.products_list = product1

    print("""Задание 1
Для класса Product добавить строковое отображение""")
    print(product1)

    print("""\nДля класса Category добавить строковое отображение""")
    print(category)

    print("""\nЗадание 2
Для класса Product необходимо добавить возможность складывать объекты между собой""")
    print(product1 + product2)

    print("""\n* Дополнительное задание""")

    pr = ProductsFromCategory(category)
    for item in pr:
        print(item)


if __name__ == '__main__':
    main()
