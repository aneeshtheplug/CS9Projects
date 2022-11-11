from CarInventoryNode import CarInventoryNode
from Car import Car
class CarInventory:
    def __init__(self):
        self.root = None
    
    def addCar(self, car):
        if self.root:
            self._put(car,self.root)
        else:
            self.root = CarInventoryNode(car)
    
    def _put(self, car, currentNode):
        if car == currentNode:
            currentNode.cars.append(car)
        elif car < currentNode:
            if currentNode.left != None:
                self._put(car, currentNode.left)
            else:
                new_node = CarInventoryNode(car)
                currentNode.setLeft(new_node)
                new_node.setParent(currentNode)
        else:
            if currentNode.right != None:
                self._put(car, currentNode.right)
            else:
                new_node = CarInventoryNode(car)
                currentNode.setRight(new_node)
                new_node.setParent(currentNode)

    def _inOrder(self, node):
        ret = ""
        if node != None:
            ret += self._inOrder(node.getLeft())
            ret += str(node)
            ret += self._inOrder(node.getRight())
        return ret

    def inOrder(self):
        return self._inOrder(self.root)
    
    def _preOrder(self,node):
        ret = ""
        if node != None:
            ret += str(node)
            ret += self._preOrder(node.getLeft())
            ret += self._preOrder(node.getRight())
        return ret
        
    def preOrder(self):
        return self._preOrder(self.root)
    
    def _postOrder(self, node):
        ret = ""
        if node != None:
            ret += self._postOrder(node.getLeft())
            ret += self._postOrder(node.getRight())
            ret += str(node)
        return ret

    def postOrder(self):
        return self._postOrder(self.root)
    
    def _get(self, car, node):
        temp_node = CarInventoryNode(car)
        if temp_node == node:
            for i in node.cars:
                if i == car:
                    return True
            return False
        elif car < node:
            if node.left != None:
                return self._get(car, node.getLeft())
            else:
                return False
        else:
            if node.right != None:
                return self._get(car, node.getRight())
            else:
                return False

    def doesCarExist(self, car):
        if self.root:
            return self._get(car, self.root) 
        return False
    
    def _getCar(self, temp, current):
        if current == None:
            return None
        if temp == current:
            return current
        elif temp < current:
            return self._getCar(temp, current.getLeft())
        else:
            return self._getCar(temp, current.getRight())

    def getBestCar(self, make, model):
        temp_car = Car(make, model, 0, 0)
        temp_node = CarInventoryNode(temp_car)
        res = self._getCar(temp_node, self.root)
        if res:
            best = res.cars[0]
            for car in res.cars:
                if car > best:
                    best = car
            return best
        else:
            return res

    def getWorstCar(self, make, model):
        temp_car = Car(make, model, 0, 0)
        temp_node = CarInventoryNode(temp_car)
        res = self._getCar(temp_node, self.root)
        if res:
            worst = res.cars[0]
            for car in res.cars:
                if car < worst:
                    worst = car
            return worst
        else:
            return res
    
    def _getTotalInventoryPrice(self, node):
        total_price = 0
        if node != None:
            for car in node.cars:
                total_price += car.price
            total_price += self._getTotalInventoryPrice(node.getLeft())
            total_price += self._getTotalInventoryPrice(node.getRight())
        return total_price

    def getTotalInventoryPrice(self):
        return self._getTotalInventoryPrice(self.root)
