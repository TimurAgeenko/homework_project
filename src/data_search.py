import re
from collections import Counter


def process_bank_search(data: list[dict], search: str) -> list[dict]:
    result = []
    for item in data:
        if re.search(search, item["description"], flags=re.IGNORECASE):
            result.append(item)

    return result


def process_bank_operations(data: list[dict], categories: list) -> dict:
    descriptions = []
    for item in data:
        for category in categories:
            if re.search(category, item["description"], flags=re.IGNORECASE):
                descriptions.append(category)

    counted = Counter(descriptions)
    return counted
