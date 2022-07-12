from src.figure import Figure
from math import pi


class Circle(Figure):
    name = "Circle"

    def __init__(self, r):
        if r < 0:
            raise ValueError(f"it is impossible to create a circle with a negative radius")
        else:
            self.r = r
            # self.area = self.calculate_area()
            # self.perimeter = self.calculate_perimeter()

    @property
    def area(self):
        return pi * self.r * self.r

    @property
    def perimeter(self):
        return 2 * pi * self.r

    # def calculate_area(self):
    #     return pi * self.r * self.r
    #
    # def calculate_perimeter(self):
    #     return 2 * pi * self.r
