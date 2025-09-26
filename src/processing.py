def filter_by_state(info: list[dict], state: str = 'EXECUTED') -> list[dict]:
    """Принимает список с информацией и возвращает отредактированный список,
    в котором содержатся только словари, у которых ключ state принимает указанное значение"""
    result = []

    for item in info:
        if item["state"] == state:
            result.append(item)

    return result