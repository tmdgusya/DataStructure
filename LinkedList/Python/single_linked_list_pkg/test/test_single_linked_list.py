import unittest
from single_linked_list_pkg.node import Node
from single_linked_list_pkg.single_linked_list import SingleLinkedList

class SingleLinkedListTest(unittest.TestCase):

    def setUp(self) -> None:
        print("IN TEST METHOD", self._testMethodName)


    def test_append_func(self):
        linkedList = SingleLinkedList()

        node_one = Node("header")

        linkedList.append(node_one);
        self.assertEqual(linkedList.head, node_one);

    def test_return_ture_if_success_remove_node_in_linked_list(self):
        linkedList = SingleLinkedList()

        node_one = Node("header")

        linkedList.append(node_one);
        self.assertTrue(linkedList.remove_node(node_one));
