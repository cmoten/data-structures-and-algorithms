from sys import int_info


class StackNode(object):
    def __init__(self, value, nxt) -> None:
        self.value = value
        self.next = nxt
        
    def __repr__(self) -> str:
        nval = self.next and self.next.value or None
        return f"[{self.value}:{repr(nval)}]"
    
class Stack(object):
    def __init__(self) -> None:
        self.top = None
        
    def push(self, obj) -> None:
        """Pushes a new value to the top of the stack"""
        node = StackNode(obj, None)
        if self.top == None:
            self.top = node
        else:
            node.next = self.top
            self.top = node
            
    def pop(self):
        """Pops the value that is currently on the top of the stack"""
        if self.top == None:
            return None
        else:
            node = self.top
            self.top = node.next
        return node.value
        
    def first(self):
        """Returns a reference to the first item, does not remove."""
        return self.top != None and self.top.value or None
            
    def count(self) -> int:
        node = self.top
        count = 0
        while node:
            count += 1
            node = node.next
        return count
    
    def dump(self, mark='----'):
        """Debugging function that dumps the contents of the stack."""
        node = self.top
        print(mark)
        while node:
            print(node, " ", end='')
            node = node.next
        print()