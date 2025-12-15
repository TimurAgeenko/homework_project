import re
from collections import Counter


def process_bank_search(data: list[dict], search: str) -> list[dict]:
    """
    Принимает на вход список транзакций и строку поиска и возвращает список транзакций,
    у которых в описании есть указанная строка
    """
    result = []
    for item in data:
        if re.search(search, item["description"], flags=re.IGNORECASE):
            result.append(item)

    return result


def process_bank_operations(data: list[dict], categories: list) -> dict:
    """
    Принимает на вход список транзакций и список категорий,
    каждая из которых представляет собой описание транзакций,
    и возвращает словарь, в котором ключи - это названия категорий,
    а значения - это количество операций в каждой категории
    """
    descriptions = []
    for item in data:
        for category in categories:
            if re.search(category, item["description"], flags=re.IGNORECASE):
                descriptions.append(item["description"])

    counted = Counter(descriptions)
    return counted
