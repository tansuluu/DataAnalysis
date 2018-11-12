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

