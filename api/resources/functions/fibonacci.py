""" math_master DOCSTRING 1.0"""
import time

class Fibonacci:
    """ math_master DOCSTRING 1.0"""
    n = 0
    def __init__(self, n):
        """ math_master DOCSTRING 1.0"""
        assert isinstance(n, int), "In Fibonacci(n) n shoud be a int ;)"
        self.n = n

    def calculate(self):
        """ math_master DOCSTRING 1.0"""
        start = time.time()
        first, second = 0, 1
        for _ in range(self.n):
            first, second = second, first+second
        end = time.time()
        return first, end - start
