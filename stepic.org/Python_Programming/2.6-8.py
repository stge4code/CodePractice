n = int(input())
str_result = ''
counter = 0
for i in range(1, n + 1):
    for k in range(0, i):
        counter += 1
        if counter <= n:
            print(str(i), end=' ')
