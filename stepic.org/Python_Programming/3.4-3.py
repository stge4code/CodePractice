def dictitizer(S):
    D = {}
    for item in S:
        if item in D:
            D[item] += 1
        else:
            D[item] = 1
    return D
filename = "dataset_3363_3.txt"
with open("files/" + filename) as file:
    S = file.read().lower().split()
D = dictitizer(S)
sD = sorted(D, key=lambda x:-D[x])
with open("files/" + "_" + filename, 'w') as file:
    file.write(sD[0] + ' ' + str(D[sD[0]]))