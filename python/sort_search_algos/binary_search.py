""" Binary Search Algorithm O(logn) """

from typing import Union

Result = Union[None, int]


def binary_search(arr: list[int], value: int) -> Result:
    lowest_index = 0
    highest_index = len(arr)-1

    while lowest_index <= highest_index:
        mid_index = (lowest_index+highest_index)//2
        if arr[mid_index] == value:
            return mid_index
        elif arr[mid_index] < value:
            lowest_index = mid_index + 1
        else:
            highest_index = mid_index - 1

    return None
