import pytest

from src.widjet import get_date, mask_account_card


def test_get_date_type():
    with pytest.raises(TypeError) as exc_info:
        get_date(int)

    assert str(exc_info.value) == "Дата должна иметь тип str"


@pytest.mark.parametrize(
    "value, expected",
    [
        ("2024-03-11T02:26:18.671407", "11.03.2024"),
        ("2024-03-11T02:26:18", "Указан неверный формат даты"),
        ("2024-03-11T02:26:18.671407323", "Указан неверный формат даты"),
        ("20fg-r3-1aT02:26:18.671407", "Дата не должна содержать букв"),
    ],
)
def test_get_date(value, expected):
    assert get_date(value) == expected


def test_mask_account_card_type():
    with pytest.raises(TypeError) as exc_info:
        mask_account_card(int)

    assert str(exc_info.value) == "Входные данные должны иметь тип str"


@pytest.mark.parametrize(
    "value, expected",
    [
        ("Visa Platinum 7000792289606361", "Visa Platinum 7000 79** **** 6361"),
        ("Счет 73654108430135874305", "Счет **4305"),
        ("Maestro 1596837868705199", "Maestro 1596 83** **** 5199"),
        ("MasterCard 7158300734726758", "MasterCard 7158 30** **** 6758"),
        ("Счет 7365410843013587grrg", "В номере не должно быть букв"),
        ("Visa Platinum 8990922dfs665229", "В номере не должно быть букв"),
        ("Счет 73654108430135874305328348", "Номер счета должен состоять из 20 цифр"),
        ("Счет 3538303347444", "Номер счета должен состоять из 20 цифр"),
        ("Visa Gold 5999414228426353342341", "Номер карты должен состоять из 16 цифр"),
        ("Visa Gold 5999414228", "Номер карты должен состоять из 16 цифр"),
        ("Счет 7365410843 0135874305", "В номере не должно быть пробелов"),
        ("Visa Platinum 7000792289 606361", "В номере не должно быть пробелов"),
    ],
)
def test_mask_account_card(value, expected):
    assert mask_account_card(value) == expected
