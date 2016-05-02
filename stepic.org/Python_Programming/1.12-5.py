class SortInput:
    def __init__(self, data):
        self.data = data
        self.counter = len(data)
    def __iter__(self):
        return self
    def __next__(self):
        if self.counter == 3:
            self.counter -= 1
            result = int(max(self.data))
            self.data.remove(result)
            return result
        elif self.counter == 2:
            self.counter -= 1
            result = int(min(self.data))
            self.data.remove(result)
            return result
        elif self.counter == 1:
            self.counter -= 1
            return int(self.data[0])
        else:
            raise StopIteration()
def generate(x):
    for i in range(x):
        yield float(input())
for item in SortInput(list(generate(3))):
    print(item)