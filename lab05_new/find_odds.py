class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def getData(self):
        return self.data

    def getNext(self):
        return self.next

    def setData(self, newData):
        self.data = newData

    def setNext(self, newNext):
        self.next = newNext

class LinkedList:
    def __init__(self):
        self.head = None

    def addToFront(self, item):
        temp = Node(item)
        temp.setNext(self.head)
        self.head = temp

    def collectOdds(self):
        odds = []
        temp = self.head
        if temp == None:
            return odds
        else:
            while temp != None:
                if temp.getData() % 2 == 1:
                    odds.insert(0, temp.getData())
                    temp = temp.getNext()
                else:
                    temp = temp.getNext()
            return odds

ll = LinkedList()
assert ll.collectOdds() == []
ll.addToFront(6)
assert ll.collectOdds() == []
ll.addToFront(5)
ll.addToFront(3)
assert ll.collectOdds() == [5,3]
ll.addToFront(1)
ll.addToFront(8)
assert ll.collectOdds() == [5,3,1]
