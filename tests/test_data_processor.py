import pytest

from src.data_processor import get_csv


def test_get_csv():
    data = get_csv("./data/transactions.csv")
    assert data[0]["id"] == 650703.0
    assert data[1]["date"] == "2020-12-06T23:00:58Z"


def test_get_csv_not_exist():
    with pytest.raises(FileNotFoundError) as e:
        get_csv("./data/transaction.csv")
    assert str(e.value) == "File './data/transaction.csv' not found."


def test_get_csv_not_csv():
    with pytest.raises(ValueError) as e:
        get_csv("./data/operations.json")
    assert str(e.value) == "File './data/operations.json' is not a csv."
