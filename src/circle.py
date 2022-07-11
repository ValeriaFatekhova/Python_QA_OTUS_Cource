from src.figure import Figure
from math import pi


class Circle(Figure):
    name = "Circle"

    def __init__(self, r):
        self.r = r
        self.area = self.calculate_area()
        self.perimeter = self.calculate_perimeter()

    def calculate_area(self):
        return pi * self.r * self.r

    def calculate_perimeter(self):
        return 2 * pi * self.r
