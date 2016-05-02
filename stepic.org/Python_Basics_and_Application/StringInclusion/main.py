s, a, b = (input() for i in range(3))
if (a in b) and (a in s):
    print("Impossible")
else:
    s_before = s_after = s
    count = -1
    while (s_before != s_after) or (count < 0):
        count += 1
        s_before = s_after
        s_after = s_before.replace(a, b)
    print(count)
