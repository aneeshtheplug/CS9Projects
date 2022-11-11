from CustomPizza import CustomPizza
from SpecialtyPizza import SpecialtyPizza
from PizzaOrder import PizzaOrder
from OrderQueue import OrderQueue, QueueEmptyException
import pytest

def test__getPizzaDetails():
    cp1 = CustomPizza("S")
    assert cp1.getPizzaDetails() == \
    "CUSTOM PIZZA\n\
Size: S\n\
Toppings:\n\
Price: $8.00\n"

    cp2 = CustomPizza("L")
    cp2.addTopping("extra cheese")
    cp2.addTopping("sausage")

    assert cp2.getPizzaDetails() == \
    "CUSTOM PIZZA\n\
Size: L\n\
Toppings:\n\
\t+ extra cheese\n\
\t+ sausage\n\
Price: $14.00\n"

def test__getPizzaDetails1():
    sp1 = SpecialtyPizza("S", "Carne-more")
    assert sp1.getPizzaDetails() == \
    "SPECIALTY PIZZA\n\
Size: S\n\
Name: Carne-more\n\
Price: $12.00\n"

def test__getOrderDescription():
    cp1 = CustomPizza("S")
    cp1.addTopping("extra cheese")
    cp1.addTopping("sausage")
    sp1 = SpecialtyPizza("S", "Carne-more")
    order = PizzaOrder(123000) #12:30:00PM
    order.addPizza(cp1)
    order.addPizza(sp1)
    assert order.getOrderDescription() == \
    "******\n\
Order Time: 123000\n\
CUSTOM PIZZA\n\
Size: S\n\
Toppings:\n\
\t+ extra cheese\n\
\t+ sausage\n\
Price: $9.00\n\
\n\
----\n\
SPECIALTY PIZZA\n\
Size: S\n\
Name: Carne-more\n\
Price: $12.00\n\
\n\
----\n\
TOTAL ORDER PRICE: $21.00\n\
******\n"

def test__QueueEmptyException():
    with pytest.raises(QueueEmptyException):
        heap = OrderQueue()
        heap.processNextOrder() 

def test__processNextOrder():
    heap = OrderQueue()
    cp1 = CustomPizza("S")
    cp1.addTopping("extra cheese")
    cp1.addTopping("sausage")
    sp1 = SpecialtyPizza("S", "Carne-more")
    order = PizzaOrder(123000) #12:30:00PM
    order.addPizza(cp1)
    order.addPizza(sp1)
    heap.addOrder(order)
    assert heap.processNextOrder() == \
    "******\n\
Order Time: 123000\n\
CUSTOM PIZZA\n\
Size: S\n\
Toppings:\n\
\t+ extra cheese\n\
\t+ sausage\n\
Price: $9.00\n\
\n\
----\n\
SPECIALTY PIZZA\n\
Size: S\n\
Name: Carne-more\n\
Price: $12.00\n\
\n\
----\n\
TOTAL ORDER PRICE: $21.00\n\
******\n"