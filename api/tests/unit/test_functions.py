""" math_master DOCSTRING 1.0"""
import unittest

from resources.functions import fibonacci, factorial, ackermann

class TestFunctions(unittest.TestCase):
    """ math_master DOCSTRING 1.0"""
    def test_fibonacci(self):
        """ math_master DOCSTRING 1.0"""
        fib,time = fibonacci.Fibonacci(n=10).calculate()
        self.assertEqual(fib, 55)
        self.assertLess(time, 5)
        fib,time = fibonacci.Fibonacci(n=5).calculate()
        self.assertEqual(fib, 5)
        self.assertLess(time, 5)
        fib,time = fibonacci.Fibonacci(n=-5).calculate()
        self.assertEqual(fib, 0)
        self.assertLess(time, 5)

    def test_factorial(self):
        """ math_master DOCSTRING 1.0"""
        fac,time = factorial.Factorial(n=10).calculate()
        self.assertEqual(fac, 3628800)
        self.assertLess(time, 5)
        fac,time = factorial.Factorial(n=5).calculate()
        self.assertEqual(fac, 120)
        self.assertLess(time, 5)
        fac,time = factorial.Factorial(n=-55).calculate()
        self.assertEqual(fac, 1)
        self.assertLess(time, 5)

    def test_ackerman(self):
        """ math_master DOCSTRING 1.0"""
        ack,time = ackermann.Ackermann(n=3, m=3).calculate(n=3, m=3)
        self.assertEqual(ack, 61)
        self.assertLess(time, 5)
        ack,time = ackermann.Ackermann(n=3, m=2).calculate(n=3, m=2)
        self.assertEqual(ack, 9)
        self.assertLess(time, 5)

if __name__ == '__main__':
    unittest.main()
