class Crypter():
    def __init__(self, alphabet, keys):
        self.alphtokeys = {}
        self.keystoalph = {}
        for i in range(len(alphabet)):
            self.alphtokeys[alphabet[i]] = keys[i]
            self.keystoalph[keys[i]] = alphabet[i]
    def encrypt(self, S):
        result = []
        for item in S:
            result.append(self.alphtokeys[item])
        return ''.join(result)
    def decrypt(self, S):
        result = []
        for item in S:
            result.append(self.keystoalph[item])
        return ''.join(result)

alphabet, keys = input(), input()
crypter = Crypter(alphabet, keys)
print(crypter.encrypt(input()))
print(crypter.decrypt(input()))