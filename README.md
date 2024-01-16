# Домашнее задание 15.1. Наследование

## Код в файле main.py предназначен только для визуального тестирования программы.
### Для запуска проекта `main`
### Для запуска тестов 
```bash
pytest --cov
```
#### Пример работы программы

```text
[Создан объект Smartphone - {'name_product': 'Смартфон Samsung Galaxy S23 Ultra 5G', 'description_product': 'Мощный сотовый телефон с хорошей камерой', '_Product__price': 124990, 'quantity_in_stock': 7, 'performance': 'Snapdragon 8 Gen 2 for Galaxy', 'model': 'SM-S918B', 'memory': 'оперативная 12 ГБ, встроенная 512 ГБ', 'color': 'черный фантом'}, Создан объект LawnGrass - {'name_product': 'Низкорослый газон Greenlab 4 кг', 'description_product': 'Газонная трава способствует очищению воздуха от токсинов', '_Product__price': 2384, 'quantity_in_stock': 70, 'manufacturer_country': 'Германия', 'germination_period': 'на 5-й день', 'color': 'зеленый'}, Создан объект Product - {'name_product': 'Смартфон Samsung Galaxy Note 9', 'description_product': 'Мощный сотовый телефон с хорошей камерой', '_Product__price': 90000, 'quantity_in_stock': 11}, Создан объект Product - {'name_product': 'Ноутбук Acer Nitro 5', 'description_product': 'Игровой ноутбук с экраном 144Hz', '_Product__price': 150000, 'quantity_in_stock': 3}]
==================
Создан объект Smartphone - {'name_product': 'Смартфон Samsung Galaxy S23 Ultra 5G', 'description_product': 'Мощный сотовый телефон с хорошей камерой', '_Product__price': 124990, 'quantity_in_stock': 7, 'performance': 'Snapdragon 8 Gen 2 for Galaxy', 'model': 'SM-S918B', 'memory': 'оперативная 12 ГБ, встроенная 512 ГБ', 'color': 'черный фантом'}
Создан объект LawnGrass - {'name_product': 'Низкорослый газон Greenlab 4 кг', 'description_product': 'Газонная трава способствует очищению воздуха от токсинов', '_Product__price': 2384, 'quantity_in_stock': 70, 'manufacturer_country': 'Германия', 'germination_period': 'на 5-й день', 'color': 'зеленый'}
Создан объект Product - {'name_product': 'Смартфон Samsung Galaxy Note 9', 'description_product': 'Мощный сотовый телефон с хорошей камерой', '_Product__price': 90000, 'quantity_in_stock': 11}
Создан объект Product - {'name_product': 'Ноутбук Acer Nitro 5', 'description_product': 'Игровой ноутбук с экраном 144Hz', '_Product__price': 150000, 'quantity_in_stock': 3}

Process finished with exit code 0

```