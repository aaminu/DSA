import pytest
from selection_sort import selection_sort
from quick_sort import quick_sort

########################## Selection Sort #########################


def test_sorting_1():
    test_data = {
        "input": [2, 3, 5],
        "output": [2, 3, 5]
    }

    # Act
    response = selection_sort(test_data["input"])

    # Asset
    assert response == test_data["output"]


@pytest.mark.parametrize(
    "input_arr, output_arr",
    [
        ([], []),
        ([3, 1], [1, 3]),
        ([5, 4, 4, 4, 5], [4, 4, 4, 5, 5]),
        ([2, 1, 1, 1, 1], [1, 1, 1, 1, 2]),
        ([5, 4, 1, 3, 2], [1, 2, 3, 4, 5]),
        ([2.0, 1.3, 1.12, 1.0, 1.05], [1.0, 1.05, 1.12, 1.3, 2.0])
    ]
)
def test_sorting_2(input_arr, output_arr):
    # Act
    response = selection_sort(input_arr)

    # Assert
    assert response == output_arr


######################## Quick Sort #########################


@pytest.mark.parametrize(
    "input_arr, output_arr",
    [
        ([], []),
        ([3, 1], [1, 3]),
        ([5, 4, 4, 4, 5], [4, 4, 4, 5, 5]),
        ([2, 1, 1, 1, 1], [1, 1, 1, 1, 2]),
        ([5, 4, 1, 3, 2], [1, 2, 3, 4, 5]),
        ([2.0, 1.3, 1.12, 1.0, 1.05], [1.0, 1.05, 1.12, 1.3, 2.0])
    ]
)
def test_sorting_3(input_arr, output_arr):
    # Act
    response = quick_sort(input_arr)

    # Assert
    assert response == output_arr
