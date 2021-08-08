import unittest
from single_linked_list_pkg.node import Node
from single_linked_list_pkg.single_linked_list import SingleLinkedList

class SingleLinkedListTest(unittest.TestCase):


    def test_append_func(self):
        linkedList = SingleLinkedList()

        node_one = Node("header")

        linkedList.append(node_one);
        self.assertEqual(linkedList.head, node_one);
