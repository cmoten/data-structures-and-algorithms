from tabnanny import check


class SingleLinkedListNode(object):
    def __init__(self, value, nxt) -> None:
        self.value = value
        self.next = nxt
        
    def __repr__(self) -> str:
        nval = self.next and self.next.value or None
        return f"[{self.value}:{repr(nval)}]"
    
class SingleLinkedList(object):
    def __init__(self) -> None:
        self.begin = None
        self.end = None
        
    def push(self, obj):
        """Appends a new value on the end of the list"""
        node = SingleLinkedListNode(obj, None)
        if self.begin == None:
            self.begin = node
            self.end = self.begin
            
        else:
            self.end.next = node
            self.end = node
            assert self.begin != self.end
            
        assert self.end.next == None
        
    def pop(self):
        """Removes the last item and returns it"""
        if self.begin == None:
            return None
        elif self.end == self.begin:
            node = self.begin
            self.end = self.begin = None
            return node.value
        else:
            node = self.begin
            while node.next != self.end:
                node = node.next
            assert self.end != node
            poppedNode = node.next.value
            node.next = None
            self.end = node
            return poppedNode
        
    def shift(self, obj):
        """Another name for push."""
        node = SingleLinkedListNode(obj, None)
        if self.begin == None:
            self.begin = node
            self.end = self.begin
        else:
            node.next = self.begin
            self.begin = node
        assert self.end.next == None
        

    def unshift(self):
        """Removes the first item and returns it."""
        if self.begin == None:
            return None
        elif self.end == self.begin:
            node = self.begin
            self.end = None
            self.begin = None
            assert self.begin == None and self.end == None
            return node.value
        else:
            node = self.begin
            self.begin = self.begin.next
            return node.value

    def remove(self, obj):
        """Finds a matching item and removes it from the list."""
        index = 0
        checkValue = SingleLinkedListNode(obj, None)
        if self.begin == None:
            index -= 1
            return index
        if self.begin.value == checkValue.value:
            index = 0
            self.unshift()
            return index
        if self.end.value == checkValue.value:
            index = self.count() - 1
            self.pop()
            return index
        currentNode = self.begin
        while currentNode.next != self.end:
            prevNode = currentNode
            currentNode = currentNode.next
            index += 1
            testValue = self.get(index)
            if testValue == checkValue.value:
                prevNode.next = currentNode.next
                return index       

    def first(self):
        """Returns a *reference* to the first item, does not remove."""
        return self.begin.value

    def last(self):
        """Returns a reference to the last item, does not remove."""
        return self.end.value
        
    def count(self)->int:
        """Counts the number of elements in the list"""
        node = self.begin
        count = 0
        while node:
            count += 1
            node = node.next
            
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

    def dump(self, mark):
        """Debugging function that dumps the contents of the list."""
        node = self.begin
        while node:
            print(repr(node))
            node = node.next
        