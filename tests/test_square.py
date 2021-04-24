from source.oop_figure import Triangle, Square, Circle, Rectangle


def test_check_square_name():
    assert Square(line_a=10).name == 'Square'


def test_check_square_angles():
    assert Square(line_a=2000).angles == 4


def test_calc_square_area():
    assert Square(line_a=30).area() == 900


def test_calc_square_perimetr():
    assert Square(line_a=10).perimetr() == 40


def test_sum_area_square_rectangle():
    assert Square(line_a=100).add_area(Rectangle(line_a=300, line_b=500)) == 160000


def test_sum_area_square_triangle():
    triangle = Triangle(line_a=1, line_b=2, line_c=3, line_h=4)
    assert Square(line_a=25).add_area(triangle) == 629


def test_sum_area_square_circle():
    sum_area_square_circle = Square(line_a=1).add_area(Circle(radius=17))
    assert round(sum_area_square_circle, 2) == 908.92
