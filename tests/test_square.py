from source.oop_figure import Square, Rectangle

def test_check_square_name():
    assert Square(10).name == 'Square'

def test_check_square_angles():
    assert Square(2000).angles == 4

def test_calc_square_area():
    assert Square(30).area() == 900


def test_calc_square_perimetr():
    assert Square(10).perimetr() == 40

def test_sum_area_square_rectangle():
    assert Square(100).add_area(Rectangle(300, 500)) == 160000