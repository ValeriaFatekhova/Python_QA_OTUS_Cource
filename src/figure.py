class Figure:
    name = None

    @property
    def area(self):
        return None

    @property
    def perimeter(self):
        return None

    def add_area(self, figure):
        if not isinstance(figure, Figure):
            raise ValueError(f"argument {figure} is not an object of Figure class")
        else:
            return self.area + figure.area

    def calculate_area(self):
        pass

    def calculate_perimeter(self):
        pass
