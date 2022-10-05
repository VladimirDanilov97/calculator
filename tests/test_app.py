from ..calculation import Circle
from math import pi


def test_circle_good():
    c1 = Circle(2)
    assert  c1.calculate_square() == pi
    

def test_circle_bad():
    c1 = Circle(1)
    assert  c1.calculate_square() != pi