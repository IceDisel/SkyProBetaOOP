import json


def read_json_file(path: str) -> list:
    """
    Функция чтения JSON файла
    :param path: Путь до файла
    :return: Список словарей с данными
    """
    with open(path, encoding='UTF-8') as json_file:
        json_list = json.load(json_file)

    return json_list
