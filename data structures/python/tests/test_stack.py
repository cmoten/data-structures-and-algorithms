import unittest


import unittest
from stack import *

class TestStack(unittest.TestCase):
    def test_push(self):
        colors = Stack()
        colors.push("Pthalo Blue")
        self.assertEqual(colors.count(), 1)
        colors.push("Ultramarine Blue")
        self.assertEqual(colors.count(), 2)
        
    def test_pop(self):
        colors = Stack()
        colors.push("Magenta")
        colors.push("Alizarin")
        self.assertEqual(colors.pop(), "Alizarin")
        self.assertEqual(colors.pop(), "Magenta")
        self.assertEqual(colors.pop(), None)
        
    def test_first(self):
        colors = Stack()
        colors.push("Cadmium Yellow Light")
        self.assertEqual(colors.first(), "Cadmium Yellow Light")
        colors.push("Hansa Yellow")
        self.assertEqual(colors.first(), "Hansa Yellow")
        colors.push("Pthalo Green")
        self.assertEqual(colors.first(), "Pthalo Green")        
                              


if __name__ == '__main__':
    unittest.main()
