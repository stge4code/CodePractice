class IntInput:
    def __init__(self, size=3):
        self.size = size
    def __iter__(self):
        return self
    def __next__(self):
        if self.size > 0:
            self.size -= 1
            return int(input())
        else:
            raise StopIteration()
a, b, h = IntInput(3)
if h < a:
    print("Недосып")
elif h > b:
    print("Пересып")
else:
    print("Это нормально")
