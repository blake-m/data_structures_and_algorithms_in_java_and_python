import unittest

from singly_linked_list import Element, LinkedList
from unittest import TestCase


class TestSinglyLinkedList(TestCase):
    def test_initialize_element(self):
        element1 = Element('Value1')
        self.assertEqual(element1.value, 'Value1')
        self.assertIsNone(element1.next)

    def test_initialize_element_with_next_element(self):
        element1 = Element('Value1')
        element2 = Element('Value2')
        element1.next = element2
        self.assertEqual(element1.value, 'Value1')
        self.assertEqual(element1.next.value, 'Value2')
        self.assertIsNotNone(element1.next)

    def test_initialize_empty_linked_list(self):
        ll = LinkedList()
        self.assertIsNone(ll.head)
        self.assertEqual(ll.size, 0)

    def test_initialize_linked_list_with_an_element(self):
        element1 = Element('Value1')
        ll = LinkedList(element1)
        self.assertEqual(ll.head.value, 'Value1')
        self.assertEqual(ll.size, 1)

    def test_append_with_empty_linked_list(self):
        ll = LinkedList()
        element1 = Element('Value1')
        ll.append(element1)
        self.assertEqual(ll.head.value, 'Value1')

    def test_get_position(self):
        element1 = Element('Value1')
        ll = LinkedList(element1)
        element2 = Element('Value2')
        element3 = Element('Value3')
        element1.next = element2
        element2.next = element3
        self.assertEqual(ll.get_position(3).value, 'Value3')

    def test_append_list_with_elements(self):
        element1 = Element('Value1')
        element2 = Element('Value2')
        element3 = Element('Value3')
        ll = LinkedList(element1)
        ll.append(element2)
        ll.append(element3)
        self.assertEqual(ll.head.value, 'Value1')
        self.assertEqual(ll.get_position(2).value, 'Value2')
        self.assertEqual(ll.get_position(3).value, 'Value3')

    def test_insert_at_the_beginning(self):
        element1 = Element('Value1')
        element2 = Element('Value2')
        element3 = Element('Value3')
        ll = LinkedList(element2)
        ll.append(element3)
        ll.insert(element1, 1)
        self.assertEqual(ll.get_position(1).value, 'Value1')

    def test_insert_in_the_middle(self):
        element1 = Element('Value1')
        element2 = Element('Value2')
        element3 = Element('Value3')
        ll = LinkedList(element2)
        ll.append(element3)
        ll.insert(element1, 2)
        self.assertEqual(ll.get_position(2).value, 'Value1')

    def test_delete(self):
        element1 = Element('Value1')
        element2 = Element('Value2')
        element3 = Element('Value3')
        ll = LinkedList(element1)
        ll.append(element2)
        ll.append(element3)
        ll.delete('Value2')
        self.assertNotEqual(ll.get_position(2).value, 'Value2')


if __name__ == '__main__':
    unittest.main()
