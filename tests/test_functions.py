import json

import pytest

from src.functions import read_json_file


@pytest.fixture
def tmp_path() -> str:
    return 'tests/test.json'


def test_read_json_file_valid_file(tmp_path: str) -> None:
    """
    Тест на чтение корректного JSON-файла
    :param tmp_path: путь к файлу
    :return: None
    """
    data = [{'имя': 'Джон', 'возраст': 30}, {'имя': 'Алиса', 'возраст': 25}]

    with open(tmp_path, 'w', encoding="utf-8") as file:
        json.dump(data, file)

    assert read_json_file(str(tmp_path)) == data
