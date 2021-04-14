from source.oop_figure import Triangle, Square, Circle, Rectangle


def test_check_circle_name():
    assert Circle(radius=10).name == 'Circle'


def test_check_circle_angles():
    assert Circle(radius=300).angles == 0


def test_calc_area_circle():
    assert Circle(radius=99).area() == 30790.74959783356


def test_calc_perimetr_circle():
    assert Circle(radius=1).perimetr() == 6.283185307179586


def test_sum_area_circle_triangle():
    triangle = Triangle(line_a=9, line_b=12, line_c=15, line_h=40)
    assert Circle(radius=9).add_area(triangle) == 494.46900494077323


def test_sum_area_circle_rectangle():
    assert Circle(radius=2).add_area(Rectangle(5, 20)) == 112.56637061435917


def test_sum_area_circle_square():
    assert Circle(radius=21).add_area(Square(21)) == 1826.4423602330987
