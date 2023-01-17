""" Different Algorithms using recurssion """

from typing import Union

Num = Union[int, float]


def recursive_sum(arr: list[Num]) -> Num:
    """Sum the elements in an array using recurssion"""
    if len(arr) == 0:
        return 0
    return arr.pop(0) + recursive_sum(arr)


def recursive_count(arr: list[Num]) -> Num:
    """Count the number of elements in an array using recurssion"""
    if len(arr) == 0:
        return 0
    arr.pop(0)
    return 1 + recursive_count(arr)


def recursive_max(arr: list[Num]) -> Union[Num, None]:
    """Get the maximum number of in an array using recurssion"""
    if len(arr) == 0:
        return None
    if len(arr) == 1:
        return arr[0]
    value = arr.pop(0)
    return value if value >= recursive_max(arr) else recursive_max(arr)
