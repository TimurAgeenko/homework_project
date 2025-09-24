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
