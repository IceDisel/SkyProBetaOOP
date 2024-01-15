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

    # category = Category("Электроника", "Компьютерная электроника и сотовые телефоны")

    product1 = Product("Смартфон Samsung Galaxy Note 9", "Мощный сотовый телефон с хорошей камерой",
                       90_000, 11)
    product2 = Product("Ноутбук Acer Nitro 5", "Игровой ноутбук с экраном 144Hz",
                       150_000, 3)

    repr_info = [smart1, grass1, product1, product2]
    print(repr_info)
    print("==================")
    for info in repr_info:
        print(repr(info))


if __name__ == '__main__':
    main()
