from figure import Figure


class Rectangle(Figure):
    def __init__(self, side_a: int | float, side_b: int | float):
        super().__init__(name="Rectangle")
        self.side_a = side_a
        self.side_b = side_b
        if (not isinstance(side_a, (int, float)) or not isinstance(side_b, (int, float))
                or any(True for side in [side_a, side_b] if side <= 0)):
            raise ValueError("Стороны задаются целыми или дробными числами (int, float) и должны быть больше 0")

    def get_area(self) -> int | float:
        return self.side_a * self.side_b

    def get_perimeter(self) -> int | float:
        return self.side_a * 2 + self.side_b * 2
