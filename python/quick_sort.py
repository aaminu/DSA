""" Quick Sort Algorithm based Divide and Conquer O(nlog(n))"""

from typing import Union
import random

Num = Union[int, float]


def quick_sort(arr: list[Num]) -> list[Num]:
    if len(arr) < 2:
        return arr
    pivot = arr.pop(random.randrange(0, len(arr)))
    less = [i for i in arr if i <= pivot]
    great = [i for i in arr if i > pivot]

    return quick_sort(less) + [pivot] + quick_sort(great)
