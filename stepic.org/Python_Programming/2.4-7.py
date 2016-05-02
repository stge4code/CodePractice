class Crypter:
    def __init__(self):
        pass
    def crypt(data):
        s = str(data)
        char = s[0]
        result = ''
        counter = 0
        for i in s:
            if char == i:
                counter += 1
            else:
                result += char + str(counter)
                counter = 1
                char = i
        result += char + str(counter)
        return result

print(Crypter.crypt(input()))

