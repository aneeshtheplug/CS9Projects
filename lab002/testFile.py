from Circle import Circle
from Shape2D import Shape2D
from Square import Square

b = Shape2D("blue")
c = Circle("red", 7)
c1 = Circle("grey", 0)
s = Square("purple", 9)

def test_Shape2D():
    assert b.getShapeProperties() == 'Shape: N/A, Color: blue'
    assert b.getColor() == "blue"

def test_Circle():
    assert c.getRadius() == 7
    assert c.computeArea() == 153.93791
    assert c.computePerimeter() == 43.98226
    assert c.getShapeProperties() == "Shape: CIRCLE, Color: red, Radius: 7, Area: 153.93791, Perimeter: 43.98226"
    assert c1.getRadius() == 0
    assert c1.computeArea() == 0
    assert c1.computePerimeter() == 0
    assert c1.getShapeProperties() == "Shape: CIRCLE, Color: grey, Radius: 0, Area: 0.0, Perimeter: 0.0"

def test_Square():
    assert s.getSide() == 9
    assert s.computeArea() == 81
    assert s.computePerimeter() == 36
    assert s.getShapeProperties() == "Shape: SQUARE, Color: purple, Side: 9, Area: 81, Perimeter: 36"





