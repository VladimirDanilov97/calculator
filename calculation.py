import math
from math import asin, cos, sin, pi, sqrt

class Circle():
    def __init__(self, d):
        self.d = d
    
    def calculate_square(self):
        return self.d**2*pi/4


class Cylyndre():
    def __init__(self) -> None:
        self.d

class TorosphiricalDish():
    def __init__(self, D, R, r, h, s) -> None:
        self.D = D-2*s
        self.R = R
        self.r = r
        self.h = h       
    
    def calculate_inner_volume(self):
        k = self.r/self.D # knuckle-radius parameter
        f = self.R/self.D # dish-radius parameter

        alpha = asin( (1 - 2*k)/(2*(f-k)) )

        a_1 = f * self.D * (1 - cos(alpha))
        a_2 = k * self.D * cos(alpha)
        D_1 = (2*f * self.D * sin(alpha))
        s = (k * self.D * sin(alpha))**2
        t = 2*a_2

        V_1 = pi/4 * (2*a_1**3/3 + a_1*D_1**2/2)
        V_2 = pi*a_2 * ( (self.D/2 - k*self.D)**2 + s )
        V_3 = pi*t**3/12
        V_4_1 = pi*self.D*(1-2*k)
        V_4_2 = t*sqrt(s)/4 + k**2*self.D**2/2*asin(cos(alpha)) 
        V_4 = V_4_1 * V_4_2
        V_5 = pi*self.D**2*self.h/4 

        inner_volume = V_1 + V_2 + V_3 + V_4 + V_5
        return round(inner_volume, 3)  
        
