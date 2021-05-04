""" math_master DOCSTRING 1.0"""
from app import app



class TestApp:
    """ math_master DOCSTRING 1.0"""
    response = None
    def test_fibonacci_post(self):
        """ math_master DOCSTRING 1.0"""
        self.response = app.test_client().post('/math/fibonacci', json={
            'n': 10
        })
        assert self.response.status_code == 200
        assert self.response.json[0] == 55, "In fibonacci n=10, should be 55"

    def test_factorial_post(self):
        """ math_master DOCSTRING 1.0"""
        self.response = app.test_client().post('/math/factorial', json={
            'n': 30
        })
        assert self.response.status_code == 200
        assert self.response.json[0] == 265252859812191058636308480000000, \
            "In factorial n=30, should be 265252859812191058636308480000000"

    def test_ackermann_post(self):
        """ math_master DOCSTRING 1.0"""
        self.response = app.test_client().post('/math/ackermann', json={
            'n': 2,
            'm': 2
        })
        assert self.response.status_code == 200
        assert self.response.json[0] == 7, "In ackermann n=2 and m=2, should be 7"
