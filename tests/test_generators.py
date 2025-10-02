import pytest

from src.generators import filter_by_currency


def test_filter_by_currency(transactions):
    generator_usd = filter_by_currency(transactions, "USD")
    assert next(generator_usd) == {
                "id": 939719570,
                "state": "EXECUTED",
                "date": "2018-06-30T02:08:58.425572",
                "operationAmount": {
                    "amount": "9824.07",
                    "currency": {
                        "name": "USD",
                        "code": "USD"
                    }
                },
                "description": "Перевод организации",
                "from": "Счет 75106830613657916952",
                "to": "Счет 11776614605963066702"
    }

    assert next(generator_usd) == {
                "id": 142264268,
                "state": "EXECUTED",
                "date": "2019-04-04T23:20:05.206878",
                "operationAmount": {
                    "amount": "79114.93",
                    "currency": {
                        "name": "USD",
                        "code": "USD"
                    }
                },
                "description": "Перевод со счета на счет",
                "from": "Счет 19708645243227258542",
                "to": "Счет 75651667383060284188"
    }

    generator_rub = filter_by_currency(transactions, "RUB")
    assert next(generator_rub) == {
                "id": 873106923,
                "state": "EXECUTED",
                "date": "2019-03-23T01:09:46.296404",
                "operationAmount": {
                    "amount": "43318.34",
                    "currency": {
                        "name": "руб.",
                        "code": "RUB"
                    }
                },
                "description": "Перевод со счета на счет",
                "from": "Счет 44812258784861134719",
                "to": "Счет 74489636417521191160"
    }

    assert next(generator_rub) == {
                "id": 594226727,
                "state": "CANCELED",
                "date": "2018-09-12T21:27:25.241689",
                "operationAmount": {
                    "amount": "67314.70",
                    "currency": {
                        "name": "руб.",
                        "code": "RUB"
                    }
                },
                "description": "Перевод организации",
                "from": "Visa Platinum 1246377376343588",
                "to": "Счет 14211924144426031657"
    }


def test_filter_by_currency_type_or_empty():
    with pytest.raises(StopIteration) as exc_info:
        next(filter_by_currency(int, str))
        next(filter_by_currency(list, int))
        next(filter_by_currency([], "USD"))

    assert str(exc_info.value) == "Переданы некорректные данные"



def test_filter_by_currency_empty_result(transactions):
    with pytest.raises(StopIteration) as exc_info:
        next(filter_by_currency(transactions, "123"))

    assert str(exc_info.value) == "Транзакции с указанной валютой не проводились"