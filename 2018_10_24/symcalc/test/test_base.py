import unittest

from ..base import Symbol, Number

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
    def test_eq(self):
        x = Symbol('x')
        y = Symbol('y')
        xx = Symbol('x')
        self.assertEqual(x, xx)
        self.assertEqual(x+y, y+x)

    def testsimplification(self):
        x = Number(1)
        y = Number(2)
        z = Symbol('z')
        self.assertEqual((x+y).simplify(), 3)
        self.assertEqual((0+y).simplify(), y)
        self.assertEqual((x*y).simplify(), 2)

    def testdiff(self):
        x = Symbol('x')
        y = Symbol('y')
        z = Symbol('z')
        self.assertEqual((x+y).diff(x), 1)
        self.assertEqual((y*y).diff(y), 2*y)
#        self.assertEqual((0+y).simplify(), y)
#        self.assertEqual((x*y).simplify(), 2)

if __name__=='__main__':
    unittest.main()
