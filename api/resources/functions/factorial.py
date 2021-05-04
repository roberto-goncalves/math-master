""" math_master DOCSTRING 1.0"""
import time

class Factorial:
    """ math_master DOCSTRING 1.0"""
    n = 0
    def __init__(self, n):
        """ math_master DOCSTRING 1.0"""
        assert isinstance(n, int), "In factorial(n) n shoud be a int ;)"
        self.n = n
    def calculate(self):
        """ math_master DOCSTRING 1.0"""
        start = time.time()
        fac = 1
        for i in range(1, self.n+1):
            fac *= i
        end = time.time()
        return fac, end - start
