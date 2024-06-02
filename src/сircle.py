from figure import Figure
from math import pi


class Circle(Figure):
    def __init__(self, radius: int | float):
        super().__init__(name='Circle')
        if not isinstance(radius, (int, float)) or radius <= 0:
            raise ValueError("Радиус задается целым или дробным числом (int, float) и должен быть больше 0")
        self.radius = radius

    def get_area(self) -> int | float:
        return pi * self.radius**2

    def get_perimeter(self) -> int | float:
        return 2 * pi * self.radius
