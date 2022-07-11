import pytest

from src.circle import Circle
from src.rectangle import Rectangle
from src.square import Square
from src.triangle import Triangle


@pytest.fixture
def triangle(a, b, c):
    return Triangle(a, b, c)

@pytest.fixture
def rectangle(a, b):
    return Rectangle(a, b)

@pytest.fixture
def square(a):
    return Square(a)

@pytest.fixture
def circle(r):
    return Circle(r)