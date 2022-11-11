class Apartment():
    def __init__(self, rent, metersFromUCSB, condition):
        self.rent = rent
        self.metersFromUCSB = metersFromUCSB
        self.condition = condition
    
    def getRent(self):
        return self.rent

    def getMetersFromUCSB(self):
        return self.metersFromUCSB
    
    def getCondition(self):
        return self.condition
    
    def setRent(self,rent):
        self.rent = rent
    
    def setMetersFromUCSB(self, metersFromUCSB):
        self.metersFromUCSB = metersFromUCSB
    
    def setConditon(self, condition):
        self.condition = condition
    
    def getApartmentDetails(self):
        return f'(Apartment) Rent: ${self.rent}, Distance From UCSB: {self.metersFromUCSB}m, Condition: {self.condition}'
    
    def __lt__(self, other):
        if self.rent < other.rent:
            return True
        elif self.rent == other.rent:
            if self.metersFromUCSB < other.metersFromUCSB:
                return True
            elif self.metersFromUCSB == other.metersFromUCSB:
                if self.condition == "excellent" and other.condition != "excellent":
                    return True
                elif self.condition == "average" and other.condition == "bad":
                    return True
                else:
                    return False
            else:
                return False
        else:
            return False
    
    def __gt__(self, other):
        if self.rent > other.rent:
            return True
        elif self.rent == other.rent:
            if self.metersFromUCSB > other.metersFromUCSB:
                return True
            elif self.metersFromUCSB == other.metersFromUCSB:
                if self.condition == "bad" and other.condition != "bad":
                    return True
                elif self.condition == "average" and other.condition == "excellent":
                    return True
                else:
                    return False
            else:
                return False
        else:
            return False

    def __eq__(self, other):
        if self.rent == other.rent:
            if self.metersFromUCSB == other.metersFromUCSB:
                if self.condition == other.condition:
                    return True
                else:
                    return False
            return False
        else:
            return False    
