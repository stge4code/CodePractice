def sumgen(i, j, imax, jmax):
    if i > 0:
        yield [i - 1, j]
    else:
        yield [imax, j]
    if i < imax:
        yield [i + 1, j]
    else:
        yield [0, j]

    if j < jmax:
        yield [i, j + 1]
    else:
        yield [i, 0]
    if j > 0:
        yield [i, j - 1]
    else:
        yield [i, jmax]
matrix = []
line = input()
while line != "end":
    matrix.append([int(x) for x in line.split()])
    line = input()
result = []
for i in range(len(matrix)):
    resultline = []
    for j in range(len(matrix[i])):
        sum = 0
        for item in sumgen(i, j, len(matrix) - 1, len(matrix[i]) - 1):
            sum += matrix[item[0]][item[1]]
        resultline.append(str(sum))
    result.append(resultline)
for i in range(len(result)):
    print("\t".join(result[i]))