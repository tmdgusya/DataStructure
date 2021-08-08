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
