from typing import Iterator, Union


def filter_by_currency(info: list[dict], currency: str) -> Union[Iterator[dict] or str]:
    if not isinstance(info, list) or not isinstance(currency, str) or not info:
        return "Переданы некорректные данные"

    result = list(filter(lambda x: x["operationAmount"]["currency"]["code"] == currency, info))

    if not result:
        return "Транзакции с указанной валютой не проводились"

    for item in result:
        yield item


def transaction_descriptions(info: list[dict]) -> Union[Iterator[str] or str]:
    if not isinstance(info, list) or not info:
        return "Переданы некорректные данные"

    for item in info:
        yield item["description"]