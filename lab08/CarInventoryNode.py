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
    
    def isLeftChild(self):
        return self.parent and self.parent.left == self
    
    def isRightChild(self):
        return self.parent and self.parent.right == self
    
    def replaceNodeData(self,make, model,cars,lc,rc):
        self.make = make
        self.model = model
        self.cars = cars
        self.left = lc
        self.right = rc
        if self.left:
            self.left.parent = self
        if self.right:
            self.right.parent = self
    
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
        if rhs == None:
            return False
        if self.make == rhs.make:
            if self.model == rhs.model:
                return True
            return False
        return False