import pytest
from binary_search import binary_search


def test_selection_1():
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
def test_selection_2(input_arr, value, output_index):
    # Act
    response = binary_search(input_arr, value)

    # Assert
    assert response == output_index
