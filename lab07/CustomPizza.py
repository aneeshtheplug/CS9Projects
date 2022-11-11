from Pizza import Pizza
class CustomPizza(Pizza):
    def __init__(self, size):
        super().__init__(size)
        self.toppings = []
        if self.size == "S":
            self.price = 8.00
        elif self.size == "M":
            self.price = 10.00
        else:
            self.price = 12.00
    
    def addTopping(self,topping):
        if self.getSize() == "S":
            self.price += 0.50
            self.toppings.append(topping)
        elif self.getSize() == "M":
            self.price += 0.75
            self.toppings.append(topping)
        else:
            self.price += 1.00
            self.toppings.append(topping)
    
    def getPizzaDetails(self):
        new_line = '\n'
        new_tab = '\t'
        top_str = f'Toppings:{new_line}'
        if len(self.toppings) == 0:
            return f'CUSTOM PIZZA{new_line}Size: {self.size}{new_line}Toppings:{new_line}Price: ${self.price:.2f}{new_line}'
        else:
            top_str = f'Toppings:{new_line}'
            for i in range(len(self.toppings)):
                top_str += f'{new_tab}+ {self.toppings[i]}{new_line}'
            return f'CUSTOM PIZZA{new_line}Size: {self.size}{new_line}' + top_str + f'Price: ${self.price:.2f}{new_line}'
