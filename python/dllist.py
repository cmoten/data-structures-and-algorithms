


class DoubleLinkedListNode(object):
    def __init__(self, value, nxt, prev) -> None:
        self.value = value
        self.next = nxt
        self.prev = prev
        
    def __repr__(self, nval, pval) -> str:
        nval = self.next and self.next.value or None
        pval = self.prev and self.prev.value or None
        return f"[{self.value},{repr(nval)},{repr(pval)}]"
    
class DoubleLinkedList(object):
    def __init__(self) -> None:
        self.begin = None
        self.end = None
        
    def push(self, obj):
        """Appends a new value on the end of the list"""
        if self.end:
            node = DoubleLinkedListNode(obj, None, self.end)
            self.end.next = node
            self.end = node
        else:
            node = DoubleLinkedListNode(obj, None, None)
            self.begin = node
            self.end = self.begin
        
    def pop(self):
        """Removes the last item and returns it"""
        if self.begin == None:
            return None
        elif self.end == self.begin:
            node = self.begin
            self.begin = self.end = None
            return node.value
        else:
            node = self.end
            self.end = node.prev
            self.end.next = None
            return node.value
            
        
    def shift(self, obj):
       """Actually just another name for push""" 
       node = DoubleLinkedListNode(obj, None, None)
       if self.begin == None:
           self.begin = node
           self.end = self.begin
       else:
           self.begin.prev = node
           node.next = self.begin
           self.begin = node
        
       
       
    def unshift(self):
        """Removes the first item (from begin) and returns it"""
        if self.begin == None:
            return None
        node = self.begin
        if self.begin == self.end:
            self.begin = self.end = None
        else:
            self.begin = node.next
            self.begin.prev = None
        return node.value
        
        
    def detach_node(self, node):
        """You'll need to use this operation sometimes, but mostly inside remove().
        It should take a node, and detach it from the list, whether the node is at
        the front, end, or in the middle."""
        if node == self.end:
            self.pop()
        elif node == self.begin:
            self.unshift()
        else:
            prev = node.prev
            nxt = node.next
            prev.next = nxt
            nxt.prev = prev
        
    def remove(self, obj):
        """Finds a matching item and removes it from the list."""
        node = self.begin
        count = 0
        while node:
            if node.value == obj:
                self.detach_node(node)
                return count
            else:
                count += 1
                node = node.next
        return -1
        
        
    def first(self):
        """Returns a *reference* to the first item, does not remove."""
        return self.begin and self.begin.value or None
    
    def last(self):
        """Returns a reference to the last item, does not remove."""
        return self.end and self.end.value or None
    
    def count(self):
        """Counts the nujber of elements in the list."""
        node = self.begin
        count = 0
        while node:
            node = node.next
            count += 1
        return count
        
    def get(self, index):
        """Get the value at index."""
        if(index < 0) or (index >= self.count()):
            return None
        counter = 0
        node = self.begin
        while counter != index:
            node = node.next
            counter += 1
        return node.value
            
        
    def dump(self, mark='----'):
        """Debugging function that dumps the contents of the list."""
        node = self.begin
        print(mark)
        while node:
            print(node, " ", end='')
            node = node.next
        print()