import pytest
from search_in_list import search_in_list


@pytest.mark.parametrize("test_input_list, test_input_item, expected", [
    ([1, 2, 3, 4, 5], 3, True),
    (["apple", "banana", "orange"], "banana", True),
    ([True, False, True], False, True),
    ([], "item", False),
])
def test_search_in_list(test_input_list, test_input_item, expected):
    assert search_in_list(test_input_list, test_input_item) == expected
