import pytest

"""Triangle creation test"""


@pytest.mark.parametrize("a, b, c", [
    (13, 14, 15),
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
def test_triangle_creation(a, b, c):
    pass


"""Rectangle creation test"""


@pytest.mark.parametrize("a, b", [
    (2, 4),
    (-1, 5),
    (4, -2),
    (0, 2),
    (3, 0),
    (0, 0),
])
def test_rectangle_creation(a, b):
    pass


"""Square creation test"""


@pytest.mark.parametrize("a", [10, 0, -9, 100000000])
def test_square_creation(a):
    pass


"""Circle creation test"""


@pytest.mark.parametrize("r", [10, 0, -9, 100000000])
def test_circle_creation(r):
    pass
