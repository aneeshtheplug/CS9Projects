from CarInventoryNode import CarInventoryNode
from Car import Car
class CarInventory:
    def __init__(self):
        self.root = None
        self.size = 0

    def addCar(self,car):
        if self.root:
            self._put(car,self.root)
        else:
            self.root = CarInventoryNode(car)
            self.size = self.size + 1
            
    def _put(self,car,currentNode):
        new_node = CarInventoryNode(car)
        if new_node == currentNode:
            currentNode.cars.append(car)
        elif new_node < currentNode:
            if currentNode.left:
                self._put(car,currentNode.left)
            else:
                currentNode.left = new_node
                new_node.parent = currentNode
                self.size = self.size + 1
        else:
            if currentNode.right:
                self._put(car,currentNode.right)
            else:
                currentNode.right = new_node
                new_node.parent = currentNode
                self.size = self.size + 1

    def _inOrder(self, node):
        ret = ""
        if node:
            ret += self._inOrder(node.getLeft())
            ret += str(node)
            ret += self._inOrder(node.getRight())
        return ret

    def inOrder(self):
        return self._inOrder(self.root)
    
    def _preOrder(self,node):
        ret = ""
        if node:
            ret += str(node)
            ret += self._preOrder(node.getLeft())
            ret += self._preOrder(node.getRight())
        return ret
        
    def preOrder(self):
        return self._preOrder(self.root)
    
    def _postOrder(self, node):
        ret = ""
        if node:
            ret += self._postOrder(node.getLeft())
            ret += self._postOrder(node.getRight())
            ret += str(node)
        return ret

    def postOrder(self):
        return self._postOrder(self.root)
    
    def _getCar(self, temp, current):
        if not current:
            return None
        if temp == current:
            return current
        elif temp < current:
            return self._getCar(temp, current.getLeft())
        else:
            return self._getCar(temp, current.getRight())
            
    def doesCarExist(self,car):
        temp_node = CarInventoryNode(car)
        result = self._getCar(temp_node, self.root)
        if result:
            for i in range(len(result.cars)):
                if result.cars[i] == car:
                    return True
        return False
            

    def getBestCar(self, make, model):
        temp_car = Car(make, model, 0, 0)
        temp_node = CarInventoryNode(temp_car)
        result = self._getCar(temp_node, self.root)
        if result:
            best = result.cars[0]
            for car in result.cars:
                if car > best:
                    best = car
            return best
        return result

    def getWorstCar(self, make, model):
        temp_car = Car(make, model, 0, 0)
        temp_node = CarInventoryNode(temp_car)
        result = self._getCar(temp_node, self.root)
        if result:
            worst = result.cars[0]
            for car in result.cars:
                if car < worst:
                    worst = car
            return worst
        return result
    
    def _getTotalInventoryPrice(self, node):
        total_price = 0
        if node:
            for car in node.cars:
                total_price = total_price + car.price
            total_price += self._getTotalInventoryPrice(node.getLeft())
            total_price += self._getTotalInventoryPrice(node.getRight())
        return total_price

    def getTotalInventoryPrice(self):
        return self._getTotalInventoryPrice(self.root)
            
    def getSuccessor(self, make, model):
        temp_car = Car(make, model, 0, 0)
        temp_node = CarInventoryNode(temp_car)
        result = self._getCar(temp_node, self.root)
        if result:
            if result.right:
                result = result.right
                while result.left:
                    result = result.left
                return result
            if not result.parent:
                return None
            while result.parent:
                if result.parent.left == result:
                    return result.parent
                result = result.parent
            return None
        return result
    
    def removeCar(self, make, model, year, price):
        temp_car = Car(make, model, year, price)
        temp_node = CarInventoryNode(temp_car)
        result = self._getCar(temp_node, self.root)
        if result:
            for i in range(len(result.cars)):
                if result.cars[i] == temp_car:
                    result.cars.pop(i)
                    break
            if len(result.cars) == 0:
                return self.delete(result)
            else:
                return True
        return False

    def spliceOut(self, currentNode):
        if (currentNode.right is None) and (currentNode.left is None):
            if currentNode == currentNode.parent.left:
                currentNode.parent.left = None
            else:
                currentNode.parent.right = None
        else:
            if currentNode.right:
                if currentNode.parent.left == currentNode:
                    currentNode.parent.left = currentNode.right
                else:
                    currentNode.parent.right = currentNode.right
                currentNode.right.parent = currentNode.parent

    def delete(self,node):
        if self.size > 1:
            self.size = self.size - 1
            return self.deleteNode(node) # remove modifies the tree
        elif self.size == 1 and self.root == node:
            self.root = None
            self.size = self.size - 1
            return True
        else:
            raise KeyError('Error, key not in tree')

    def deleteNode(self, currentNode):
        if (currentNode.right is None) and (currentNode.left is None):
            if currentNode == currentNode.parent.left:
                currentNode.parent.left = None
                return True
            else:
                currentNode.parent.right = None
                return True
        elif (currentNode.right is not None) and (currentNode.left is not None):
             succ = self.getSuccessor(currentNode.make, currentNode.model)
             self.spliceOut(succ)
             currentNode.make = succ.make
             currentNode.model = succ.model
             currentNode.cars = succ.cars
             return True
        else:
            if currentNode.left:
                if currentNode.isLeftChild():
                    currentNode.left.parent = currentNode.parent
                    currentNode.parent.left = currentNode.left
                    return True
                elif currentNode.isRightChild():
                    currentNode.left.parent = currentNode.parent
                    currentNode.parent.right = currentNode.left
                    return True
                else:
                    currentNode.replaceNodeData(currentNode.left.make,
					currentNode.left.model,
					currentNode.left.cars,
					currentNode.left.left,
                    currentNode.left.right)
                    return True
            else:
                if currentNode.isLeftChild():
                    currentNode.right.parent = currentNode.parent
                    currentNode.parent.left = currentNode.right
                    return True
                elif currentNode.isRightChild():
                    currentNode.right.parent = currentNode.parent
                    currentNode.parent.right = currentNode.right
                    return True
                else:
                    currentNode.replaceNodeData(currentNode.right.make,
					currentNode.right.model,
					currentNode.right.cars,
					currentNode.right.left,
                    currentNode.right.right)
                    return True

