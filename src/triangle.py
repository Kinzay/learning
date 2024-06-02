from figure import Figure


class Triangle(Figure):
    def __init__(self, side_a: int | float, side_b: int | float, side_c: int | float):
        super().__init__(name='Triangle')
        self.size_a = side_a
        self.size_b = side_b
        self.size_c = side_c
        if (not isinstance(side_a, (int, float)) or not isinstance(side_b, (int, float))
                or not isinstance(side_c, (int, float)) or any(True for side in [side_a, side_b, side_c] if side <= 0)):
            raise ValueError("Стороны задаются целыми или дробными числами (int, float) и должны быть больше 0")

        if not (side_a < side_b + side_c and side_b < side_c + side_a and side_c < side_a + side_b):
            raise ValueError("При заданных сторонах треугольник не существует")

    def get_area(self) -> int | float:
        half_perimeter = self.get_perimeter() / 2
        return (half_perimeter * (half_perimeter - self.size_a) * (half_perimeter - self.size_b) *
                (half_perimeter - self.size_c))**0.5

    def get_perimeter(self) -> int | float:
        return self.size_a + self.size_b + self.size_c
