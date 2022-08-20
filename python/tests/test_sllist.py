import unittest
from sllist import *

class TestSingleLinkedList(unittest.TestCase):
    def test_push(self):
        colors = SingleLinkedList()
        colors.push("Pthalo Blue")
        self.assertEqual(colors.count(), 1)
        colors.push("Ultramarine Blue")
        self.assertEqual(colors.count(), 2)
        
    def test_pop(self):
        colors = SingleLinkedList()
        colors.push("Magenta")
        colors.push("Alizarin")
        self.assertEqual(colors.pop(), "Alizarin")
        self.assertEqual(colors.pop(), "Magenta")
        self.assertEqual(colors.pop(), None)
        
    def test_unshif(self):
        colors = SingleLinkedList()
        colors.push("Viridian")
        colors.push("Sap Green")
        colors.push("Van Dyke")
        self.assertEqual(colors.unshift(), "Viridian")
        self.assertEqual(colors.unshift(), "Sap Green")
        self.assertEqual(colors.unshift(), "Van Dyke")
        self.assertEqual(colors.unshift(), None)
        
    def test_shift(self):
        colors = SingleLinkedList()
        colors.shift("Cadmium Orange")
        self.assertEqual(colors.count(), 1)
        colors.shift("Carbazole Violet")
        self.assertEqual(colors.count(), 2)
        self.assertEqual(colors.pop(), "Cadmium Orange")
        self.assertEqual(colors.count(), 1)
        self.assertEqual(colors.pop(), "Carbazole Violet")
        self.assertEqual(colors.count(), 0)
        
if __name__ == '__main__':
    unittest.main()