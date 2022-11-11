from lab03 import *
def test_integerDivison():
    assert integerDivision(27,4) == 6
    assert integerDivision(0,4) == 0
    assert integerDivision(4,2) == 2
    assert integerDivision(10,10) == 1
    assert integerDivision(5,9) == 0

def test_collectEvenInts():
    assert collectEvenInts([1,2,3,4,5]) == [2,4]
    assert collectEvenInts([]) == []
    assert collectEvenInts([2,2,4]) == [2,2,4]
    assert collectEvenInts([1,3,5]) == []
    assert collectEvenInts([20]) == [20]

def test_countVowels():
    assert countVowels("This Is A String") == 4
    assert countVowels("") == 0
    assert countVowels("AAA") == 3
    assert countVowels("qwty") == 0
    assert countVowels("Space  between") == 5

def test_reverseString():
    assert reverseString("CMPSC9") == "9CSPMC"
    assert reverseString("") == ""
    assert reverseString("nitin") == "nitin"
    assert reverseString("test") == "tset"
    assert reverseString("h") == "h"

def test_removeSubString():
    assert removeSubString("Lolololol", "lol") == "Loo"
    assert removeSubString("sub", "subway") == "sub"
    assert removeSubString("hello", "he") == "llo"
    assert removeSubString("warriors", "want") == "warriors"

