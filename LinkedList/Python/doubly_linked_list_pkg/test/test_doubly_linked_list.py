import unittest
from doubly_linked_list_pkg.doubly_linked_list import DoublyLinkedList
from doubly_linked_list_pkg.node import Node

class DoublyLinkedListTest(unittest.TestCase):

    def test_append_front(self):
        doublyLinkedList = DoublyLinkedList()
        node = Node("1")
        doublyLinkedList.append_front(node)

        self.assertEqual(doublyLinkedList.head, node);

    def test_append_front_if_exist_head_node(self):
        doubly_linked_list = DoublyLinkedList()
        head_node = Node("head")
        new_node = Node("My Position")
        doubly_linked_list.append_front(head_node)
        doubly_linked_list.append_front(new_node)

        self.assertEqual(doubly_linked_list.head, new_node)
        self.assertEqual(new_node.next, head_node)