import pytest

from src.сircle import Circle
from src.square import Square
from src.figure import Figure


@pytest.mark.parametrize('data_type', ['integer', 'float'])
def test_circle_create_positive(circle_data, data_type):
    side = circle_data(data=data_type)[0]
    circle = Circle(side)
    assert isinstance(circle, Circle)


@pytest.mark.parametrize('data_type', ['integer', 'float'])
def test_circle_get_area_positive(circle_data, data_type):
    side, area = circle_data(data=data_type)[0], circle_data(data=data_type)[1]
    circle = Circle(side)
    assert circle.get_area() == area


@pytest.mark.parametrize('data_type', ['integer', 'float'])
def test_circle_get_perimeter_positive(circle_data, data_type):
    side, perimeter = circle_data(data=data_type)[0], circle_data(data=data_type)[2]
    circle = Circle(side)
    assert circle.get_perimeter() == perimeter


def test_circle_add_area_positive():
    circle = Circle(1)
    square = Square(2)
    assert circle.add_area(square) == 7.141592653589793


@pytest.mark.parametrize("side", [0, '1', -2], ids=['zero', 'not number', 'negative integer'])
def test_circle_create_negative(side):
    with pytest.raises(ValueError):
        Circle(side)


@pytest.mark.parametrize("second_figure", [0, '1', Figure], ids=['zero', 'string', 'not valid class'])
def test_circle_add_area_negative(second_figure):
    circle = Circle(1)
    with pytest.raises(ValueError):
        circle.add_area(second_figure)