from find_odds import *
def test__collectOdds():
    ll = LinkedList()
    ll.collectOdds() == []
    ll.addToFront(6)
    ll.collectOdds() == []
    ll.addToFront(5)
    ll.addToFront(3)
    ll.collectOdds() == [5,3]
    ll.addToFront(1)
    ll.addToFront(8)
    ll.collectOdds() == [5,3,1]