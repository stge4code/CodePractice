def update_dictionary(D, key, value):
    if key in D:
        D[key].append(value)
    elif 2 * key in D:
        D[2 * key].append(value)
    else:
        D[2 * key] = []
        D[2 * key].append(value)


d = {}
print(update_dictionary(d, 1, -1))  # None
print(d)                            # {2: [-1]}
update_dictionary(d, 2, -2)
print(d)                            # {2: [-1, -2]}
update_dictionary(d, 1, -3)
print(d)                            # {2: [-1, -2, -3]}