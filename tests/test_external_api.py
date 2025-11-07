import os
from unittest.mock import patch

import pytest
from dotenv import load_dotenv

from src.external_api import get_convert_amount, get_transaction_amount


@patch("requests.get")
def test_get_convert_amount(mock_get):
    mock_get.return_value.json.return_value = {
        "success": True,
        "query": {"from": "USD", "to": "RUB", "amount": 79114.93},
        "info": {"timestamp": 1762364105, "rate": 81.347862},
        "date": "2025-11-05",
        "result": 6435830.40778,
    }
    assert get_convert_amount(79114.93, "USD") == 6435830.40778

    load_dotenv()
    api_key = os.getenv("API_KEY")
    url = "https://api.apilayer.com/exchangerates_data/convert"
    headers = {"apikey": f"{api_key}"}
    params = {"amount": "79114.93", "from": "USD", "to": "RUB"}
    mock_get.assert_called_once_with(url=url, headers=headers, params=params)


def test_get_transaction_amount_rub(transactions):
    assert get_transaction_amount(transactions[2]) == 43318.34
    assert get_transaction_amount(transactions[4]) == 67314.70


def test_get_transaction_amount_error():
    with pytest.raises(ValueError) as e:
        get_transaction_amount(None)
        get_transaction_amount({})
    assert str(e.value) == "Переданы некорректные данные"


@patch("src.external_api.get_convert_amount")
def test_get_transaction_amount_usd(mock_get, transactions):
    mock_get.return_value = 799188.232037
    assert get_transaction_amount(transactions[0]) == 799188.232037
    mock_get.assert_called_once_with(9824.07, "USD")
