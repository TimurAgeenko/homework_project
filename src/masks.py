def get_mask_card_number(card_number: str) -> str:
    """Принимает номер карты и возвращает его замаскированный вариант"""
    result = card_number[:4] + " " + card_number[4:6] + "** **** " + card_number[-4:]

    return result


def get_mask_account(account_number: str) -> str:
    """Принимает номер счета и возвращает его замаскированный вариант"""
    result = "**" + account_number[-4:]

    return result
