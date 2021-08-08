import unittest
from doubly_linked_list_pkg.doubly_linked_list import DoublyLinkedList
from doubly_linked_list_pkg.node import Node

class DoublyLinkedListTest(unittest.TestCase):

    def test_append_front(self):
        doublyLinkedList = DoublyLinkedList()
        node = Node("1")
        doublyLinkedList.append_front(node)

        self.assertEqual(doublyLinkedList.head, node);