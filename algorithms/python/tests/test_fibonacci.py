#run on the command line using python -m unittest tests/example_test.py

import unittest
from fibonacci_memo import fib

class TestStringMethod(unittest.TestCase):
    
    def test_fib(self):
        self.assertEqual(fib(50), 12586269025)
        self.assertEqual(fib(60), 1548008755920)
        self.assertEqual(fib(100), 354224848179261915075)
        
        
        
if __name__ == '__main__':
    unittest.main()