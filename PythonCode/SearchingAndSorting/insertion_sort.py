"""My implementation of insertion sort algorithm.

An assumption is made that the arrays provided are integers.
"""
from typing import List

import logging

logging.basicConfig(level=logging.DEBUG)


def insertion_sort(array: List[int]) -> List[int]:
    array_length = len(array)
    for i in range(1, array_length):
        current_element = array[i]
        j = i - 1
        while j >= 0 and current_element < array[j]:
            array[j+1] = array[j]
            j -= 1
        array[j + 1] = current_element
    return array
