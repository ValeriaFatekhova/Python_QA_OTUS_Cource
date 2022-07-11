from src.figure import Figure


class Square(Figure):
    name = "Square"

    def __init__(self, a):
        self.a = a
        self.area = self.calculate_area()
        self.perimeter = self.calculate_perimeter()

    def calculate_area(self):
        return self.a*self.a

    def calculate_perimeter(self):
        return 4*self.a
