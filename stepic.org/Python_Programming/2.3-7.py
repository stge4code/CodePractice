a, b = (int(input()) for i in range(2))
sum = 0
counter = 0
for i in range(a, b + 1):
    if i % 3 == 0:
        counter += 1
        sum += i
print(sum / counter)