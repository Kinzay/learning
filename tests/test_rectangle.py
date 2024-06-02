import pytest

from src.rectangle import Rectangle
from src.square import Square
from src.figure import Figure


@pytest.mark.parametrize('data_type', ['integer', 'float'])
def test_rectangle_create_positive(rectangle_data, data_type):
    side_a, side_b = rectangle_data(data=data_type)[0], rectangle_data(data=data_type)[1]
    rectangle = Rectangle(side_a, side_b)
    assert isinstance(rectangle, Rectangle)


@pytest.mark.parametrize('data_type', ['integer', 'float'])
def test_rectangle_get_area_positive(rectangle_data, data_type):
    side_a, side_b, area = (rectangle_data(data=data_type)[0], rectangle_data(data=data_type)[1],
                            rectangle_data(data=data_type)[2])
    rectangle = Rectangle(side_a, side_b)
    assert rectangle.get_area() == area


#
@pytest.mark.parametrize('data_type', ['integer', 'float'])
def test_rectangle_get_perimeter_positive(rectangle_data, data_type):
    side_a, side_b, perimeter = (rectangle_data(data=data_type)[0], rectangle_data(data=data_type)[1],
                                 rectangle_data(data=data_type)[3])
    rectangle = Rectangle(side_a, side_b)
    assert rectangle.get_perimeter() == perimeter


def test_circle_add_area_positive():
    rectangle = Rectangle(1, 2)
    square = Square(2)
    assert rectangle.add_area(square) == 6


@pytest.mark.parametrize("sides", [(0, 1), (2, '1'), (3, -2)], ids=['zero', 'not number', 'negative integer'])
def test_rectangle_create_negative(sides):
    side_a, side_b = sides
    with pytest.raises(ValueError):
        Rectangle(side_a, side_b)


def test_rectangle_create_with_not_all_param():
    with pytest.raises(TypeError):
        Rectangle(2)


@pytest.mark.parametrize("second_figure", [0, '1', Figure], ids=['zero', 'string', 'not valid class'])
def test_rectangle_add_area_negative(second_figure):
    rectangle = Rectangle(2, 4)
    with pytest.raises(ValueError):
        rectangle.add_area(second_figure)
