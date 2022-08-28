import unittest
from queue import *

class TestQueue(unittest.TestCase):
    def test_shift(self):
        colors = Queue()
        colors.shift("Pthalo Blue")
        self.assertEqual(colors.count(), 1)
        colors.shift("Ultramarine Blue")
        self.assertEqual(colors.count(), 2)
        
    def test_unshift(self):
        colors = Queue()
        colors.shift("Magenta")
        colors.shift("Alizarin")
        self.assertEqual(colors.unshift(), "Magenta")
        self.assertEqual(colors.unshift(), "Alizarin")
        self.assertEqual(colors.unshift(), None)
        
    def test_first(self):
        colors = Queue()
        colors.shift("Cadmium Red Light")
        self.assertEqual(colors.first(), "Cadmium Red Light")
        colors.shift("Hansa Yellow")
        self.assertEqual(colors.first(), "Cadmium Red Light")
        colors.shift("Pthalo Green")
        self.assertEqual(colors.first(), "Cadmium Red Light")