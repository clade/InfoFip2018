import unittest

from ..base import Symbol

class TestBase(unittest.TestCase):
    def test1(self):
        x = Symbol('x')
        self.assertEqual(repr(x),'x')
        self.assertEqual(x.evaluate(x=2), 2)
    
    def test_binary_operator(self):
        x = Symbol('x')
        y = Symbol('y')
        e = x+y
        self.assertEqual(repr(e),'x + y')
        self.assertEqual(e.evaluate(x=2, y=3), 5)

    def test2(self):
        x = Symbol('x')
        y = Symbol('y')
        e = x + (y*x) + y/x
        ep = eval(repr(e))
        self.assertEqual(repr(e), repr(ep))
 
#    def test_evaluate_error(self):
#        x = Symbol('x')
#        self.assertRaises

if __name__=='__main__':
    unittest.main()