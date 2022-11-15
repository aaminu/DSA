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
