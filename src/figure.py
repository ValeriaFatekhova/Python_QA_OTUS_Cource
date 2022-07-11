class Figure:
    name = None
    area = None
    perimeter = None

    def add_area(self, figure):
        if not isinstance(figure, Figure):
            raise ValueError(f"argument {figure} is not an object of Figure class")
        else:
            return self.area + figure.area

    def get_area(self):
        return self.area

    def get_perimeter(self):
        return self.perimeter

    def get_name(self):
        return self.name

    def calculate_area(self):
        pass

    def calculate_perimeter(self):
        pass
