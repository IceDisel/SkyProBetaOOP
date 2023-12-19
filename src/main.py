from models.Category import Category
from models.Product import Product


# Данный код является для проверки программы!!!
def main():
    category = Category("Электроника", "Компьютерная электроника и сотовые телефоны")

    product1 = Product("Смартфон Samsung Galaxy Note 9", "Мощный сотовый телефон с хорошей камерой",
                       90_000, 11)
    product2 = Product("Ноутбук Acer Nitro 5", "Игровой ноутбук с экраном 144Hz",
                       150_000, 3)

    category.products.append(product1)
    category.products.append(product2)

    print(f"Категория: {category.name_category}")
    print(f"Описание: {category.description_category}")
    print("Товары:")
    for product in category.products:
        print(f"- {product.name_product}: {product.description_product}, Цена: {product.price},"
              f"Количество: {product.quantity_in_stock}")

    print(f"\n- Количество категорий - {category.total_categories}")
    print(f"- Количество уникальных товаров - {category.total_unique_products}")


if __name__ == '__main__':
    main()
