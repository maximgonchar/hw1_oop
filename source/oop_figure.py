import math


class Figure:
    name = None
    area = None
    angles = None
    perimetr = None

    def __init__(self, name, angles):
        self.name = name
        self.angles = angles

    @property
    def figure_name(self):
        return self.name

    @property
    def figure_angles(self):
        return self.angles

    def add_area(self, another_figure):
        if isinstance(another_figure, Figure):
            return self.area() + another_figure.area()
        else:
            raise AttributeError("Передан неправильный класс")


class Rectangle(Figure):

    def __init__(self, line_a, line_b):
        self.line_a = line_a
        self.line_b = line_b
        super().__init__("Rectangle", 4)

    def area(self):
        return self.line_a * self.line_b

    def perimetr(self):
        return 2 * self.line_a + 2 * self.line_b


class Square(Rectangle):
    def __init__(self, line_a):
        super().__init__(line_a, line_a)
        Figure.__init__(self, "Square", 4)


class Triangle(Figure):
    def __init__(self, line_a: int, line_b: int, line_c: int, line_h: int):
        self.line_a = line_a
        self.line_b = line_b
        self.line_c = line_c
        self.line_h = line_h
        super().__init__("Triangle", 3)

    def area(self) -> float:
        return 0.5 * self.line_b * self.line_h

    def perimetr(self) -> int:
        return self.line_a + self.line_b + self.line_c


class Circle(Figure):
    def __init__(self, radius: int):
        self.radius = radius
        super().__init__("Circle", 0)

    def area(self) -> float:
        return self.radius ** 2 * math.pi

    def perimetr(self) -> float:
        return 2 * math.pi * self.radius
