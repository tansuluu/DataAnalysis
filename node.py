
class Node:
    def __init__(self, value):
        self.value = value
        self.leftChild = None
        self.rightChild = None

    def get_leftChild(self):
        return self.leftChild

    def get_rightChild(self):
        return self.rightChild

    def get_value(self):
        return self.value

    def set_leftChild(self, newValue):
        self.leftChild = newValue

    def set_rightChild(self, newValue):
        self.rightChild = newValue

    def set_value(self, newValue):
        self.value = newValue

    def __str__(self) -> str:
        return super().__str__()

class BinaryTree:
    root = None

    def addNode(self,root, value):
        if root.get_value() == None:
            root = Node(value)
        elif root.get_value() > value:
            addNode(root.get_leftChild(), value)
        else:
            addNode(root.get_rightChild(), value)

    def add(self,value):
        addNode(root, value)


add(6)
add(3)
add(5)




