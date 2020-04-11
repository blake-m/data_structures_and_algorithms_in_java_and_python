import logging

import unittest

from SearchingAndSorting import binary_search as bs

# Uncomment to disable debugging messages
logging.disable(logging.CRITICAL)


class TestIterativeBinarySearch(unittest.TestCase):
    def test_binary_search_returns_index_with_small_sought_element(self):
        test_array = list(range(50))
        sought = 3
        self.assertEqual(
            sought, bs.iterative_binary_search(test_array, sought))

    def test_binary_search_returns_index_with_big_sought_element(self):
        test_array = list(range(50))
        sought = 46
        self.assertEqual(
            sought, bs.iterative_binary_search(test_array, sought))

    def test_binary_search_returns_index_with_sougt_element_in_middle(self):
        test_array = list(range(50))
        sought = 24
        self.assertEqual(
            sought, bs.iterative_binary_search(test_array, sought))

    def test_binary_search_returns_minus_one_when_element_not_found(self):
        test_array = list(range(50))
        sought = 501
        self.assertEqual(-1, bs.iterative_binary_search(test_array, sought))

    def test_binary_search_returns_minus_one_with_an_empty_array(self):
        test_array = []
        sought = 501
        self.assertEqual(-1, bs.iterative_binary_search(test_array, sought))


class TestRecursiveBinarySearch(unittest.TestCase):
    def test_binary_search_returns_index_with_small_sought_element(self):
        test_array = list(range(50))
        sought = 3
        self.assertEqual(
            sought, bs.recursive_binary_search(test_array, sought))

    def test_binary_search_returns_index_with_big_sought_element(self):
        test_array = list(range(50))
        sought = 46
        self.assertEqual(
            sought, bs.recursive_binary_search(test_array, sought))

    def test_binary_search_returns_index_with_sougt_element_in_middle(self):
        test_array = list(range(50))
        sought = 24
        self.assertEqual(
            sought, bs.recursive_binary_search(test_array, sought))

    def test_binary_search_returns_minus_one_when_element_not_found(self):
        test_array = list(range(50))
        sought = 501
        self.assertEqual(-1, bs.recursive_binary_search(test_array, sought))

    def test_binary_search_returns_minus_one_with_an_empty_array(self):
        test_array = []
        sought = 501
        self.assertEqual(-1, bs.recursive_binary_search(test_array, sought))


if __name__ == '__main__':
    unittest.main()
