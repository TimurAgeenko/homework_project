import logging

logger = logging.getLogger("masks")
file_handler = logging.FileHandler(r"log\masks.log", mode="w")
file_formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)
logger.setLevel(logging.DEBUG)


def get_mask_card_number(card_number: str) -> str:
    """Принимает номер карты и возвращает его замаскированный вариант"""
    if not isinstance(card_number, str):
        logger.error("Возникла ошибка: номер карты не соответствует типу str.")
        raise TypeError("Номер карты должен иметь тип str")

    elif card_number.isalpha():
        logger.error("Возникла ошибка: в номере карты содержатся буквы.")
        return "В номере карты не должно быть букв"

    elif len(card_number) != 16:
        logger.error("Возникла ошибка: в номере карты неправильное количество символов.")
        return "Номер карты должен состоять из 16 цифр"

    logger.info(f"Маскируем указанный номер карты: {card_number}")
    result = card_number[:4] + " " + card_number[4:6] + "** **** " + card_number[-4:]

    return result


def get_mask_account(account_number: str) -> str:
    """Принимает номер счета и возвращает его замаскированный вариант"""
    if not isinstance(account_number, str):
        logger.error("Возникла ошибка: номер счета не соответствует типу str.")
        raise TypeError("Номер счета должен иметь тип str")

    elif account_number.isalpha():
        logger.error("Возникла ошибка: в номере счета содержатся буквы.")
        return "В номере счета не должно быть букв"

    elif len(account_number) != 20:
        logger.error("Возникла ошибка: в номере счета неправильное количество символов.")
        return "Номер счёта должен состоять из 20 цифр"

    logger.info(f"Маскируем указанный номер счета: {account_number}")
    return "**" + account_number[-4:]
