printer = ['No', 'Yes']

class Marker():
    marker = None

    def __init__(self):
        self.marker = False

    def addValue(self, value):
        self.marker += value
        return self.marker

    def getValue(self):
        return self.marker

class Node:
    parents = None
    name = None

    def __init__(self, name, parent = object):
        self.name = name
        self.parents = [parent]

    def addParent(self, parent):
        if self.parents[0] == object:
            self.parents.pop()
        self.parents.append(parent)

    def getParents(self):
        return self.parents

class Tree:
    data = None

    def __init__(self):
        self.data = {}
#        self.addNode(object)
    def addNode(self, node):
        self.data[node.name] = node
    def getNode(self, name):
        if name in self.data:
            return self.data[name]
        return None
    def inNode(self, name):
        if name in self.data:
            return True
        return False

def create(nodes, tree):
    child = Node(nodes[0])
    if not tree.inNode(child.name):
        tree.addNode(child)
    else:
        child = tree.getNode(child.name)

    for i in range(1, len(nodes)):
        parent = Node(nodes[i])
        if not tree.inNode(parent.name):
            tree.addNode(parent)
        else:
            parent = tree.getNode(parent.name)
        child.addParent(parent)

def search(node, test_node, tree, result = Marker()):
    if node == object:
        return

    if node.name == test_node.name:
        result.addValue(True)
        return

    for item in node.getParents():
        search(item, test_node, tree, result)

def test(nodes, tree):
    child = tree.getNode(nodes[1])
    parent = tree.getNode(nodes[0])
    result = Marker()
    search(child, parent, tree, result)
    if result.getValue():
        return 1
    return 0

def makeInputMass(mass):
    result = []
    for item in mass:
        if item != ':':
            result.append(item)
    return result

tree = Tree()
for i in range(int(input())):
    create(makeInputMass(input().split(' ')), tree)
# print(tree)
for i in range(int(input())):
    print(printer[test(makeInputMass(input().split(' ')), tree)])