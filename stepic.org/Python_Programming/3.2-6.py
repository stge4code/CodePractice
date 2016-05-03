def dictitizer(S):
    D = {}
    for item in S:
        if item in D:
            D[item] += 1
        else:
            D[item] = 1
    return D
S = input().lower().split()
D = dictitizer(S)
for key, value in D.items():
    print(key, value)