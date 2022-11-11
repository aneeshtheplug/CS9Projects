class Pizza:
    def __init__(self, size):
        self.size = size
        self.price = 0
    
    def setSize(self,size):
        self.size = size
    
    def setPrice(self,price):
        self.price = price
    
    def getSize(self):
        return self.size

    def getPrice(self):
        return self.price

    