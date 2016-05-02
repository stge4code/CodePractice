def LSM(a, b):
    x = a * b
    result = x
    while x > 0:
        if (x % a == 0) and (x % b == 0):
            if result >= x:
                result = x
        x -= 1
    return result
a, b = int(input()), int(input())
print(LSM(a, b))