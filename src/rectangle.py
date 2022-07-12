from src.figure import Figure


class Rectangle(Figure):
    name = "Rectangle"

    def __init__(self, a, b):
        if a < 0 or b < 0:
            raise ValueError(f"impossible to create a rectangle with negative sides")
        else:
            self.a = a
            self.b = b
            self.area = self.calculate_area()
            self.perimeter = self.calculate_perimeter()

    def calculate_area(self):
        return self.a*self.b

    def calculate_perimeter(self):
        return 2*self.a + 2*self.b
