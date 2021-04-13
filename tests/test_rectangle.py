from source.oop_figure import Rectangle, Circle



def test_check_rectangle_name():
    rectangle = Rectangle(3, 5)
    assert rectangle.name == "Rectangle"


def test_check_rectangle_angles():
    rectangle = Rectangle(4, 5)
    assert rectangle.angles == 4


def test_calc_rectangle_area():
    rectangle = Rectangle(3, 7)
    assert rectangle.area() == 21


def test_calc_rectangle_perimetr():
    rectangle = Rectangle(9, 12)
    assert rectangle.perimetr() == 42

def test_calc_sum_area_rectangle_circle():
    rectangle = Rectangle(4, 3)
    circle = Circle(5)
    assert rectangle.add_area(circle) == 90.53981633974483