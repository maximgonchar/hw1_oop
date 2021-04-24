from source.oop_figure import Triangle, Square, Circle, Rectangle


def test_check_circle_name():
    assert Circle(radius=10).name == 'Circle'


def test_check_circle_angles():
    assert Circle(radius=300).angles == 0


def test_calc_area_circle():
    area_circle = Circle(radius=99).area()
    assert round(area_circle, 2) == 30790.75


def test_calc_perimetr_circle():
    perimetr_circle = Circle(radius=1).perimetr()
    assert round(perimetr_circle, 2) == 6.28


def test_sum_area_circle_triangle():
    triangle = Triangle(line_a=9, line_b=12, line_c=15, line_h=40)
    sum_area_circle_triangle = Circle(radius=9).add_area(triangle)
    assert round(sum_area_circle_triangle, 2)== 494.47


def test_sum_area_circle_rectangle():
    sum_area_circle_rectangle = Circle(radius=2).add_area(Rectangle(5, 20))
    assert round(sum_area_circle_rectangle, 2) == 112.57


def test_sum_area_circle_square():
    sum_area_circle_square = Circle(radius=21).add_area(Square(21))
    assert round(sum_area_circle_square, 2) == 1826.44
