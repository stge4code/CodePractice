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
y = IntInput(1).__next__()
if (y % 4 == 0 and y % 100 != 0) or y % 400 == 0:
    print("Високосный")
else:
    print("Обычный")