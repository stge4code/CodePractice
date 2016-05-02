data = [int(i) for i in input().split()]
n = int(input())
index = 0
flag = True
for i in data:
    if i == n:
        flag = False
        print(index, end=' ')
    index += 1
if flag:
    print('Отсутствует')