from src.figure import Figure


class Rectangle(Figure):
    name = "Rectangle"

    def __init__(self, a, b):
        self.a = a
        self.b = b
        self.area = a*b
        self.perimeter = 2*a + 2*b

