""" Selection Sort Algorithm O(n^2) """

from typing import Union

Num = Union[int, float]


def find_smallest_index(arr: list[Num]) -> int:
    smallest = arr[0]
    smallest_index = 0
    for index in range(1, len(arr)):
        if smallest > arr[index]:
            smallest_index = index
            smallest = arr[index]
    return smallest_index


def selection_sort(arr: list[Num]) -> list[Num]:
    new_array = []
    for index in range(len(arr)):
        smallest = find_smallest_index(arr)
        new_array.append(arr.pop(smallest))
    return new_array
