import unittest

from singly_linked_list import SinglyLinkedList


class TestSinglyLinkedListNode(unittest.TestCase):
    def setUp(self):
        self.node = SinglyLinkedList.Node('Some Data')
        self.another_node = SinglyLinkedList.Node('Some Data', self.node)

    def test__str__(self):
        self.assertEqual(str(self.node), 'Some Data')

    def test_link_with_another_node(self):
        self.assertEqual(self.another_node.data, self.another_node.next.data)


class TestSinglyLinkedListEmpty(unittest.TestCase):
    def setUp(self):
        self.sll = SinglyLinkedList()

    def test_size(self):
        self.assertEqual(self.sll.size, 0)

    def test_size_cannot_be_changed(self):
        with self.assertRaises(AttributeError):
            self.sll.size = 53

    def test_is_empty(self):
        self.assertTrue(self.sll.size == 0)

    def test_add_first(self):
        self.sll.add_first("Some data")
        self.assertEqual(self.sll._SinglyLinkedList__head.data, "Some data")

    def test_add_first_tail_head_are_same(self):
        self.sll.add_first("Some data")
        self.assertEqual(self.sll._SinglyLinkedList__head, self.sll._SinglyLinkedList__tail)

    def test_add_first_size_increases(self):
        self.sll.add_first("Some data")
        self.assertEqual(self.sll.size, 1)

    def test_add_last(self):
        self.sll.add_last("Some data")
        self.assertEqual(self.sll._SinglyLinkedList__head.data, "Some data")

    def test_add_last_tail_head_are_same(self):
        self.sll.add_last("Some data")
        self.assertEqual(self.sll._SinglyLinkedList__head, self.sll._SinglyLinkedList__tail)

    def test_add_last_size_increases(self):
        self.sll.add_last("Some data")
        self.assertEqual(self.sll.size, 1)

    def test__getitem__raises_index_error(self):
        with self.assertRaises(IndexError):
            var = self.sll[0]
        with self.assertRaises(IndexError):
            var = self.sll[5]


class TestSinglyLinkedListWithElements(unittest.TestCase):
    def setUp(self):
        self.sll = SinglyLinkedList()
        for i in range(10):
            data = 'Some Data - Node ' + str(i)
            self.sll.add_last(data)

    def test_size(self):
        self.assertEqual(self.sll.size, 10)

    def test_is_empty(self):
        self.assertFalse(self.sll.size == 0)

    def test_add_first(self):
        self.sll.add_first("first")
        self.assertEqual(self.sll._SinglyLinkedList__head.data, "first")
        self.assertEqual(self.sll._SinglyLinkedList__head.next.data, "Some Data - Node 0")

    def test_add_last(self):
        self.sll.add_last("last")
        self.assertEqual(self.sll._SinglyLinkedList__tail.data, "last")

    def test_clear_size_resets_to_0(self):
        self.sll.clear()
        self.assertEqual(self.sll.size, 0)

    def test_clear_no_elements_are_left_in_the_list(self):
        self.sll.clear()
        self.assertIsNone(self.sll._SinglyLinkedList__head)
        self.assertIsNone(self.sll._SinglyLinkedList__tail)

    def test__getitem__(self):
        for i in range(self.sll.size):
            self.assertEqual(self.sll[i], "Some Data - Node " + str(i))

    def test__getitem__raises_index_error(self):
        with self.assertRaises(IndexError):
            var = self.sll[25]

    def test_check_at_index(self):
        for i in range(self.sll.size):
            self.assertEqual(self.sll.check_at_index(i), "Some Data - Node " + str(i))


if __name__ == '__main__':
    unittest.main()
