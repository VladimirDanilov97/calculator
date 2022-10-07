from ..calculation import Circle, TorosphiricalDish
from math import pi


def test_circle_good():
    c1 = Circle(2)
    assert  c1.calculate_square() == pi
    

def test_circle_bad():
    c1 = Circle(1)
    assert  c1.calculate_square() != pi

def test_torosphirical_dish_volume():
    d1 = TorosphiricalDish(1, 1, 0.1, 0.02, 4, 214)
    V = d1.calculate_inner_volume()
    assert V == 0.115