import pytest
from recurssion import *


def test_recursive_sum_1():
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
        ([5], 5),
        ([2, -1, 1, 1, 1], sum([1, -1, 1, 1, 2])),
        ([5, 4, 3, 2, 1], sum([1, 2, 3, 4, 5])),
        ([], 0)
    ]
)
def test_recursive_sum_2(input_arr, output):
    # Act
    response = recursive_sum(input_arr)

    # Assert
    assert response == output


@pytest.mark.parametrize(
    "input_arr, output",
    [
        (list(range(100)), 100),
        (list(range(78)), 78),
        ([], 0),
        ([1], 1)
    ]
)
def test_recursive_count_1(input_arr, output):
    # Act
    response = recursive_count(input_arr)

    # Assert
    assert response == output


@pytest.mark.parametrize(
    "input_arr, output",
    [
        (list(range(100)), 99),
        (list(range(78, 55, -1)), 78),
        ([], None),
        ([1], 1)
    ]
)
def test_recursive_max_1(input_arr, output):
    # Act
    response = recursive_max(input_arr)

    # Assert
    assert response == output
