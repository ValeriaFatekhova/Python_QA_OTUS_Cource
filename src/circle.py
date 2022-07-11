from src.figure import Figure
from math import pi


class Circle(Figure):
    name = "Circle"

    def __init__(self, r):
        self.r = r
        self.area = pi*r*r
        self.perimeter = 2*pi*r
