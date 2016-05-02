import numpy
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
def InRange(x):
    if (-15 < x <= 12) or (14 < x < 17) or (19 <= x):
        return True
    return False

x = IntInput(1).__next__()
print(InRange(x))