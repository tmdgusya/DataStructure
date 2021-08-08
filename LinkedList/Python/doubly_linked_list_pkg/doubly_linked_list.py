class DoublyLinkedList(object):

    def __init__(self) -> None:
        self.head = None;
        self.tail = None;

    def append_front(self, node):
        if self.head == None:
            node.next = self.head
            self.head = node
            node.prev = None