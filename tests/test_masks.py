import pytest

from src.masks import get_mask_account, get_mask_card_number


@pytest.mark.parametrize(
    "value, expected",
    [
        ("73654108430135874305", "**4305"),
        ("alpha", "В номере счета не должно быть букв"),
        ("1234", "Номер счёта должен состоять из 20 цифр"),
        ("123412341234123412341234", "Номер счёта должен состоять из 20 цифр"),
    ],
)
def test_get_mask_account(value, expected):
    assert get_mask_account(value) == expected


def test_get_mask_account_type():
    with pytest.raises(TypeError) as exc_info:
        get_mask_account(int)

    assert str(exc_info.value) == "Номер счета должен иметь тип str"


@pytest.mark.parametrize(
    "value, expected",
    [
        ("7000792289606361", "7000 79** **** 6361"),
        ("alpha", "В номере карты не должно быть букв"),
        ("1234", "Номер карты должен состоять из 16 цифр"),
        ("123412341234123412341234", "Номер карты должен состоять из 16 цифр"),
    ],
)
def test_get_mask_card_number(value, expected):
    assert get_mask_card_number(value) == expected


def test_get_mask_card_number_type():
    with pytest.raises(TypeError) as exc_info:
        get_mask_card_number(int)

    assert str(exc_info.value) == "Номер карты должен иметь тип str"
