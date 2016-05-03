import numpy
def ciclereplacement(flags):
    maxindex = len(flags) - 1
    temp = flags[maxindex]
    for i in range(maxindex, 0, -1):
        flags[i] = flags[i - 1]
    flags[0] = temp

def gensteps():
    num = 1
    while True:
        yield [num, num, num + 1]
        yield [num + 1, num + 2, num + 2]
        num += 3

def generatepair1(pair, r, pairs, flag):
    if flag == 'u': #вверх
        for incr in range(r):
            pair[0] += 1
            if (pair[0], pair[1]) not in pairs:
                pairs.append((pair[0], pair[1]))
    elif flag == 'd': #вниз
        for incr in range(r):
            pair[0] += -1
            if (pair[0], pair[1]) not in pairs:
                pairs.append((pair[0], pair[1]))
    elif flag == 'r': #вправо
        for incr in range(r):
            pair[1] += +1
            if (pair[0], pair[1]) not in pairs:
                pairs.append((pair[0], pair[1]))
    elif flag == 'l': #влево
        for incr in range(r):
            pair[1] += -1
            if (pair[0], pair[1]) not in pairs:
                pairs.append((pair[0], pair[1]))

def generatepair(pair, r, pairs, flag):
    if flag == 'u': #вверх
        for incr in range(r):
            pair[0] += -1
            if (pair[0], pair[1]) not in pairs:
                pairs.append((pair[0], pair[1]))
    elif flag == 'd': #вниз
        for incr in range(r):
            pair[0] += 1
            if (pair[0], pair[1]) not in pairs:
                pairs.append((pair[0], pair[1]))
    elif flag == 'r': #вправо
        for incr in range(r):
            pair[1] += +1
            if (pair[0], pair[1]) not in pairs:
                pairs.append((pair[0], pair[1]))
    elif flag == 'l': #влево
        for incr in range(r):
            pair[1] += -1
            if (pair[0], pair[1]) not in pairs:
                pairs.append((pair[0], pair[1]))

def generatepath(value):
    pairs = [(0, 0)]
    pair = [0, 0]
    flags = ['l', 'd', 'r', 'u']
    value_temp = value
    for steps in gensteps():
        for i in range(3):
            if value_temp - steps[i] > 0:
                generatepair(pair, steps[i], pairs, flags[i])
                value_temp -= steps[i]
            else:
                generatepair(pair, value_temp, pairs, flags[i])
                return pairs
        ciclereplacement(flags)


def clearspace(space):
    result = []
    for i in range(indexes[6] + 1):
        temp = []
        for j in range(indexes[6] + 1):
            if space[i][j] != '0':
                temp.append(space[i][j])
        if len(temp) > 0:
            result.append(temp)
    return result

def makespace(indexes, path, value):
    space = []
    for i in range(indexes[6] + 1):
        space.append(['0' for j in range(indexes[6] + 1)])
    temp = value
    for pair in path:
        space[pair[0] - indexes[4]][pair[1] - indexes[4]] = str(temp)
        temp -= 1
    return space

def checkreverse(result):
    firstelement = result[0][0]
    if firstelement != '1':
        result.reverse()
        for item in result:
            item.reverse()
    return result
n = int(input())
value = numpy.power(n, 2)
path = generatepath(value)
indexes = [numpy.inf, -numpy.inf, numpy.inf, -numpy.inf, 0, 0, 0]
for pair in path:
    indexes[0] = min(pair[0], indexes[0])
    indexes[1] = max(pair[0], indexes[1])
    indexes[2] = min(pair[1], indexes[2])
    indexes[3] = max(pair[1], indexes[3])
    indexes[4] = min(indexes[0], indexes[2])
    indexes[5] = max(indexes[1], indexes[3])
    indexes[6] = indexes[5] - indexes[4]
result = checkreverse(clearspace(makespace(indexes, path, value)))
for item in result:
    print("\t".join(item))
