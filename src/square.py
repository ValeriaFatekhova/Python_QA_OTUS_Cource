from src.figure import Figure


class Square(Figure):
    name = "Square"

    def __init__(self, a):
        self.a = a
        self.area = a*a
        self.perimeter = 4*a

