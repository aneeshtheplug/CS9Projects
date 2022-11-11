class Shape2D:
    def __init__(self, color):
        self.color = color
    
    def setColor(self, color):
        self.color = color

    def getColor(self):
        return self.color
    
    def getShapeProperties(self):
        return f'Shape: N/A, Color: {self.color}'