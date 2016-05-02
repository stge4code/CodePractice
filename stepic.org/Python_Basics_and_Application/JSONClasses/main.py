import json

class Node:
    def __init__(self, name):
        self.name = name
        self.parents = []
        self.childscounter = 0

    def addparent(self, parent):
        if parent not in self.parents:
            self.parents.append(parent)
            Node.childscounterincr(parent)

    def childscounterincr(node):
        node.childscounter += 1
        for parent in node.parents:
            Node.childscounterincr(parent)


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
            result.append(str(node.name) + " : " + str(node.childscounter + 1))
        for item in sorted(result):
            print(item)

#tree = Tree(test1.loads(input()))


with open("test2") as f:
    tree = Tree(json.load(f))

tree.printchildscount()