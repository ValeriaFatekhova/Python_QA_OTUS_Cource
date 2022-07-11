import pytest

from src.circle import Circle
from src.rectangle import Rectangle
from src.square import Square
from src.triangle import Triangle


@pytest.fixture
def triangle(a, b, c):
    triangle = Triangle(a, b, c)
    yield triangle
    del triangle

@pytest.fixture
def rectangle(a, b):
    rectangle = Rectangle(a, b)
    yield rectangle
    del rectangle

@pytest.fixture
def square(a):
    square = Square(a)
    yield square
    del square

@pytest.fixture
def circle(r):
    circle = Circle(r)
    yield circle
    del circle

