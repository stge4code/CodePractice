printer = {
    True: "Счастливый",
    False: "Обычный"
}
def listGen(x):
    counter = 6
    x_tmp = x
    while counter > 0:
        yield x_tmp % 10
        x_tmp = (x_tmp - x_tmp % 10) // 10
        counter -= 1
def check(mass):
    sum_l, sum_r = 0, 0
    for i in range(3):
        sum_l += mass[i]
        sum_r += mass[i + 3]
    return sum_l == sum_r
x = list(listGen(int(input())))
print(printer[check(x)])