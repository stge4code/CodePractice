def f(x):
    if x <= -2:
        return 1 - (x + 2) ** 2
    elif -2 < x <= 2:
        return - x / 2.0
    else:
       return  (x - 2) ** 2 + 1