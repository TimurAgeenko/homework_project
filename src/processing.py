import datetime as dt

from src.widjet import get_date


def filter_by_state(info: list[dict], state: str = "EXECUTED") -> list[dict]:
    """Принимает список с информацией и возвращает отредактированный список
    со словарями, у которых ключ state принимает указанное значение"""
    if not isinstance(info, list) or not isinstance(state, str):
        raise TypeError("Переданы некорректные данные")

    result = []

    for item in info:
        if item["state"] == state:
            result.append(item)

    return result


def sort_by_date(info: list[dict], reverse: bool = True) -> list[dict]:
    """Принимает список и возвращает его отсортированный по дате вариант, по умолчанию - по убыванию"""
    if not isinstance(info, list) or not isinstance(reverse, bool):
        raise TypeError("Переданы некорректные данные")

    for item in info:
        if not item["date"][8:10].isdigit() or not item["date"][5:7].isdigit() or not item["date"][:4].isdigit():
            raise ValueError("Дата не должна содержать букв")

    result = sorted(info, key=lambda x: dt.datetime.strptime(get_date(x["date"]), "%d.%m.%Y"), reverse=reverse)

    return result
