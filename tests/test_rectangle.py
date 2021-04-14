from source.oop_figure import Rectangle, Circle, Square, Triangle


def test_check_rectangle_name():
    assert Rectangle(line_a=3, line_b=5).name == "Rectangle"


def test_check_rectangle_angles():
    assert Rectangle(line_a=4, line_b=5).angles == 4


def test_calc_rectangle_area():
    assert Rectangle(line_a=3, line_b=7).area() == 21


def test_calc_rectangle_perimetr():
    assert Rectangle(line_a=9, line_b=12).perimetr() == 42


def test_calc_sum_area_rectangle_square():
    assert Rectangle(line_a=4, line_b=3).add_area(Square(line_a=10)) == 112


def test_calc_sum_area_rectangle_circle():
    assert Rectangle(line_a=4, line_b=3).add_area(Circle(radius=5)) == 90.53981633974483


def test_calc_sum_area_rectangle_triangle():
    triangle = Triangle(line_a=9, line_b=10, line_c=15, line_h=14)
    assert Rectangle(line_a=4, line_b=3).add_area(triangle) == 82
