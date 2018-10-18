import unittest
import math

from ..math import sin
from ..base import Symbol

class TestMath(unittest.TestCase):
    def test_sin(self):
        x = Symbol('x')
        e = sin(x)
        self.assertEqual(e.evaluate(x=1), math.sin(1))
        self.assertEqual(repr(e), 'sin(x)')
       
if __name__=='__main__':
    unittest.main()