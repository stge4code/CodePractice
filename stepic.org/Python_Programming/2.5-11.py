data = [int(i) for i in input().split()]
data.sort()
char = data[0]
counter = 0
for item in data:
    if char == item:
        counter += 1
    else:
        if counter > 1:
            print(char, end=' ')
        char = item
        counter = 1
if counter > 1:
    print(char, end=' ')