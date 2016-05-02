class SumIntInput:
    def __init__(self):
        self.sum = 0
    def __iter__(self):
        return self
    def __next__(self):
        result = int(input())
        if result != 0:
            self.sum += result
            return self.sum
        else:
            raise StopIteration()
item = 0
for item in SumIntInput():
    pass
print(item)