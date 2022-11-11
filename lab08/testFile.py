from Car import Car
from CarInventoryNode import CarInventoryNode
from CarInventory import CarInventory

def test__eq__():
    car1 = Car("Dodge", "dart", 2015, 6000)
    car2 = Car("dodge", "DaRt", 2015, 6000)
    assert car1.__eq__(car2) == True 

def test__gt__():
    car1 = Car("Tesla", "X", 2015, 6000)
    car2 = Car("dodge", "DaRt", 2015, 6000)
    assert car1.__gt__(car2) == True 

def test__lt__():
    car1 = Car("Ford", "Escort", 2015, 6000)
    car2 = Car("dodge", "DaRt", 2015, 6000)
    assert car2.__lt__(car1) == True 

def test__str__():
    c = Car("Honda", "CRV", 2007, 8000)
    assert c.__str__() == "Make: HONDA, Model: CRV, Year: 2007, Price: $8000"

def test__NodeStr__():
    car1 = Car("Dodge", "dart", 2015, 6000)
    car2 = Car("dodge", "DaRt", 2003, 5000)
    carNode = CarInventoryNode(car1)
    carNode.cars.append(car2)
    assert carNode.__str__() == f'Make: DODGE, Model: DART, Year: 2015, Price: $6000\nMake: DODGE, Model: DART, Year: 2003, Price: $5000\n'

def test__NodeGt__():
    car1 = Car("Dodge", "dart", 2015, 6000)
    car2 = Car("Tesla", "Model3", 2018, 50000)
    carNode = CarInventoryNode(car1)
    carNode1 =  CarInventoryNode(car2)
    assert carNode1.__gt__(carNode) == True

def test__NodeLt__():
    car1 = Car("Dodge", "dart", 2015, 6000)
    car2 = Car("Tesla", "Model3", 2018, 50000)
    carNode = CarInventoryNode(car1)
    carNode1 =  CarInventoryNode(car2)
    assert carNode.__lt__(carNode1) == True

def test__NodeEq__():
    car1 = Car("Dodge", "dart", 2015, 6000)
    car2 = Car("dodge", "DaRt", 2003, 5000)
    carNode = CarInventoryNode(car1)
    carNode1 =  CarInventoryNode(car2)
    assert carNode.__eq__(carNode1) == True

def test__inOrder():
    bst = CarInventory()

    car1 = Car("Nissan", "Leaf", 2018, 18000)
    car2 = Car("Tesla", "Model3", 2018, 50000)
    car3 = Car("Mercedes", "Sprinter", 2022, 40000)
    car4 = Car("Mercedes", "Sprinter", 2014, 25000)
    car5 = Car("Ford", "Ranger", 2021, 25000)

    bst.addCar(car1)
    bst.addCar(car2)
    bst.addCar(car3)
    bst.addCar(car4)
    bst.addCar(car5)

    assert bst.inOrder() == \
"""\
Make: FORD, Model: RANGER, Year: 2021, Price: $25000
Make: MERCEDES, Model: SPRINTER, Year: 2022, Price: $40000
Make: MERCEDES, Model: SPRINTER, Year: 2014, Price: $25000
Make: NISSAN, Model: LEAF, Year: 2018, Price: $18000
Make: TESLA, Model: MODEL3, Year: 2018, Price: $50000
"""
    bst1 = CarInventory()

    car1 = Car("Mazda", "CX-5", 2022, 25000)
    car2 = Car("Tesla", "Model3", 2018, 50000)
    car3 = Car("BMW", "X5", 2022, 60000)
    car4 = Car("BMW", "X5", 2020, 58000)
    car5 = Car("Audi", "A3", 2021, 25000)

    bst1.addCar(car1)
    bst1.addCar(car2)
    bst1.addCar(car3)
    bst1.addCar(car4)
    bst1.addCar(car5)


    bst1.removeCar("BMW", "X5", 2020, 58000)

    assert bst1.inOrder() == \
"""\
Make: AUDI, Model: A3, Year: 2021, Price: $25000
Make: BMW, Model: X5, Year: 2022, Price: $60000
Make: MAZDA, Model: CX-5, Year: 2022, Price: $25000
Make: TESLA, Model: MODEL3, Year: 2018, Price: $50000
"""
    bst1.removeCar("BMW", "X5", 2022, 60000)
    assert bst1.inOrder() == \
"""\
Make: AUDI, Model: A3, Year: 2021, Price: $25000
Make: MAZDA, Model: CX-5, Year: 2022, Price: $25000
Make: TESLA, Model: MODEL3, Year: 2018, Price: $50000
"""


def test__preOrder():
    bst = CarInventory()

    car1 = Car("Nissan", "Leaf", 2018, 18000)
    car2 = Car("Tesla", "Model3", 2018, 50000)
    car3 = Car("Mercedes", "Sprinter", 2022, 40000)
    car4 = Car("Mercedes", "Sprinter", 2014, 25000)
    car5 = Car("Ford", "Ranger", 2021, 25000)

    bst.addCar(car1)
    bst.addCar(car2)
    bst.addCar(car3)
    bst.addCar(car4)
    bst.addCar(car5)

    assert bst.preOrder() == \
"""\
Make: NISSAN, Model: LEAF, Year: 2018, Price: $18000
Make: MERCEDES, Model: SPRINTER, Year: 2022, Price: $40000
Make: MERCEDES, Model: SPRINTER, Year: 2014, Price: $25000
Make: FORD, Model: RANGER, Year: 2021, Price: $25000
Make: TESLA, Model: MODEL3, Year: 2018, Price: $50000
"""
    bst1 = CarInventory()

    car1 = Car("Mazda", "CX-5", 2022, 25000)
    car2 = Car("Tesla", "Model3", 2018, 50000)
    car3 = Car("BMW", "X5", 2022, 60000)
    car4 = Car("BMW", "X5", 2020, 58000)
    car5 = Car("Audi", "A3", 2021, 25000)

    bst1.addCar(car1)
    bst1.addCar(car2)
    bst1.addCar(car3)
    bst1.addCar(car4)
    bst1.addCar(car5)


    bst1.removeCar("BMW", "X5", 2020, 58000)

    assert bst1.preOrder() == \
"""\
Make: MAZDA, Model: CX-5, Year: 2022, Price: $25000
Make: BMW, Model: X5, Year: 2022, Price: $60000
Make: AUDI, Model: A3, Year: 2021, Price: $25000
Make: TESLA, Model: MODEL3, Year: 2018, Price: $50000
"""
    bst1.removeCar("BMW", "X5", 2022, 60000)

    assert bst1.preOrder() == \
"""\
Make: MAZDA, Model: CX-5, Year: 2022, Price: $25000
Make: AUDI, Model: A3, Year: 2021, Price: $25000
Make: TESLA, Model: MODEL3, Year: 2018, Price: $50000
"""


def test__postOrder():
    bst = CarInventory()

    car1 = Car("Nissan", "Leaf", 2018, 18000)
    car2 = Car("Tesla", "Model3", 2018, 50000)
    car3 = Car("Mercedes", "Sprinter", 2022, 40000)
    car4 = Car("Mercedes", "Sprinter", 2014, 25000)
    car5 = Car("Ford", "Ranger", 2021, 25000)

    bst.addCar(car1)
    bst.addCar(car2)
    bst.addCar(car3)
    bst.addCar(car4)
    bst.addCar(car5)

    assert bst.postOrder() == \
"""\
Make: FORD, Model: RANGER, Year: 2021, Price: $25000
Make: MERCEDES, Model: SPRINTER, Year: 2022, Price: $40000
Make: MERCEDES, Model: SPRINTER, Year: 2014, Price: $25000
Make: TESLA, Model: MODEL3, Year: 2018, Price: $50000
Make: NISSAN, Model: LEAF, Year: 2018, Price: $18000
"""
    bst1 = CarInventory()

    car1 = Car("Mazda", "CX-5", 2022, 25000)
    car2 = Car("Tesla", "Model3", 2018, 50000)
    car3 = Car("BMW", "X5", 2022, 60000)
    car4 = Car("BMW", "X5", 2020, 58000)
    car5 = Car("Audi", "A3", 2021, 25000)

    bst1.addCar(car1)
    bst1.addCar(car2)
    bst1.addCar(car3)
    bst1.addCar(car4)
    bst1.addCar(car5)


    bst1.removeCar("BMW", "X5", 2020, 58000)

    assert bst1.postOrder() == \
"""\
Make: AUDI, Model: A3, Year: 2021, Price: $25000
Make: BMW, Model: X5, Year: 2022, Price: $60000
Make: TESLA, Model: MODEL3, Year: 2018, Price: $50000
Make: MAZDA, Model: CX-5, Year: 2022, Price: $25000
"""
    bst1.removeCar("BMW", "X5", 2022, 60000)
    assert bst1.postOrder() == \
"""\
Make: AUDI, Model: A3, Year: 2021, Price: $25000
Make: TESLA, Model: MODEL3, Year: 2018, Price: $50000
Make: MAZDA, Model: CX-5, Year: 2022, Price: $25000
"""



def test__doesCarExist():
    bst = CarInventory()

    car1 = Car("Nissan", "Leaf", 2018, 18000)
    car2 = Car("Tesla", "Model3", 2018, 50000)
    car3 = Car("Mercedes", "Sprinter", 2022, 40000)
    car4 = Car("Mercedes", "Sprinter", 2014, 25000)
    car5 = Car("Ford", "Ranger", 2021, 25000)

    bst.addCar(car1)
    bst.addCar(car2)
    bst.addCar(car3)
    bst.addCar(car4)
    bst.addCar(car5)

    search = Car("Mercedes", "Sprinter", 2014, 25000)
    search_1 = Car("Ford", "Explorer", 2021, 25000)
    assert bst.doesCarExist(search) == True
    assert bst.doesCarExist(search_1) == False
    

def test__getBestCar():
    bst = CarInventory()

    car1 = Car("Nissan", "Leaf", 2018, 18000)
    car2 = Car("Tesla", "Model3", 2018, 50000)
    car3 = Car("Mercedes", "Sprinter", 2022, 40000)
    car4 = Car("Mercedes", "Sprinter", 2014, 25000)
    car5 = Car("Ford", "Ranger", 2021, 25000)

    bst.addCar(car1)
    bst.addCar(car2)
    bst.addCar(car3)
    bst.addCar(car4)
    bst.addCar(car5)

    assert bst.getBestCar("Mercedes", "Sprinter") == car3

def test__getWorstCar():
    bst = CarInventory()

    car1 = Car("Nissan", "Leaf", 2018, 18000)
    car2 = Car("Tesla", "Model3", 2018, 50000)
    car3 = Car("Mercedes", "Sprinter", 2022, 40000)
    car4 = Car("Mercedes", "Sprinter", 2014, 25000)
    car5 = Car("Ford", "Ranger", 2021, 25000)

    bst.addCar(car1)
    bst.addCar(car2)
    bst.addCar(car3)
    bst.addCar(car4)
    bst.addCar(car5)

    assert bst.getWorstCar("Mercedes", "Sprinter") == car4

def test__getTotalInventoryPrice():
    bst = CarInventory()

    car1 = Car("Nissan", "Leaf", 2018, 18000)
    car2 = Car("Tesla", "Model3", 2018, 50000)
    car3 = Car("Mercedes", "Sprinter", 2022, 40000)
    car4 = Car("Mercedes", "Sprinter", 2014, 25000)
    car5 = Car("Ford", "Ranger", 2021, 25000)

    bst.addCar(car1)
    bst.addCar(car2)
    bst.addCar(car3)
    bst.addCar(car4)
    bst.addCar(car5)

    assert bst.getTotalInventoryPrice() == 158000



