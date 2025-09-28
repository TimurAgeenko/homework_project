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
