def mod_checker(x, mod=0):
    return lambda y: y % x == mod

mod_3 = mod_checker(3)

print(mod_3(3)) # True
print(mod_3(4)) # False

mod_3_1 = mod_checker(3, 1)
print(mod_3_1(4)) # True

a = []
lower = ''
offset = ''
upper = ''
offset = ''
step = ''
x = a[lower + offset : upper + offset]
x = a[lower:upper], a[lower:upper:], a[lower::step]
x = a[lower : : upper]
x = a[lower+offset : upper+offset]
x = a[lower + offset:upper + offset]