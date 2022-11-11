def index(self, item):
    temp = self.head
    counter = 0
    while temp!= None:
        if temp.getData() == item:
            return counter
        else:
            temp = temp.getNext()
            counter += 1
    return counter