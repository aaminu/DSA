""" Different Algorithms using recurssion """

from typing import Union

Num = Union[int, float]


def recursive_sum(arr: list[Num]) -> Num:
    if len(arr) == 1:
        return arr[0]
    return arr.pop(0) + recursive_sum(arr)
