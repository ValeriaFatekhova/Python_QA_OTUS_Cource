class Figure:
    name = None

    @property
    def area(self):
        return None

    @property
    def perimeter(self):
        return None

    def get_name(self):
        return self.name

    def add_area(self, figure):
        if not isinstance(figure, Figure):
            raise ValueError(f"argument {figure} is not an object of Figure class")
        else:
            return self.area + figure.area
