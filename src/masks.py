def get_mask_card_number(card_number: str) -> str:
    """Принимает номер карты и возвращает его замаскированный вариант"""
    result = card_number[:4] + " " + card_number[4:6] + "** **** " + card_number[-4:]

    return result


def get_mask_account(account_number: str) -> str:
    """Принимает номер счета и возвращает его замаскированный вариант"""
    if not isinstance(account_number, str):
        raise TypeError("Номер счета должен иметь тип str")

    elif account_number.isalpha():
        return "В номере счета не должно быть букв"

    elif len(account_number) != 20:
        return "Номер счёта должен состоять из 20 цифр"

    return "**" + account_number[-4:]
