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
    
    def test_append_node_to_middle_func(self):
        linkedList = SingleLinkedList()

        node_one = Node("One")
        node_two = Node("Two")
        node_thr = Node("Thr")

        linkedList.append(node_one)
        linkedList.append(node_thr)
        linkedList.append_with_index(node_two, 1)

        self.assertEqual(node_one.next, node_two)

    def test_append_after(self):
        linkedList = SingleLinkedList()

        node_one = Node("One")
        node_two = Node("Two")
        node_thr = Node("Thr")

        linkedList.append(node_one)
        linkedList.append(node_thr)
        linkedList.append_after(node_one, node_two)

        self.assertEqual(node_two.next, node_thr);
    
    def test_insert_head_if_not_exist_append_with_index(self):
        linkedList = SingleLinkedList()

        node_one = Node("header")

        linkedList.append(node_one)
        self.assertEqual(linkedList.head, node_one)


    def test_return_ture_if_success_remove_node_in_linked_list(self):
        linkedList = SingleLinkedList()

        node_one = Node("header")

        linkedList.append(node_one);
        self.assertTrue(linkedList.remove_node(node_one));

    def test_return_false_if_fail_remove_node_in_linked_list(self):
        linkedList = SingleLinkedList()

        node_one = Node("header")
        other_node = Node("Other Node")

        linkedList.append(other_node)
        self.assertFalse(linkedList.remove_node(node_one))

    def test_return_true_if_exist_node_in_linked_list(self):
        linkedList = SingleLinkedList()

        node_one = Node("this")

        linkedList.append(node_one)
        self.assertTrue(linkedList.isExist(node_one))

    def test_return_false_if_not_exist_node_in_linked_list(self):
        linkedList = SingleLinkedList()

        node_one = Node("this")
        node_other = Node("Other")
        linkedList.append(node_one)

        self.assertFalse(linkedList.isExist(node_other));
    
    def test_get_correct_size_linked_list(self):

        linkedList = SingleLinkedList()

        node_one = Node("This")

        linkedList.append(node_one);

        self.assertEqual(linkedList.size(), 1);

    def test_get_size_return_zero_if_not_exist_node_in_linked_list(self):
        linkedList = SingleLinkedList()

        self.assertEqual(linkedList.size(), 0);