classesTree = {"object":{}}
printer = ['No', 'Yes']

def dicgen(num, *items):
    result = []
    for i in range(num):
        result.append([])
    for i in range(len(items)):
        result[i] = items[i]
    return result

def diccopy(mass):
    mass_tmp = []
    for item in mass:
        mass_tmp.append(item)
    return mass_tmp

def dicincrease(mass, masstoadd):
    mass_tmp = diccopy(mass)
    mass_tmp.append(masstoadd)
    return mass_tmp

def srch(node, classesTree, result, path = ["None"], nodes = []):
    nodes_tmp = dicincrease(nodes, classesTree)
    for key in classesTree:
        path_tmp = dicincrease(path, key)
        if key == node:
            result.append(dicgen(2, path_tmp, dicincrease(nodes_tmp, classesTree[key])))
        srch(node, classesTree[key], result, path_tmp, nodes_tmp)


def make(child, parent, classesTree):
    result = dicgen(0)
    srch(parent, classesTree, result)
    for item in result:
        tree = item[1]
        node = tree[len(tree) - 1]
        if not (child in node):
            node[child] = {}

def create(mass, classesTree):
    if len(mass) == 1:
        make(mass[0].strip(), "object", classesTree)
    else:
        for i in range(1, len(mass)):
            result = dicgen(0)
            srch(mass[i].strip(), classesTree, result)
            if len(result) == 0:
                make(mass[i].strip(), "object", classesTree)
            make(mass[0].strip(), mass[i].strip(), classesTree)

def test(mass, classesTree):
    parent = mass[0].strip()
    child = mass[1].strip()
    result_child = dicgen(0)
    srch(child, classesTree, result_child)
    result = "None"
    for item in result_child:
        names = item[0]
        nodes = item[1]
        if parent in names:
            return 1
    return 0

def makeclassmass(mass):
    result = []
    for item in mass:
        if item != ':':
            result.append(item)
    return result


for i in range(int(input())):
    create(makeclassmass(input().split(' ')), classesTree)
print(classesTree)
for i in range(int(input())):
    print(printer[test(makeclassmass(input().split(' ')), classesTree)])