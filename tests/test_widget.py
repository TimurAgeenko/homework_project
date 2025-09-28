import pytest

from src.widjet import mask_account_card, get_date

def test_get_date_type():
    with pytest.raises(TypeError) as exc_info:
        get_date(int)

    assert str(exc_info.value) == "Дата должна иметь тип str"


@pytest.mark.parametrize("value, expected", [
    ("2024-03-11T02:26:18.671407", "11.03.2024"),
    ("2024-03-11T02:26:18", "Указан неверный формат даты"),
    ("2024-03-11T02:26:18.671407323", "Указан неверный формат даты"),
    ("20fg-r3-1aT02:26:18.671407", "Дата не должна содержать букв")
])
def test_get_date(value, expected):
    assert get_date(value) == expected
