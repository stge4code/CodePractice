def easten_ranger(a, b):
    for i in range(a, b):
        yield i

def western_ranger(a, b, c = 1):
    yield str(c)
    for i in range(a, b):
        yield str(i * c)

def ranger(a, b):
    yield ''
    for i in range(a, b):
        yield str(i)

i2i = lambda : int(input())
a, b, c, d = i2i(), i2i(), i2i(), i2i()
res = "\t".join(ranger(c, d + 1))
print(res)
for i in easten_ranger(a, b + 1):
    res = "\t".join(western_ranger(c, d + 1, i))
    print(res)