import pytest
from recurssion import *


def test_selection_1():
    test_data = {
        "input": [2, 3, 5, 1, 4],
        "output": sum([2, 3, 5, 1, 4])
    }

    # Act
    response = recursive_sum(test_data["input"])

    # Asset
    assert response == test_data["output"]


@pytest.mark.parametrize(
    "input_arr, output",
    [
        ([5, 4, 4, 4, 5], sum([4, 4, 4, 5, 5])),
        ([2, 1, 1, 1, 1], sum([1, 1, 1, 1, 2])),
        ([5, 4, 3, 2, 1], sum([1, 2, 3, 4, 5])),
        ([2.0, 1.3, 1.12, 1.0, 1.05], sum([1.0, 1.05, 1.12, 1.3, 2.0]))
    ]
)
def test_selection_2(input_arr, output):
    # Act
    response = recursive_sum(input_arr)

    # Assert
    assert response == output