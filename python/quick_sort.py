""" Quick Sort Algorithm based Divide and Conquer"""

from typing import Union

Num = Union[int, float]


def quick_sort(arr: list[Num]) -> list[Num]:
    if len(arr) < 2:
        return arr
    pivot = arr[0]
    less = [i for i in arr[1:] if i <= pivot]
    great = [i for i in arr[1:] if i > pivot]

    return quick_sort(less) + [pivot] + quick_sort(great)
