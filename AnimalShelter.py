from Animal import Animal

class AnimalShelter:
    ''' dictionary structure where the keys of the dictionary will be a str
       type representing an Animals species (all upper-case characters).
       The dictionary value will be a list of Animal objects that the
       AnimalShelter contains'''

    def __init__(self):
        self.dict = {}

    def addAnimal(self, animal):
        if self.dict.get(animal.species) == None:
            self.dict[animal.species] = [animal]
        else:
            self.dict[animal.species].append(animal)

    def removeAnimal(self, animal):
        '''  Removes an Animal object (animal) from the AnimalShelter if it exists. Your code
         will need to check and see if the parameter animal object has the same species, name,
        age, and weight as an existing animal in the AnimalShelter if it is to be removed from 
        the AnimalShelter.'''
        for key in self.dict:
            if key == animal.species:
                for val in self.dict[key]:
                    if val == animal:
                        self.dict[key].remove(val)
                    else:
                        continue
    def removeSpecies(self, species):
        if self.dict.get(species.upper()) != None:
            del self.dict[species.upper()]
    
    def getAnimalsBySpecies(self, species):
        if self.dict.get(species.upper()) == None:
            return ""
        else:
            new_str = ''
            for val in range(len(self.dict[species.upper()])):
                if self.dict[species.upper()][val] != self.dict[species.upper()][-1]:
                    new_str +=  self.dict[species.upper()][val].toString() + '\n'
                else:
                    new_str += self.dict[species.upper()][val].toString()
            return new_str
    
    def doesAnimalExist(self,animal):
        counter = 0
        for key in self.dict:
            if key == animal.species:
                for val in self.dict[key]:
                    if val == animal:
                        counter+=1
                    else:
                        counter+=0
        else:
            if counter != 0:
                return True
            else:
                return False    
