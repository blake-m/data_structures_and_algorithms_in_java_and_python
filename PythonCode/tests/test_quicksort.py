import logging
import unittest

import numpy as np

from SearchingAndSorting.quicksort import quicksort

# Uncomment to disable debugging messages
# logging.disable(logging.CRITICAL)


class TestQuickSort(unittest.TestCase):
    def test_quicksort_returns_sorted_array(self):
        test_arrays = [
            [6, 5, 4, 3, 2, 1, 0, -1],
            [124, 32, 124, 32, 225, 756, 87, -125],
            [64, 34, 25, 12, 22, 11, 90],
        ]

        correct_answers = [
            [-1, 0, 1, 2, 3, 4, 5, 6],
            [-125, 32, 32, 87, 124, 124, 225, 756],
            [11, 12, 22, 25, 34, 64, 90],
        ]

        for test, answer in zip(test_arrays, correct_answers):
            self.assertEqual(answer, quicksort(test))


if __name__ == '__main__':
    unittest.main()
