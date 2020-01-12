import unittest

from singly_linked_list import SinglyLinkedList


class TestSinglyLinkedListNode(unittest.TestCase):
    def setUp(self) -> None:
        self.node = SinglyLinkedList.Node('Some Data')
        self.another_node = SinglyLinkedList.Node('Some Data', self.node)

    def test__str__(self):
        self.assertEqual(str(self.node), 'Some Data')

    def test_link_with_another_node(self):
        self.assertEqual(self.another_node.data, self.another_node.next.data)


class TestSinglyLinkedList(unittest.TestCase):
    def setUp(self) -> None:
        self.sll = SinglyLinkedList()

    def test_size(self):
        self.assertEqual(self.sll.size, 0)

    def test_size_cannot_be_changed(self):
        with self.assertRaises(AttributeError):
            self.sll.size = 53

    def test_is_empty(self):
        self.assertTrue(self.sll.size == 0)

    def add_first(self):
        self.sll.add_first()
        pass


# Remember about this flashcard: Handling Expected Failures


if __name__ == '__main__':
    unittest.main()
