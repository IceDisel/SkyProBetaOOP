# Домашнее задание 14.1. Магические методы

## Код в файле main.py предназначен только для визуального тестирования программы.
### Для запуска проекта `main`
### Для запуска тестов 
```bash
pytest --cov
```
#### Пример работы программы

```text
Задание 1
Для класса Product добавить строковое отображение
Смартфон Samsung Galaxy Note 9, 90000 руб. Остаток: 11 шт.

Для класса Category добавить строковое отображение
Электроника, количество продуктов: 14 шт.

Задание 2
Для класса Product необходимо добавить возможность складывать объекты между собой
1440000

* Дополнительное задание
Ноутбук Acer Nitro 5, 150000 руб. Остаток: 3
Смартфон Samsung Galaxy Note 9, 90000 руб. Остаток: 11
```

#### Пример выполненных тестов
```text
=========================================================== test session starts ===========================================================
platform win32 -- Python 3.10.9, pytest-7.4.3, pluggy-1.3.0
rootdir: D:\Project\Python\SkyProBetaOOP                   
plugins: cov-4.1.0                                         
collected 3 items

tests\test_Category.py .                                                                                                          [ 33%]
tests\test_Product.py .                                                                                                           [ 66%]
tests\test_functions.py .                                                                                                         [100%]

---------- coverage: platform win32, python 3.10.9-final-0 -----------
Name                      Stmts   Miss  Cover                         
---------------------------------------------                         
models\Category.py           22      6    73%                         
models\Product.py            24      9    62%                         
models\__init__.py            0      0   100%                         
src\__init__.py               0      0   100%                         
src\functions.py              5      0   100%
tests\__init__.py             0      0   100%
tests\test_Category.py        9      0   100%
tests\test_Product.py        12      0   100%
tests\test_functions.py      11      0   100%
---------------------------------------------
TOTAL                        83     15    82%

============================================================ 3 passed in 0.09s ============================================================ 
```