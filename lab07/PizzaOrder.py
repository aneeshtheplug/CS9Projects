from CustomPizza import CustomPizza
from SpecialtyPizza import SpecialtyPizza

class PizzaOrder:
    def __init__(self,time):
        self.pizzas = []
        self.time = time

    def getTime(self):
        return self.time
    
    def setTime(self,time):
        self.time = time
    
    def addPizza(self,pizza):
        self.pizzas.append(pizza)
    
    def getOrderDescription(self):
        new_line = '\n'
        pizza = f''
        total_price = 0
        for i in range(len(self.pizzas)):
            pizza += f'{self.pizzas[i].getPizzaDetails()}{new_line}----{new_line}'
            total_price += self.pizzas[i].getPrice()
        return f'******{new_line}Order Time: {self.time}{new_line}{pizza}TOTAL ORDER PRICE: ${total_price:.2f}{new_line}******{new_line}'