from sort_search_algos.binary_search import binary_search
from sort_search_algos.selection_sort import selection_sort
from sort_search_algos.quick_sort import quick_sort
import pytest

########################## binary Search #########################


def test_binary_search_1():
    # Gather
    test_data = {
        "input": [2, 3, 5, 1, 4],
        "value": 5,
        "output": 2
    }

    # Act
    response = binary_search(test_data["input"], test_data["value"])

    # Asset
    assert response == test_data["output"]


@pytest.mark.parametrize(
    "input_arr, value, output_index",
    [
        (list(range(100)), 0, 0),
        (list(range(100)), 99, 99),
        (list(range(1, 100)), 50, 49),
        (list(range(1, 100)), 25, 24),
        (list(range(0, 100, 2)), 25, None),
        (list(range(0, 10, 3)), 8, None)
    ]
)
def test_binary_search_2(input_arr, value, output_index):
    # Act
    response = binary_search(input_arr, value)

    # Assert
    assert response == output_index


########################## Selection Sort #########################

@pytest.mark.parametrize(
    "input_arr, output_arr",
    [
        ([], []),
        ([2, 3, 5], [2, 3, 5]),
        ([3, 1], [1, 3]),
        ([5, 4, 4, 4, 5], [4, 4, 4, 5, 5]),
        ([2, 1, 1, 1, 1], [1, 1, 1, 1, 2]),
        ([5, 4, 1, 3, 2], [1, 2, 3, 4, 5]),
        ([2.0, 1.3, 1.12, 1.0, 1.05], [1.0, 1.05, 1.12, 1.3, 2.0])
    ]
)
def test_selection_sort(input_arr, output_arr):
    # Act
    response = selection_sort(input_arr)

    # Assert
    assert response == output_arr

######################## Quick Sort #########################


@pytest.mark.parametrize(
    "input_arr, output_arr",
    [
        ([], []),
        ([2, 3, 5], [2, 3, 5]),
        ([3, 1], [1, 3]),
        ([5, 4, 4, 4, 5], [4, 4, 4, 5, 5]),
        ([2, 1, 1, 1, 1], [1, 1, 1, 1, 2]),
        ([5, 4, 1, 3, 2], [1, 2, 3, 4, 5]),
        ([2.0, 1.3, 1.12, 1.0, 1.05], [1.0, 1.05, 1.12, 1.3, 2.0])
    ]
)
def test_quick_sort(input_arr, output_arr):
    # Act
    response = quick_sort(input_arr)

    # Assert
    assert response == output_arr
