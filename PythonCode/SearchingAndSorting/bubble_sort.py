"""My implementation of bubble sort algorithm.

An assumption is made that the arrays provided are integers.
"""
from typing import Sequence

import logging

logging.basicConfig(level=logging.DEBUG)


def bubble_sort(array: Sequence[int]) -> Sequence[int]:
    if not array:
        return array

    logging.debug('BEGIN SORTING.')
    array_length = len(array)
    while True:
        for i in range(array_length):
            no_swaps = True

            logging.debug('Input state: {}'.format(array))

            for j in range(array_length-i-1):
                if array[j] > array[j + 1]:
                    array[j + 1], array[j] = array[j], array[j + 1]
                    no_swaps = False

            logging.debug('Output state: {}'.format(array))

            if no_swaps:
                logging.debug('SORTING FINISHED.\n')
                return array
