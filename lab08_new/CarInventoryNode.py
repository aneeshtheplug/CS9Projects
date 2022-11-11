from Car import Car
class CarInventoryNode:
    def __init__(self,car):
        self.cars = [car]
        self.left = None
        self.right = None
        self.parent = None
        self.make = car.make
        self.model = car.model

    def getMake(self):
        return self.make
    
    def getModel(self):
        return self.model
    
    def getParent(self):
        return self.parent
    
    def setParent(self, parent):
        self.parent = parent

    def getLeft(self):
        return self.left
    
    def setLeft(self,left):
        self.left = left
    
    def setRight(self,right):
        self.right = right
    
    def getRight(self):
        return self.right
    
    def __str__(self):
        car_str = f''
        new_line = '\n'
        for i in range(len(self.cars)):
            car_str += str(self.cars[i]) + new_line
        return car_str
    
    def __gt__(self, rhs):
        if self.make > rhs.make:
            return True
        elif self.make == rhs.make:
            if self.model > rhs.model:
                return True
            return False
        return False 
    
    def __lt__(self, rhs):
        if self.make < rhs.make:
            return True
        elif self.make == rhs.make:
            if self.model < rhs.model:
                return True
            return False
        return False
    
    def __eq__(self, rhs):
        if self.make == rhs.make:
            if self.model == rhs.model:
                return True
            return False
        return False

''''
car1 = Car("Dodge", "dart", 2015, 6000)
car2 = Car("dodge", "DaRt", 2003, 5000)
carNode = CarInventoryNode(car1)
carNode.cars.append(car2)
print(carNode)'''
