import math


LENGTH_UNITS = [
    (1, 'm'),
    (10**-2, 'cm')
]

SQUARE_UNITS = [
    (1, 'm2'),
    (10**-4, 'cm2'),
    (10**-6, 'mm2')
]

PRESSURE_UNITS = [
    (1, 'Pa',
    10**-6, 'MPa',
    10**-6*9.8, 'kgf/cm2')
]

class Circle():
    def __init__(self, d):
        self.d = d
    
    def calculate_square(self):
        return self.d**2*math.pi/4

class Cylyndre():
    def __init__(self) -> None:
        self.d