class Animal:
    def __init__(self, species = None, weight = None, age = None, name = None):
        if species == None:
            self.species = species
        else:
            self.species = species.upper()
        if weight == None:
            self.weight = weight
        else:
            self.weight = float(weight)
        if age == None:
            self.age = age
        else:
            self.age = int(age)
        if name == None:
            self.name = name
        else:
            self.name = name.upper()
        
    def setSpecies(self, species):
        self.species = species.upper()
        
    def setWeight(self, weight):
        self.weight = float(weight)
        
    def setAge(self, age):
        self.age = int(age)

    def setName(self, name):
        self.name = name.upper()
        
    def toString(self):
        return f'Species: {self.species}, Name: {self.name}, Age: {self.age}, Weight: {self.weight}'
