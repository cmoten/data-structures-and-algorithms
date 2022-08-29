import unittest
from dllist import *

class TestDoubleLinkedList(unittest.TestCase):
    def test_push(self):
        colors = DoubleLinkedList()
        colors.push("Pthalo Blue")
        self.assertEqual(colors.count(), 1)
        colors.push("Ultramarine Blue")
        self.assertEqual(colors.count(), 2)
        
    def test_pop(self):
        colors = DoubleLinkedList()
        colors.push("Magenta")
        colors.push("Alizarin")
        self.assertEqual(colors.pop(), "Alizarin")
        self.assertEqual(colors.count(), 1)
        self.assertEqual(colors.pop(), "Magenta")
        self.assertEqual(colors.pop(), None)
        
    def test_shift(self):
        colors = DoubleLinkedList()
        colors.shift("Cadmium Orange")
        self.assertEqual(colors.count(), 1)
        colors.shift("Carbazole Violet")
        self.assertEqual(colors.count(), 2)
        self.assertEqual(colors.pop(), "Cadmium Orange")
        self.assertEqual(colors.count(), 1)
        self.assertEqual(colors.pop(), "Carbazole Violet")
        self.assertEqual(colors.count(), 0)
        
    def test_unshift(self):
        colors = DoubleLinkedList()
        colors.push("Viridian")
        colors.push("Sap Green")
        colors.push("Van Dyke")
        self.assertEqual(colors.unshift(), "Viridian")
        self.assertEqual(colors.unshift(), "Sap Green")
        self.assertEqual(colors.unshift(), "Van Dyke")
        self.assertEqual(colors.unshift(), None)
        
    def test_remove(self):
        colors = DoubleLinkedList()
        colors.push("Cobalt")
        colors.push("Zinc White")
        colors.push("Nickel Yellow")
        colors.push("Perinone")
        self.assertEqual(colors.remove("Cobalt"), 0)
        self.assertEqual(colors.remove("Perinone"), 2)
        self.assertEqual(colors.remove("Nickel Yellow"), 1)
        self.assertEqual(colors.remove("Zinc White"), 0)
        
    def test_first(self):
        colors = DoubleLinkedList()
        colors.push("Cadmium Red Light")
        self.assertEqual(colors.first(), "Cadmium Red Light")
        colors.push("Hansa Yellow")
        self.assertEqual(colors.first(), "Cadmium Red Light")
        colors.shift("Pthalo Green")
        self.assertEqual(colors.first(), "Pthalo Green")
        
    def test_last(self):
        colors = DoubleLinkedList()
        colors.push("Cadmium Red Light")
        self.assertEqual(colors.last(), "Cadmium Red Light")
        colors.push("Hansa Yellow")
        self.assertEqual(colors.last(), "Hansa Yellow")
        colors.shift("Pthalo Green")
        self.assertEqual(colors.last(), "Hansa Yellow")
        
    def test_get(self):
        colors = DoubleLinkedList()
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