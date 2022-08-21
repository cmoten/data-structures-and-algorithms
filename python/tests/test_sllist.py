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
        
    def test_first(self):
        colors = SingleLinkedList()
        colors.push("Cadmium Red Light")
        self.assertEqual(colors.first(), "Cadmium Red Light")
        colors.push("Hansa Yellow")
        self.assertEqual(colors.first(), "Cadmium Red Light")
        colors.shift("Pthalo Green")
        self.assertEqual(colors.first(), "Pthalo Green")
        
    def test_last(self):
        colors = SingleLinkedList()
        colors.push("Cadmium Red Light")
        self.assertEqual(colors.last(), "Cadmium Red Light")
        colors.push("Hansa Yellow")
        self.assertEqual(colors.last(), "Hansa Yellow")
        colors.shift("Pthalo Green")
        self.assertEqual(colors.last(), "Hansa Yellow")
        
    def test_get(self):
        colors = SingleLinkedList()
        colors.push("Vermillion")
        self.assertEqual(colors.get(0), "Vermillion")
        colors.push("Sap Green")
        self.assertEqual(colors.get(0), "Vermillion")
        self.assertEqual(colors.get(1), "Sap Green")
        colors.push("Cadmium Yellow Light")
        self.assertEqual(colors.get(0), "Vermillion")
        self.assertEqual(colors.get(1), "Sap Green")
        self.assertEqual(colors.get(2), "Cadmium Yellow Light")
        self.assertEqual(colors.pop(), "Cadmium Yellow Light")
        self.assertEqual(colors.get(0), "Vermillion")
        self.assertEqual(colors.get(1), "Sap Green")
        self.assertEqual(colors.get(2), None)
        colors.pop()
        self.assertEqual(colors.get(0), "Vermillion")
        colors.pop()
        self.assertEqual(colors.get(0), None)

        
        
if __name__ == '__main__':
    unittest.main()