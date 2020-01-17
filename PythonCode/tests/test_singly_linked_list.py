import unittest

from singly_linked_list import SinglyLinkedList


class TestSinglyLinkedListNode(unittest.TestCase):
    def setUp(self):
        self.node = SinglyLinkedList._SinglyLinkedList__Node('Some Data')
        self.another_node = SinglyLinkedList._SinglyLinkedList__Node('Some Data', self.node)

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

    def test_add_first_with_item_data_equal_to_none(self):
        self.sll.add_first(None)
        self.assertIsNone(self.sll._SinglyLinkedList__head.data)
        self.assertIsNotNone(self.sll._SinglyLinkedList__head)

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

    def test_remove_first_throws_exception_with_empty_list(self):
        with self.assertRaises(IndexError):
            self.sll.remove_first()

    def test_remove_last_throws_exception_with_empty_list(self):
        with self.assertRaises(IndexError):
            self.sll.remove_last()

    def test_remove_at_index_throws_exception_with_empty_list(self):
        with self.assertRaises(IndexError):
            self.sll.remove_at_index(0)

    def test_insert_item_at_with_empty_list(self):
        self.sll.insert_item_at("Some item", 0)

    def test_insert_item_at_throws_exception_with_wrong_input(self):
        with self.assertRaises(IndexError):
            self.sll.insert_item_at(1, 2441)

    def test_initialization_with_first_element(self):
        sll = SinglyLinkedList(5.1241)
        self.assertEqual(sll._SinglyLinkedList__head.data, 5.1241)

    def test_check_last(self):
        self.assertIsNone(self.sll.check_last())


class TestSinglyLinkedListWithItems(unittest.TestCase):
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

    def test_clear_no_items_are_left_in_the_list(self):
        self.sll.clear()
        self.assertIsNone(self.sll._SinglyLinkedList__head)
        self.assertIsNone(self.sll._SinglyLinkedList__tail)

    def test__getitem__(self):
        for i in range(self.sll.size):
            self.assertEqual(self.sll[i], "Some Data - Node " + str(i))

    def test__getitem__raises_index_error(self):
        with self.assertRaises(IndexError):
            self.sll[25]

    def test_check_at_index(self):
        for i in range(self.sll.size):
            self.assertEqual(self.sll.check_at_index(i), "Some Data - Node " + str(i))

    def test_check_first(self):
        self.assertEqual(self.sll.check_first(), self.sll._SinglyLinkedList__head.data)
        self.assertEqual(self.sll.check_first(), "Some Data - Node 0")

    def test_check_last(self):
        self.assertEqual(self.sll.check_last(), self.sll._SinglyLinkedList__tail.data)
        self.assertEqual(self.sll.check_last(), "Some Data - Node 9")

    def test_remove_first_removes_first_item(self):
        self.assertEqual(self.sll.remove_first(), "Some Data - Node 0")
        self.assertEqual(self.sll._SinglyLinkedList__head.data, "Some Data - Node 1")

    def test_remove_first_decreases_size_by_one(self):
        start_size = self.sll.size
        self.sll.remove_first()
        self.assertEqual(self.sll.size, start_size-1)

    def test_remove_last_removes_last_item(self):
        self.assertEqual(self.sll.remove_last(), "Some Data - Node 9")
        self.assertEqual(self.sll._SinglyLinkedList__tail.data, "Some Data - Node 8")

    def test_remove_last_decreases_size_by_one(self):
        start_size = self.sll.size
        self.sll.remove_last()
        self.assertEqual(self.sll.size, start_size-1)

    def test_remove_at_index(self):
        self.assertEqual(self.sll.remove_at_index(1), "Some Data - Node 1")
        self.assertEqual(self.sll[1], "Some Data - Node 2")

    def test_remove_at_index_decreases_size_by_one(self):
        start_size = self.sll.size
        self.sll.remove_at_index(1)
        self.assertEqual(self.sll.size, start_size-1)

    def test_insert_item_at_index_inserts_the_item(self):
        self.sll.insert_item_at("Secret Element", 1)
        self.assertEqual(self.sll[1], "Secret Element")
        self.assertEqual(self.sll[2], "Some Data - Node 1")

    def test_insert_item_at_index_increases_list_size(self):
        start_size = self.sll.size
        self.sll.insert_item_at("Secret Element", 1)
        self.assertEqual(self.sll.size, start_size + 1)

    def test_iterator(self):
        iterator = iter(self.sll)
        for i in range(self.sll.size):
            self.assertEqual(next(iterator), "Some Data - Node " + str(i))
        with self.assertRaises(StopIteration):
            next(iterator)

    def test_iterator_changes_when_item_added(self):
        iterator = iter(self.sll)
        next(iterator)
        self.sll.insert_item_at('Some Item', 1)
        self.assertEqual(next(iterator), 'Some Item')
        self.assertEqual(next(iterator), 'Some Data - Node 1')

    def test_str(self):
        string_for_comparison = "['Some Data - Node 0', 'Some Data - Node 1'"
        self.assertEqual(str(self.sll)[:43], string_for_comparison)


if __name__ == '__main__':
    unittest.main()
