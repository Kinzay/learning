import pytest

from src.square import Square
from src.rectangle import Rectangle
from src.figure import Figure


@pytest.mark.parametrize('data_type', ['integer', 'float'])
def test_square_create_positive(square_data, data_type):
    side = square_data(data=data_type)[0]
    rectangle = Square(side)
    assert isinstance(rectangle, Square)


@pytest.mark.parametrize('data_type', ['integer', 'float'])
def test_square_get_area_positive(square_data, data_type):
    side, area = square_data(data=data_type)[0], square_data(data=data_type)[1]
    rectangle = Square(side)
    assert rectangle.get_area() == area


@pytest.mark.parametrize('data_type', ['integer', 'float'])
def test_square_get_perimeter_positive(square_data, data_type):
    side, perimeter = square_data(data=data_type)[0], square_data(data=data_type)[2]
    square = Square(side)
    assert square.get_perimeter() == perimeter


def test_square_add_area_positive():
    square = Square(2)
    rectangle = Rectangle(2, 4)
    assert rectangle.add_area(square) == 12


@pytest.mark.parametrize("side", [0, '1', -2], ids=['zero', 'not number', 'negative integer'])
def test_rectangle_create_negative(side):
    with pytest.raises(ValueError):
        Square(side)


@pytest.mark.parametrize("second_figure", [0, '1', Figure], ids=['zero', 'string', 'not valid class'])
def test_square_add_area_negative(second_figure):
    square = Square(2)
    with pytest.raises(ValueError):
        square.add_area(second_figure)
