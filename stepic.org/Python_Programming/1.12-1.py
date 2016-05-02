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
def HeronsFormula(a, b, c):
    p = (a + b + c) / 2.0
    return numpy.sqrt(p * (p - a) * (p - b) * (p - c))

a, b, c = IntInput(3)
print(HeronsFormula(a, b, c))