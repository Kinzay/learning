import pytest


@pytest.fixture()
def circle_data(request):
    def _wrapper(data: str):
        if data == 'integer':
            side, area, perimeter = 1, 3.141592653589793, 6.283185307179586
            return side, area, perimeter
        if data == 'float':
            side, area, perimeter = 2.25, 15.904312808798327, 14.137166941154069
            return side, area, perimeter

    yield _wrapper


@pytest.fixture()
def rectangle_data(request):
    def _wrapper(data: str):
        if data == 'integer':
            side_a, side_b, area, perimeter = 1, 2, 2, 6
            return side_a, side_b, area, perimeter
        if data == 'float':
            side_a, side_b, area, perimeter = 2.25, 3, 6.75, 10.5
            return side_a, side_b, area, perimeter

    yield _wrapper


@pytest.fixture()
def square_data(request):
    def _wrapper(data: str):
        if data == 'integer':
            side, area, perimeter = 5, 25, 20
            return side, area, perimeter
        if data == 'float':
            side, area, perimeter = 2.25, 5.0625, 9.0
            return side, area, perimeter

    yield _wrapper


@pytest.fixture()
def triangle_data(request):
    def _wrapper(data: str):
        if data == 'integer':
            triangle_properties = {'side_a': 1,
                                   'side_b': 3,
                                   'side_c': 3,
                                   'area': 1.479019945774904,
                                   'perimeter': 1.479019945774904}
            return triangle_properties
        if data == 'float':
            triangle_properties = {'side_a': 1.2,
                                   'side_b': 2.3,
                                   'side_c': 3.4,
                                   'area': 0.6680896272207812,
                                   'perimeter': 0.6680896272207812}
            return triangle_properties

    yield _wrapper
