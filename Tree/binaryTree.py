class binaryTree(object):
    def __init__(self, value):
        self.value = value
        self.leftBranch = None
        self.rightBranch = None
        self.parent = None

    def setLeftBranch(self, node):
        self.leftBranch = node

    def setRightBranch(self, node):
        self.rightBranch = node

    def setParent(self, parent):
        self.parent = parent

    def getValue(self):
        return self.value

    def getLeftBranch(self):
        return self.leftBranch

    def getRightBranch(self):
        return self.rightBranch

    def getParent(self):
        return self.parent

    def __str__(self):
        return self.value


def DFSBinary(root, fcn):
    queue = [root]
    while len(queue) > 0:
        print('at node ' + str(queue[0].getValue()))
        if fcn(queue[0]):
            return True
        else:
            temp = queue.pop(0)
            if temp.getRightBranch():
                queue.insert(0, temp.getRightBranch())
            if temp.getLeftBranch():
                queue.insert(0, temp.getLeftBranch())
    return False


def BFSBinary(root, fcn):
    queue = [root]
    while len(queue) > 0:
        print('at node ' + str(queue[0].getValue()))
        if fcn(queue[0]):
            return True
        else:
            temp = queue.pop(0)
            if temp.getLeftBranch():
                queue.append(temp.getLeftBranch())
            if temp.getRightBranch():
                queue.append(temp.getRightBranch())
    return False


# creating the nodes
n5 = binaryTree(5)
n2 = binaryTree(2)
n1 = binaryTree(1)
n4 = binaryTree(4)
n8 = binaryTree(8)
n6 = binaryTree(6)
n7 = binaryTree(7)
n3 = binaryTree(3)

# constructing the tree
n5.setLeftBranch(n2)
n2.setParent(n5)
n5.setRightBranch(n8)
n8.setParent(n5)
n2.setLeftBranch(n1)
n1.setParent(n2)
n2.setRightBranch(n4)
n4.setParent(n2)
n8.setLeftBranch(n6)
n6.setParent(n8)
n6.setRightBranch(n7)
n7.setParent(n6)
n4.setLeftBranch(n3)
n3.setParent(n4)


def find6(node):
    return node.getValue() == 6


def find10(node):
    return node.getValue() == 10


def find2(node):
    return node.getValue() == 2


def lt6(node):
    return node.getValue() > 6


# test examples

print('DFS')
print(DFSBinary(n5, find6))


##print('')
##print('BFS')
##BFSBinary(n5, find6)


## if we wanted to return the path that got to the goal, would need to modify

def DFSBinaryPath(root, fcn):
    queue = [root]
    while len(queue) > 0:
        if fcn(queue[0]):
            return TracePath(queue[0])
        else:
            temp = queue.pop(0)
            if temp.getRightBranch():
                queue.insert(0, temp.getRightBranch())
            if temp.getLeftBranch():
                queue.insert(0, temp.getLeftBranch())
    return False


def TracePath(node):
    if not node.getParent():
        return [node]
    else:
        return [node] + TracePath(node.getParent())
