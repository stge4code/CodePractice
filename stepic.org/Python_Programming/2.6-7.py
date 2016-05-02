s = int(input())
data = [s]
while s != 0:
    result = int(input())
    s += result
    data.append(result)
data_tmp = [i * i for i in data]
s = 0
for i in data_tmp:
    s += i
print(s)
