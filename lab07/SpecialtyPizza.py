from Pizza import Pizza
class SpecialtyPizza(Pizza):
    def __init__(self, size, name):
        super().__init__(size)
        self.name = name
        if self.size == "S":
            self.price = 12.00
        elif self.size == "M":
            self.price = 14.00
        else:
            self.price = 16.00

    def getPizzaDetails(self):
        new_line = '\n'
        return f'SPECIALTY PIZZA{new_line}Size: {self.size}{new_line}Name: {self.name}{new_line}Price: ${self.price:.2f}{new_line}'
