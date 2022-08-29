class QueueNode(object):
    def __init__(self, value, nxt, prev) -> None:
        self.value = value
        self.next = nxt
        self.prev = prev
        
    def __repr__(self) -> str:
        nval = self.next and self.next.value or None
        pval = self.prev and self.prev.value or None
        return f"[{self.value},{repr(nval)}, {repr(pval)}]"
    
class Queue(object):
    def __init__(self) -> None:
        self.tail = None
        self.head = None
        
    def shift(self, obj):
        """Shifts a new element onto the back of the queue"""
        if self.tail:
            node = QueueNode(obj, None, self.tail)
            self.tail.next = node
            self.tail = node
        else:
            self.head = QueueNode(obj, None, None)
            self.tail = self.head
            
    def unshift(self):
        """Removes the element that is first in the queue."""
        if self.head:
            node = self.head
            
            if self.head == self.tail:
                self.head = None
                self.tail = None
            else:
                self.head = node.next
                self.head.prev = None
            return node.value
        
        return None
    
    def first(self):
        """Returns a *reference* to the first item, does not remove."""
        return self.head and self.head.value or None
    
    def empty(self):
        """Indicates if the queue is empty"""
        return self.head == None
            
    def count(self) -> int:
        node = self.head
        counter = 0
        while node:
            counter += 1
            node = node.next
        return counter
    
    