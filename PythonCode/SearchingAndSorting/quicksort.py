"""My implementation of QuickSort algorithm.

Pivot is chosen randomly to avoid pessimistic case of Computational Complexity.
An assumption is made that the arrays provided are lists of integers.
"""
from typing import List

import logging
import random

logging.basicConfig(level=logging.DEBUG)


def partition(array: List[int], low: int, high: int) -> int:
    pivot = random.choice(range(low, high+1))
    value_at_pivot = array[pivot]

    logging.debug(f"\nWHOLE-ARRAY: {array}"
                  f"\nSUB-ARRAY: {array[low:high + 1]}"
                  f"\n\tlow: {low}, high: {high}, pivot: {pivot}, "
                  f"value at pivot: {value_at_pivot}")

    array[high], array[pivot] = array[pivot], array[high]

    border_index = low
    for i in range(low, high+1):
        if array[i] <= value_at_pivot and i != high:
            array[i], array[border_index] = array[border_index], array[i]
            border_index += 1

    array[border_index], array[high] = array[high], array[border_index]

    return border_index


def quicksort(array: List[int], low: int = 0, high: int = -1) -> List[int]:
    if high == -1:
        high = len(array) - 1
    if low < high:
        border_index = partition(array, low, high)
        quicksort(array, low, border_index - 1)
        quicksort(array, border_index + 1, high)
    return array
