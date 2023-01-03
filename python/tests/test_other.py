import pytest
from other_algo.recurssion import *

########################### Recurssion Sum, Count, and Max #########################


@pytest.mark.parametrize(
    "input_arr, output",
    [
        ([5], 5),
        ([2, 3, 5, 1, 4], sum([2, 3, 5, 1, 4])),
        ([2, -1, 1, 1, 1], sum([1, -1, 1, 1, 2])),
        ([5, 4, 3, 2, 1], sum([1, 2, 3, 4, 5])),
        ([], 0)
    ]
)
def test_recursive_sum(input_arr, output):
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
def test_recursive_count(input_arr, output):
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
def test_recursive_max(input_arr, output):
    # Act
    response = recursive_max(input_arr)

    # Assert
    assert response == output
