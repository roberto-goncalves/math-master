""" math_master DOCSTRING 1.0"""
import time

class Ackermann:
    """ math_master DOCSTRING 1.0"""
    def __init__(self, n, m):
        assert isinstance(n, int), "In ackermann(n,m) n shoud be a int ;)"
        assert isinstance(m, int), "In ackermann(n,m) m shoud be a int ;)"

    def calculate(self, m, n):
        """ math_master DOCSTRING 1.0"""
        start = time.time()
        stack = []
        stack.append(m)
        while stack:
            m = stack.pop()
            if m == 0:
                n = n + 1
            elif n == 0:
                n = 1
                stack.append(m-1)
            else:
                n = n - 1
                stack.append(m-1)
                stack.append(m)
        end = time.time()
        return n, end - start
        