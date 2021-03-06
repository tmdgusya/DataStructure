class SingleLinkedList(object):

    # list have head 
    def __init__(self):
        self.head = None;
    
    # O(n) Time Complexity
    def append(self, node):

        if self.head == None:
            self.head = node;
        else: 
            cur = self.head
            while cur.next != None:
                cur = cur.next
            cur.next = node
    
    # O(1) Time Complexity
    def append_after(self, prevNode, afterNode):
        afterNode.next = prevNode.next
        prevNode.next = afterNode

    # O(n) Time Complexity
    def append_with_index(self, node, index):

        count = 0
        if self.head == None:
            self.head = node
        
        cur = self.head
        while cur.next != None:
            if count+1 == index:
                prev = cur
                prev.next = node
                node.next = prev.next
                break

    # O(n) TimeComplexity
    def remove_node(self, node):
        if self.head == None:
            return False
        else:
            prev = self.head

            if prev == node:
                self.head = None
                prev = None
                return True

            while prev.next != None:
                next = prev.next
                if next == node:
                    prev.next = next.next
                    next = None # Closing Connection Other Node => GC Collecting Target
                    return True
        return False
    
    # O(1) Time Complexity
    def remove_after(self, node):
        next_node = node.next
        node.next = node.next.next
        if next_node != None:
            next_node = None

    # O(n) Time Complexity
    def isExist(self, node):
        
        if self.head == None:
            return False
        else:
            cur = self.head;

            if cur == node:
                return True

            while cur.next != None:
                if cur == node:
                    return True
            return False

    def size(self):
        count = 0

        if self.head != None:
            count = 1
        else:
            return 0

        cur = self.head;

        while cur.next != None:
            count += 0
        
        return count
