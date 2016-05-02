import json

class Node:
    class Marker:
        def __init__(self):
            self.value = 0
        def incr(self):
            self.value += 1
            return self

    def __init__(self, name):
        self.name = name
        self.parents = []
        self.childs = []

    def addparent(self, parent):
        if parent not in self.parents:
            self.parents.append(parent)
 #           Node.addchild_(parent, self)
            Node.addchild(parent, self)

    def addchild(node, child):
        if child not in node.childs:
            node.childs.append(child)

    def getchildsnum(self):
        childlist = []
        Node.getchildslist(self, childlist)
        return len(childlist)

    def getchildslist(node, childlist):
        if node not in childlist:
            childlist.append(node)
        for child in node.childs:
            Node.getchildslist(child, childlist)


    def addchild_(node, child):
        if child not in node.childs:
            node.childs.append(child)
        for parent in node.parents:
            Node.addchild(parent, child)



class Tree:
    def __init__(self, data):
        self.nodes = {}
        for item in data:
            node = Node(item["name"])
            self.nodes[node.name] = node
        for item_node in data:
            node = self.nodes[item_node["name"]]
            for item_parent in item_node["parents"]:
                parent = self.nodes[item_parent]
                node.addparent(parent)
    def printchildscount(self):
        result = []
        for item in self.nodes:
            node = self.nodes[item]
            result.append(str(node.name) + " : " + str(node.getchildsnum()))
        for item in sorted(result):
            print(item)

#tree = Tree(json.loads(input()))


with open("test2") as f:
    tree = Tree(json.load(f))

tree.printchildscount()