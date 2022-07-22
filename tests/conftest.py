import pytest

from src.figures_2_homework.circle import Circle
from src.figures_2_homework.rectangle import Rectangle
from src.figures_2_homework.square import Square
from src.figures_2_homework.triangle import Triangle


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

@pytest.fixture
def default_triangle():
    triangle = Triangle(10, 15, 11)
    yield triangle
    del triangle

@pytest.fixture
def default_rectangle():
    rectangle = Rectangle(10, 15)
    yield rectangle
    del rectangle

@pytest.fixture
def default_square():
    square = Square(10)
    yield square
    del square

@pytest.fixture
def default_circle():
    circle = Circle(10)
    yield circle
    del circle

@pytest.fixture
def set_default_figure(figure):
    if figure == "triangle":
        triangle = Triangle(10, 15, 11)
        yield triangle
        del triangle
    if figure == "rectangle":
        rectangle = Rectangle(10, 15)
        yield rectangle
        del rectangle
    if figure == "square":
        square = Square(10)
        yield square
        del square
    if figure == "circle":
        circle = Circle(10)
        yield circle
        del circle


