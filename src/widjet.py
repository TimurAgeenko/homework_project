from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(account_card_num: str) -> str:
    """Принимает тип и номер карты или счета и возвращает замаскированный вариант"""
    account_card_num_list = account_card_num.split()

    if "Счет" in account_card_num_list:
        for item in account_card_num_list:
            item_index = account_card_num_list.index(item)
            if item.isdigit():
                account_card_num_list[item_index] = get_mask_account(item)
    else:
        for item in account_card_num_list:
            item_index = account_card_num_list.index(item)
            if item.isdigit():
                account_card_num_list[item_index] = get_mask_card_number(item)

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
