"""My implementation of Merge Sort algorithm.

An assumption is made that the arrays provided are lists of integers.
"""
from typing import List, Tuple

import logging

logging.basicConfig(level=logging.DEBUG)


def split_list_into_halfs(array: List[int]) -> Tuple[List[int], List[int]]:
    array_length = len(array)

    middle = array_length // 2
    return array[0:middle], array[middle:]


def merge(left: List[int], right: List[int]) -> List[int]:
    aux_list = []
    while left or right:
        if left and right:
            if left[0] >= right[0]:
                aux_list.append(right.pop(0))
            else:
                aux_list.append(left.pop(0))

        if left and not right:
            for elem in left:
                aux_list.append(left.pop(0))

        if right and not left:
            for elem in right:
                aux_list.append(right.pop(0))

    logging.debug(aux_list)
    return aux_list


def merge_sort(array: List[int]) -> List[int]:
    logging.debug(array)
    if len(array) > 1:
        sub_array_1, sub_array_2 = split_list_into_halfs(array)
        left = merge_sort(sub_array_1)
        right = merge_sort(sub_array_2)
        return merge(left, right)
    return array
