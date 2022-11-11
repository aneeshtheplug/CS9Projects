class Car:
    def __init__(self, make, model, year, price):
        self.make = make.upper()
        self.model = model.upper()
        self.year = year
        self.price = price
    
    def setMake(self, make):
        self.make = make
    
    def getMake(self):
        return self.make
    
    def setModel(self, model):
        self.model = model
    
    def getModel(self):
        return self.model
    
    def setYear(self, year):
        self.year = year
    
    def getYear(self):
        return self.year
    
    def setPrice(self, price):
        self.price = price
    
    def getPrice(self):
        return self.price
    
    def __gt__(self, rhs):
        if self.make > rhs.make:
            return True
        elif self.make == rhs.make:
            if self.model > rhs.model:
                return True
            elif self.model == rhs.model:
                if self.year > rhs.year:
                    return True
                elif self.year == rhs.year:
                    if self.price > rhs.price:
                        return True
                    else:
                        return False
                else:
                    return False
            else:
                return False
        else:
            return False
    
    def __lt__(self, rhs):
        if self.make < rhs.make:
            return True
        elif self.make == rhs.make:
            if self.model < rhs.model:
                return True
            elif self.model == rhs.model:
                if self.year < rhs.year:
                    return True
                elif self.year == rhs.year:
                    if self.price < rhs.price:
                        return True
                    else:
                        return False
                else:
                    return False
            else:
                return False
        else:
            return False

    def __eq__(self, rhs):
        if self.make == rhs.make:
            if self.model == rhs.model:
                if self.year == rhs.year:
                    if self.price == rhs.price:
                        return True
                    else:
                        return False
                else:
                    return False
            else:
                return False
        else:
            return False
    
    def __str__(self):
        return f'Make: {self.make}, Model: {self.model}, Year: {self.year}, Price: ${self.price}'

'''
c = Car("Honda", "CRV", 2007, 8000)
print(c)'''