from rectangle import Rectangle


class Square(Rectangle):
    def __init__(self, side_a):
        super().__init__(side_a=side_a, side_b=side_a)
        self.name = 'Square'
        if not isinstance(side_a, (int, float)) or side_a <= 0:
            raise ValueError("Сторона задается целым или дробным числом (int, float) и должно быть больше 0")
