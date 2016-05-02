def numgenerator(index, size):
    if size == 1:
        return [size - 1]
    if index == 0:
        return [size - 1, 1]
    if index == size - 1:
        return [size - 2, 0]
    return [index - 1, index + 1]
data = [int(i) for i in input().split()]
for i in range(len(data)):
    s = 0
    for k in numgenerator(i, len(data)):
        s += data[k]
    print(s, sep=' ',end=' ')