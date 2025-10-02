import pytest

from src.processing import filter_by_state, sort_by_date


def test_filter_by_state_type():
    with pytest.raises(TypeError) as exc_info:
        filter_by_state(int)
        filter_by_state(list, int)

    assert str(exc_info.value) == "Переданы некорректные данные"


def test_filter_by_state(list_for_tests, executed_list, canceled_list):
    assert filter_by_state(list_for_tests) == executed_list
    assert filter_by_state(list_for_tests, 'CANCELED') == canceled_list
    assert filter_by_state(canceled_list) == []
    assert filter_by_state(list_for_tests, '123') == []


def test_sort_by_date_type():
    with pytest.raises(TypeError) as exc_info:
        sort_by_date(int)
        sort_by_date(list, int)

    assert str(exc_info.value) == "Переданы некорректные данные"


def test_sort_by_date(list_for_tests, sorted_list, reverse_sorted_list):
    assert sort_by_date(list_for_tests) == reverse_sorted_list
    assert sort_by_date(list_for_tests, False) == sorted_list


def test_sort_by_date_value():
    with pytest.raises(ValueError) as exc_info:
        sort_by_date([{'id': 939719570, 'date': '2018-06-30T02:08:58.425'}])
        sort_by_date([{'id': 939719570, 'date': '2018-06-30T02:08:58.425654345'}])

    assert str(exc_info.value) == "Указан неверный формат даты"

    with pytest.raises(ValueError) as exc_info:
        sort_by_date([{'id': 939719570, 'date': '20fd-r6-3sT02:08:58.425654'}])

    assert str(exc_info.value) == "Дата не должна содержать букв"
