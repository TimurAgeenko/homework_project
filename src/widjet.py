from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(account_card_num: str) -> str:
    """Принимает тип и номер карты или счета и возвращает замаскированный вариант"""
    if not isinstance(account_card_num, str):
        raise TypeError("Входные данные должны иметь тип str")

    account_card_num_list = account_card_num.split()
    digits_counter = 0

    for item in account_card_num_list:
        if item.isdigit():
            digits_counter += 1

    if digits_counter == 0:
        return "В номере не должно быть букв"

    if digits_counter > 1:
        return "В номере не должно быть пробелов"

    if "Счет" in account_card_num_list:
        for item in account_card_num_list:
            item_index = account_card_num_list.index(item)
            if item.isdigit():
                if len(item) == 20:
                    account_card_num_list[item_index] = get_mask_account(item)
                else:
                    return "Номер счета должен состоять из 20 цифр"
    else:
        for item in account_card_num_list:
            item_index = account_card_num_list.index(item)
            if item.isdigit():
                if len(item) == 16:
                    account_card_num_list[item_index] = get_mask_card_number(item)
                else:
                    return "Номер карты должен состоять из 16 цифр"

    result = " ".join(account_card_num_list)

    return result


def get_date(date: str) -> str:
    """Принимает строку с датой в одном формате и возвращает в другом"""
    if not isinstance(date, str):
        raise TypeError("Дата должна иметь тип str")

    elif len(date) != 26:
        return "Указан неверный формат даты"

    elif date[8:10].isdigit() and date[5:7].isdigit() and date[:4].isdigit():
        result = date[8:10] + "." + date[5:7] + "." + date[:4]
        return result

    else:
        return "Дата не должна содержать букв"
