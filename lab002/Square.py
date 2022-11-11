from Shape2D import Shape2D
class Square(Shape2D):
    def __init__(self, color, side):
        super().__init__(color)
        self.side = side
    
    def getSide(self):
        return self.side
    
    def setSide(self, side):
        self.side = side
    
    def computeArea(self):
        return self.side ** 2
    
    def computePerimeter(self):
        return self.side * 4
    
    def getShapeProperties(self):
        return f'Shape: SQUARE, Color: {self.color}, Side: {self.side}, Area: {self.computeArea()}, Perimeter: {self.computePerimeter()}'

