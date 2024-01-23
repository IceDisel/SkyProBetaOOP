# Домашнее задание 16.1. Исключения

## Код в файле main.py предназначен только для визуального тестирования программы.
### Для запуска проекта `main`
### Для запуска тестов 
```bash
pytest --cov
```
#### Пример работы программы

```text
23088.75
0
Traceback (most recent call last):
  File "D:\Project\Python\SkyProBetaOOP\src\main.py", line 37, in <module>
    main()
  File "D:\Project\Python\SkyProBetaOOP\src\main.py", line 32, in main
    product2 = Product.add_product("Ноутбук Acer Nitro 5", "Игровой ноутбук с экраном 144Hz",
  File "D:\Project\Python\SkyProBetaOOP\models\Product.py", line 104, in add_product
    return Product(name_product, description_product, price, quantity_in_stock)
  File "D:\Project\Python\SkyProBetaOOP\models\Product.py", line 39, in __init__
    raise ValueError("Товар с нулевым количеством не может быть добавлен")
ValueError: Товар с нулевым количеством не может быть добавлен

Process finished with exit code 1

```