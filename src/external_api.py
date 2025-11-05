import os
from typing import Callable

import requests
from dotenv import load_dotenv


def get_convert_amount(transaction_amount: float, transaction_code: str) -> float:
    """
    Принимает на вход сумму транзакции и её код: USD, EUR и т.д.
    Делает запрос для конвертации суммы в рубли и возвращает результат
    """
    load_dotenv()
    api_key = os.getenv("API_KEY")
    url = "https://api.apilayer.com/exchangerates_data/convert"
    headers = {"apikey": f"{api_key}"}
    params = {"amount": f"{transaction_amount}", "from": transaction_code, "to": "RUB"}
    response = requests.get(url=url, headers=headers, params=params)
    result = response.json()
    return result["result"]


def get_transaction_amount(transaction: dict) -> float:
    """
    Принимает на вход словарь с данными о транзакции и возвращает сумму транзакции рублях
    """
    if not isinstance(transaction, dict) or transaction == {}:
        raise ValueError("Переданы некорректные данные")

    transaction_amount = float(transaction["operationAmount"]["amount"])
    transaction_code = transaction["operationAmount"]["currency"]["code"]

    if transaction_code == "RUB":
        return transaction_amount
    else:
        convert_amount = get_convert_amount(transaction_amount, transaction_code)
        return convert_amount
