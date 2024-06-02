import pytest

from src.triangle import Triangle
from src.square import Square
from src.figure import Figure


#
@pytest.mark.parametrize('data_type', ['integer', 'float'])
def test_triangle_create_positive(triangle_data, data_type):
    side_a, side_b, side_c = (triangle_data(data=data_type)['side_a'], triangle_data(data=data_type)['side_b'],
                              triangle_data(data=data_type)['side_c'])
    triangle = Triangle(side_a, side_b, side_c)
    assert isinstance(triangle, Triangle)


@pytest.mark.parametrize('data_type', ['integer', 'float'])
def test_triangle_get_area_positive(triangle_data, data_type):
    side_a, side_b, side_c, area = (triangle_data(data=data_type)['side_a'], triangle_data(data=data_type)['side_b'],
                                    triangle_data(data=data_type)['side_c'], triangle_data(data=data_type)['area'])
    triangle = Triangle(side_a, side_b, side_c)
    assert triangle.get_area() == area


#
@pytest.mark.parametrize('data_type', ['integer', 'float'])
def test_triangle_get_perimeter_positive(triangle_data, data_type):
    side_a, side_b, side_c, perimeter = (triangle_data(data=data_type)['side_a'], triangle_data(data=data_type)['side_b'],
                                    triangle_data(data=data_type)['side_c'], triangle_data(data=data_type)['perimeter'])
    triangle = Triangle(side_a, side_b, side_c)
    assert triangle.get_area() == perimeter


def test_triangle_add_area_positive():
    triangle = Triangle(1, 3, 3)
    square = Square(2)
    assert triangle.add_area(square) == 5.479019945774904


@pytest.mark.parametrize("sides", [(0, 1, 4), (2, '1', 2), (3, -2, 3), (1, 2, 3)], ids=['zero', 'not number', 'negative integer', 'non-existent triangle'])
def test_triangle_create_negative(sides):
    side_a, side_b, side_c = sides
    with pytest.raises(ValueError):
        Triangle(side_a, side_b, side_c)


def test_triangle_create_with_not_all_param():
    with pytest.raises(TypeError):
        Triangle(2, 4)


@pytest.mark.parametrize("second_figure", [0, '1', Figure], ids=['zero', 'string', 'not valid class'])
def test_triangle_add_area_negative(second_figure):
    triangle = Triangle(2, 4, 4)
    with pytest.raises(ValueError):
        triangle.add_area(second_figure)
