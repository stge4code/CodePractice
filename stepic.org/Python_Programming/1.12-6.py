suffix = {
    0: 'а',
    1: '',
    2: "ов"
}
n = int(input())
preffix = "программист"
def genSpeak(n, preffix, suffix):
    i = n % 10
    d = n % 100
    if 10 < d < 21:
        return str(n) + ' ' + preffix + suffix[2]
    if i == 1:
        return str(n) + ' ' + preffix + suffix[1]
    elif 1 < i < 5:
        return str(n) + ' ' + preffix + suffix[0]
    else:
        return str(n) + ' ' + preffix + suffix[2]
print(genSpeak(n, preffix, suffix))