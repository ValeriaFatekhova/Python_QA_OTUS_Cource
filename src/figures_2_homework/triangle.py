from src.figures_2_homework.figure import Figure
from math import sqrt


class Triangle(Figure):
    name = "Triangle"

    def __init__(self, a, b, c):
        if a+b <= c or a+c <= b or c+b <= a:
            raise ValueError(f"impossible to create a triangle with sides {a}, {b}, {c}")
        elif a <= 0 or b <= 0 or c <= 0:
            raise ValueError(f"impossible to create a triangle with negative sides")
        else:
            self.a = a
            self.b = b
            self.c = c

    @property
    def area(self):
        return sqrt((self.perimeter*0.5)*(self.perimeter*0.5-self.a)*(self.perimeter*0.5-self.b)*(self.perimeter*0.5-self.c))

    @property
    def perimeter(self):
        return self.a + self.b + self.c
