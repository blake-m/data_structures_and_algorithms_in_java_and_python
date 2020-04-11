"""My implementation of binary search algorithm.

To simplify the functions work with integers only. An assumption
is made that the arrays provided are sorted.

There are two versions:
- iterative
- recursive
"""
from typing import Sequence

import logging

logging.basicConfig(level=logging.DEBUG)


def iterative_binary_search(array: Sequence[int], sought: int) -> int:
    """Returns an index of the element searched for in and ordered array.

    In case the element is not in the array, returns -1.
    """
    if not array:
        return -1

    left_boundary = 0
    right_boundary = len(array) - 1

    while right_boundary >= left_boundary:
        logging.debug(f'Left boundary is currently: {left_boundary}')
        logging.debug(f'Right boundary is currently: {right_boundary}')

        middle_index = left_boundary + (right_boundary - left_boundary) // 2
        middle_element = array[middle_index]

        if middle_element == sought:
            return middle_index

        if middle_element > sought:
            right_boundary = middle_index - 1
        else:
            left_boundary = middle_index + 1
    return -1


def recursive_binary_search(array: Sequence[int],
                            sought: int,
                            left_boundary: int = 0,
                            right_boundary: int = -1) -> int:
    """Returns an index of the element searched for in and ordered array.

    In case the element is not in the array, returns -1.
    """
    if not array:
        return -1

    if right_boundary == -1:
        right_boundary = len(array) - 1
    logging.debug(f'Left boundary is currently: {left_boundary}')
    logging.debug(f'Right boundary is currently: {right_boundary}')

    if right_boundary >= left_boundary:
        middle_index = left_boundary + (right_boundary - left_boundary) // 2
        middle_element = array[middle_index]
        if middle_element == sought:
            return middle_index

        if middle_element > sought:
            right_boundary = middle_index
            return recursive_binary_search(array, sought, left_boundary - 1,
                                           right_boundary)

        else:
            left_boundary = middle_index
            return recursive_binary_search(array, sought, left_boundary + 1,
                                           right_boundary)
    return -1
