import os

from src.utils import get_data


def test_get_data():
    data = get_data(r"data\operations.json")
    assert data[0]["id"] == 441945886


def test_get_data_empty():
    with open(r"data\empty.json", "w"):
        assert get_data(r"data\empty.json") == []

    os.remove(r"data\empty.json")


def test_get_data_wrong_format():
    with open(r"data\not_list.json", "w") as f:
        f.write("123")
        assert get_data(r"data\not_list.json") == []

    os.remove(r"data\not_list.json")


def test_get_data_file_not_exist():
    assert get_data(r"data\not_exist.json") == []