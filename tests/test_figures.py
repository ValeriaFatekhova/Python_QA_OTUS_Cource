import pytest
from math import sqrt, pi

from src.circle import Circle
from src.rectangle import Rectangle
from src.square import Square
from src.triangle import Triangle


"""Triangle creation tests"""

@pytest.mark.parametrize("a, b, c", [
    (13, 14, 15),
])
def test_triangle_creation_positive(a, b, c):
    Triangle(a, b, c)

@pytest.mark.parametrize("a, b, c", [
    (3, 4, 15),
    (13, 4, 5),
    (3, 14, 5),
    (-13, 14, 15),
    (13, -14, 15),
    (13, 14, -15),
    (0, 14, 15),
    (13, 0, 15),
    (13, 14, 0),
])
def test_triangle_creation_negative(a, b, c):
    with pytest.raises(ValueError):
        Triangle(a, b, c)


"""Rectangle creation tests"""

@pytest.mark.parametrize("a, b", [
    (2, 4),
    (0, 2),
    (3, 0),
    (0, 0),
])
def test_rectangle_creation_positive(a, b):
    Rectangle(a, b)

@pytest.mark.parametrize("a, b", [
    (-1, 5),
    (4, -2),
])
def test_rectangle_creation_negative(a, b):
    with pytest.raises(ValueError):
        Rectangle(a, b)


"""Square creation tests"""

@pytest.mark.parametrize("a", [10, 0, 100000000])
def test_square_creation_positive(a):
    Square(a)

@pytest.mark.parametrize("a", [-9])
def test_square_creation_negative(a):
    with pytest.raises(ValueError):
        Square(a)


"""Circle creation tests"""

@pytest.mark.parametrize("r", [10, 0, 100000000])
def test_circle_creation_positive(r):
    Circle(r)

@pytest.mark.parametrize("r", [-9])
def test_circle_creation_negative(r):
    with pytest.raises(ValueError):
        Circle(r)


"""Triangle area tests"""

@pytest.mark.parametrize("a, b, c", [
    (13, 14, 15),
])
def test_triangle_area_positive(triangle, a, b, c):
    p = (a+b+c)*0.5
    assert triangle.get_area() == sqrt(p*(p-a)*(p-b)*(p-c)), "Triangle area is incorrect"


"""Triangle perimeter tests"""

@pytest.mark.parametrize("a, b, c", [
    (13, 14, 15),
])
def test_triangle_perimeter_positive(triangle, a, b, c):
    assert triangle.get_perimeter() == a+b+c, "Triangle perimeter is incorrect"


"""Rectangle area tests"""

@pytest.mark.parametrize("a, b", [
    (100, 1000),
    (0, 0)
])
def test_rectangle_area_positive(rectangle, a, b):
    assert rectangle.get_area() == a*b, "Rectangle area is incorrect"


"""Rectangle perimeter tests"""

@pytest.mark.parametrize("a, b", [
    (100, 1000),
    (0, 0)
])
def test_rectangle_perimeter_positive(rectangle, a, b):
    assert rectangle.get_perimeter() == 2*a+2*b, "Rectangle perimeter is incorrect"


"""Square area tests"""

@pytest.mark.parametrize("a", [1000, 0])
def test_square_area_positive(square, a):
    assert square.get_area() == a*a, "Square area is incorrect"


"""Square perimeter tests"""

@pytest.mark.parametrize("a", [1000, 0])
def test_square_perimeter_positive(square, a):
    assert square.get_perimeter() == 4*a, "Square perimeter is incorrect"


"""Circle area tests"""

@pytest.mark.parametrize("r", [100000, 0])
def test_circle_area_positive(circle, r):
    assert circle.get_area() == pi*r*r, "Circle area is incorrect"


"""Circle perimeter tests"""

@pytest.mark.parametrize("r", [100000, 0])
def test_circle_perimeter_positive(circle, r):
    assert circle.get_perimeter() == 2*pi*r, "Circle perimeter is incorrect"


"""Add_area function tests"""

@pytest.mark.parametrize("figure", ["triangle", "circle", "rectangle", "square"])
def test_add_area_positive(set_default_figure, figure):
    sum_area = set_default_figure.add_area(set_default_figure)
    assert sum_area == set_default_figure.get_area() * 2

@pytest.mark.parametrize("figure", ["triangle", "circle", "rectangle", "square"])
def test_add_area_negative(set_default_figure, figure):
    class AnyObject:
        pass
    with pytest.raises(ValueError):
        set_default_figure.add_area(AnyObject())



