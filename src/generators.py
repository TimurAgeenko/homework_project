from typing import Iterator, Union


def filter_by_currency(info: list[dict], currency: str) -> Union[Iterator[dict], str]:
    """
    Принимает список словарей с транзакциями и возвращает итератор,
    который поочередно выдает транзакции, где валюта операции соответствует заданной
    """
    if not isinstance(info, list) or not isinstance(currency, str) or not info:
        return "Переданы некорректные данные"

    result = list(filter(lambda x: x["operationAmount"]["currency"]["code"] == currency, info))

    if not result:
        return "Транзакции с указанной валютой не проводились"

    for item in result:
        yield item


def transaction_descriptions(info: list[dict]) -> Union[Iterator[str], str]:
    """
    Принимает список словарей с транзакциями и возвращает описание каждой операции по очереди
    """
    if not isinstance(info, list) or not info:
        return "Переданы некорректные данные"

    for item in info:
        yield item["description"]


def card_number_generator(start: int, stop: int) -> Union[Iterator[str], str]:
    """
    Принимает диапазон чисел и генерирует номера карт в указанном диапазоне, возвращая их по очереди
    """
    if not isinstance(start, int) or not isinstance(stop, int):
        return "Укажите начальное и конечное значение числами"

    generator = ("0" * 15 + str(i) for i in range(start, stop + 1))

    for item in generator:
        result = item[-16:-12] + " " + item[-12:-8] + " " + item[-8:-4] + " " + item[-4:]
        yield result
