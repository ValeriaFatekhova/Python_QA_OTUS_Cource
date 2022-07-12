from src.figure import Figure


class Rectangle(Figure):
    name = "Rectangle"

    def __init__(self, a, b):
        if a < 0 or b < 0:
            raise ValueError(f"impossible to create a rectangle with negative sides")
        else:
            self.a = a
            self.b = b

    @property
    def area(self):
        return self.a*self.b

    @property
    def perimeter(self):
        return 2*self.a + 2*self.b
