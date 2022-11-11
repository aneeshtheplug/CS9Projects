from Apartment import Apartment
from lab06 import *

def test__getRent():
    a0 = Apartment(1115, 215, "bad")
    assert a0.getRent() == 1115

def test__getMetersFromUCSB():
    a0 = Apartment(1115, 215, "bad")
    assert a0.getMetersFromUCSB() == 215

def test__getCondition():
    a0 = Apartment(1115, 215, "bad")
    assert a0.getCondition() == 'bad'  

def test__getApartmentDetails():
    a0 = Apartment(1115, 215, "bad")
    assert a0.getApartmentDetails() == "(Apartment) Rent: $1115, Distance From UCSB: 215m, Condition: bad"

def test__lt__():
    a0 = Apartment(1115, 215, "bad")
    a1 = Apartment(950, 215, "average")
    assert a1.__lt__(a0) == True

def test__gt__():
    a0 = Apartment(1115, 215, "bad")
    a1 = Apartment(950, 215, "average")
    assert a0.__gt__(a1) == True

def test__eq__():
    a0 = Apartment(950, 215, "average")
    a1 = Apartment(950, 215, "average")
    assert a0.__eq__(a1) == True


def test__ensureSortedAscending():
    a0 = Apartment(1115, 215, "bad")
    a1 = Apartment(950, 215, "average")
    a2 = Apartment(950, 215, "excellent")
    a3 = Apartment(950, 190, "excellent")
    a4 = Apartment(900, 190, "excellent")
    a5 = Apartment(500, 250, "bad")
    apartmentList = [a0, a1, a2, a3, a4, a5]
    assert ensureSortedAscending(apartmentList) == False
    mergesort(apartmentList)
    assert ensureSortedAscending(apartmentList) == True

def test__getBestApartment():
    a0 = Apartment(1200, 200, "average")
    a1 = Apartment(1200, 200, "excellent")
    a2 = Apartment(1000, 100, "average")
    a3 = Apartment(1000, 215, "excellent")
    a4 = Apartment(700, 315, "bad")
    a5 = Apartment(800, 250, "excellent")
    apartmentList = [a0, a1, a2, a3, a4, a5]
    assert(getBestApartment(apartmentList)) == "(Apartment) Rent: $700, Distance From UCSB: 315m, Condition: bad"

def test__getWorstApartment():
    a0 = Apartment(1200, 200, "average")
    a1 = Apartment(1200, 200, "excellent")
    a2 = Apartment(1000, 100, "average")
    a3 = Apartment(1000, 215, "excellent")
    a4 = Apartment(700, 315, "bad")
    a5 = Apartment(800, 250, "excellent")
    apartmentList = [a0, a1, a2, a3, a4, a5]
    assert(getWorstApartment(apartmentList)) == "(Apartment) Rent: $1200, Distance From UCSB: 200m, Condition: average"

def test__getAffordableApartments():
    a0 = Apartment(1115, 215, "bad")
    a1 = Apartment(970, 215, "average")
    a2 = Apartment(950, 215, "average")
    a3 = Apartment(950, 190, "excellent")
    a4 = Apartment(900, 190, "excellent")
    a5 = Apartment(500, 250, "bad")
    apartmentList = [a0, a1, a2, a3, a4, a5]
    assert getAffordableApartments(apartmentList, 950) == "(Apartment) Rent: $500, Distance From UCSB: 250m, Condition: bad" + '\n' + "(Apartment) Rent: $900, Distance From UCSB: 190m, Condition: excellent" + '\n' + "(Apartment) Rent: $950, Distance From UCSB: 190m, Condition: excellent" + '\n' + '(Apartment) Rent: $950, Distance From UCSB: 215m, Condition: average'
    assert getAffordableApartments(apartmentList, 450) == ''