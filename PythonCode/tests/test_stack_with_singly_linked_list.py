import unittest

from stack_with_singly_linked_list import Stack


class TestStack(unittest.TestCase):
    def setUp(self):
        self.stack = Stack()

    def test_get_size(self):
        self.assertEqual(self.stack.get_size(), 0)
        self.stack.push_element_on_top(1241)
        self.assertEqual(self.stack.get_size(), 1)

    def test_is_empty(self):
        self.assertEqual(self.stack.is_empty(), True)

    def test_push_element_on_top(self):
        self.stack.push_element_on_top(1241)
        self.assertEqual(self.stack._Stack__stack_list.check_first(), 1241)

    def test_pop_element_from_top(self):
        self.stack.push_element_on_top(1241)
        self.assertEqual(self.stack.pop_element_from_top(), 1241)

    def test_pop_element_from_top_reduces_size_by_one(self):
        self.stack.push_element_on_top(1241)
        size = self.stack.get_size()
        self.stack.pop_element_from_top()
        self.assertEqual(self.stack.get_size(), size-1)

    def test_peek_element_from_top(self):
        for i in range(5):
            self.stack.push_element_on_top(i)
        self.assertEqual(self.stack.peek_element_from_top(), 4)

    def test_initialization_with_first_element(self):
        first_element = 125.23
        stack = Stack(first_element)
        self.assertEqual(stack.get_size(), 1)

    def test__str__(self):
        for i in range(5):
            self.stack.push_element_on_top(i)
        self.assertEqual(str(self.stack), "[0, 1, 2, 3, 4]")


if __name__ == '__main__':
    unittest.main()
