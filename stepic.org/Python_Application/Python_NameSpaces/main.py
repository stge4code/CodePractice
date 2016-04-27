NMS = {"global.n":{}}

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

def getmaxitem(mass):
    result = mass[0]
    for item in mass:
        if len(result) <= len(item):
            result = item
    return result


def srch(nmsp, nms, result, path = ["None"], nodes = []):
    nodes_tmp = dicincrease(nodes, nms)
    for key in nms:
        path_tmp = dicincrease(path, key)
        if key == nmsp:
            result.append(dicgen(2, path_tmp, dicincrease(nodes_tmp, nms[key])))
        srch(nmsp, nms[key], result, path_tmp, nodes_tmp)


def make(a, b, nms):
    result = dicgen(0)
    srch(b, nms, result)
    for item in result:
        tree = item[1]
        node = tree[len(tree) - 1]
        if not (a in node):
            node[a] = {}

def create(nmsp, arg, nms):
    make(nmsp + ".n", arg + ".n", nms)

def add(nmsp, arg, nms):
    make(arg + ".v", nmsp + ".n", nms)

def get_(nmsp, arg, nms):
    result_arg = dicgen(0)
    srch(arg + ".v", nms, result_arg)
    result_nmsp = dicgen(0)
    srch(nmsp + ".n", nms, result_nmsp)
    str_result = [["None.*"]]
    for item_arg in result_arg:
        str_arg = item_arg[2].split('_')
        str_arg.pop()
        for item_nmsp in result_nmsp:
            str_nmsp = item_nmsp[2].split('_')
            str_nmsp.pop()
            if (len(str_arg) - len(str_nmsp)) < 2:
                i = 0
                str_result_tmp = []
                while str_nmsp[i] == str_arg[i]:
                    str_result_tmp.append(str_nmsp[i])
                    i += 1
                str_result.append(str_result_tmp)
    str_result = getmaxitem(str_result)
    print(str_result)
    print((str_result[len(str_result) - 1]).split('.')[0])

def get(nmsp, arg, nms):
    result_nmsp = dicgen(0)
    srch(nmsp + ".n", nms, result_nmsp)
    result = "None"
    for item in result_nmsp:
        names = item[0]
        nodes = item[1]
        for i in range(len(nodes)):
            if arg + ".v" in nodes[i]:
                result = names[i]
    print(result.split('.')[0])


HANDLER = {'create': create, 'get': get, 'add': add}
n = int(input())
for i in range(0, n):
    cmd, nmsp, arg = input().split()
    HANDLER[cmd](nmsp, arg, NMS)
#print(NMS)
