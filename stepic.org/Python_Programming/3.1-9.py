def deleter(l):
    L = len(l)
    for i in range(L):
        if l[i] % 2 != 0:
            l.remove(l[i])
            return deleter(l)

def modify_list(l):
    deleter(l)
    L = len(l)
    for i in range(L):
        l[i] = l[i] // 2



lst = [1, 2, 3, 4, 5, 6]
print(modify_list(lst))  # None
print(lst)               # [1, 2, 3]
modify_list(lst)
print(lst)               # [1]

lst = [10, 5, 8, 3]
modify_list(lst)
print(lst)               # [5, 4]