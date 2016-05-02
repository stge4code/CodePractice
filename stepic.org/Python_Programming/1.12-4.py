import numpy
def HeronsFormula(a, b, c):
    p = (a + b + c) / 2.0
    return numpy.sqrt(p * (p - a) * (p - b) * (p - c))

class ApartmentSquare:
    def __init__(self, apartment):
        self.apartment = apartment
        self.apartments = {'треугольник': self.T, 'прямоугольник': self.R, 'круг': self.C}
    def calculate(self):
        return self.apartments[self.apartment]()
    def T(self):
        a, b, c = float(input()), float(input()), float(input())
        return HeronsFormula(a, b, c)
    def R(self):
        a, b = float(input()), float(input())
        return a * b
    def C(self):
        r = float(input())
        return 3.14 * r * r

print(ApartmentSquare(str(input())).calculate())