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

    # O(n) Time Complexity
    def isExist(self, node):
        
        if self.head == None:
            return False
        else:
            cur = self.head;
            while cur.next != None:
                if cur == node:
                    return True
            return False
