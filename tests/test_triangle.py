from source.oop_figure import Triangle, Square, Circle, Rectangle


def test_check_triangle_name():
    assert Triangle(line_a=6, line_b=12, line_c=15, line_h=11).name == 'Triangle'


def test_check_triangle_angles():
    assert Triangle(line_a=9, line_b=12, line_c=15, line_h=40).angles == 3


def test_calc_triangle_area():
    assert Triangle(line_a=9, line_b=10, line_c=15, line_h=14).area() == 70


def test_calc_triangle_perimetr():
    assert Triangle(line_a=1, line_b=2, line_c=3, line_h=4).perimetr() == 6


def test_sum_area_triangle_square():
    triangle = Triangle(line_a=1, line_b=2, line_c=3, line_h=4)
    assert triangle.add_area(Square(line_a=20)) == 404


def test_sum_area_triangle_circle():
    triangle = Triangle(line_a=1, line_b=2, line_c=3, line_h=4)
    sum_area_triangle_circle = triangle.add_area(Circle(radius=20))
    assert round(sum_area_triangle_circle, 2) == 1260.64


def test_sum_area_triangle_rectangle():
    triangle = Triangle(line_a=1, line_b=2, line_c=3, line_h=4)
    assert triangle.add_area(Rectangle(line_a=20, line_b=100)) == 2004
