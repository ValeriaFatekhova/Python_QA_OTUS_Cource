from src.figure import Figure
from math import sqrt


class Triangle(Figure):
    name = "Triangle"

    def __init__(self, a, b, c):
        if a+b <= c or a+c <= b or c+b <= a:
            raise ValueError(f"impossible to create a triangle with sides {a}, {b}, {c}")
        else:
            self.a = a
            self.b = b
            self.c = c
            self.perimeter = self.calculate_perimeter()
            self.area = self.calculate_area()

    def calculate_area(self):
        return sqrt((self.perimeter*0.5)*(self.perimeter*0.5-self.a)*(self.perimeter*0.5-self.b)*(self.perimeter*0.5-self.c))

    def calculate_perimeter(self):
        return self.a + self.b + self.c
