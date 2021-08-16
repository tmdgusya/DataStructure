class DoublyLinkedList(object):

    def __init__(self) -> None:
        self.head = None;
        self.tail = None;

    def append_front(self, node):
        if self.head == None:
            self.head = node
        if self.tail == None:
            self.tail = node
        else:
            self.head.prev = node
            node.next = self.head
            self.head = node
            node.prev = None

    def traversing_front(self, target):
        node = self.head
        count = 0;
        while node != None:
            if node == target:
                return count
            node = node.next
            count = count + 1
        return -1

    def traversing_tail(self, target):
        node = self.tail
        count = 0;
        while node != None:
            if node == target:
                return count
            node = node.prev
            count = count + 1
        return -1