from src.figure import Figure
from math import sqrt


class Triangle(Figure):
    name = "Triangle"

    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
        self.perimeter = a + b + c
        self.area = sqrt((self.perimeter*0.5)*(self.perimeter*0.5-a)*(self.perimeter*0.5-b)*(self.perimeter*0.5-c))
