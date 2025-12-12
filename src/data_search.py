import re


def process_bank_search(data: list[dict], search: str) -> list[dict]:
    result = []
    for item in data:
        if re.search(search, item["description"], flags=re.IGNORECASE):
            result.append(item)

    return result
