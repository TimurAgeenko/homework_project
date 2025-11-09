import json
import logging

logger = logging.getLogger("utils")
file_handler = logging.FileHandler(r"log\utils.log", mode="w")
file_formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)
logger.setLevel(logging.DEBUG)


def get_data(path: str) -> list:
    """
     Выполняет десериализацию json файла и возвращает список словарей с данными о финансовых транзакциях.
    Если у данных неправильный формат, если использовать в функции путь к пустому файлу или к файлу,
    которого не существует, то она вернет пустой список.
    """
    try:
        logger.info("Открываем файл из указанного пути и возвращаем json объект.")
        with open(path, encoding="utf-8") as f:
            return json.load(f)
    except Exception:
        logger.error("Возникла ошибка, возвращаем пустой список.")
        return []
