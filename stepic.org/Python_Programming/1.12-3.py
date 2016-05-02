import numpy
class Calculator:
    def __init__(self, a, b, cmd):
        self.a = a
        self.b = b
        self.cmd = cmd
        self.cmds = {'+': self.plus, '-': self.minus, '/': self.divide, '*': self.multiply, 'mod': self.divide_mod, 'pow': self.power, 'div': self.divide_div}
    def calculate(self):
        return self.cmds[self.cmd]()
    def plus(self):
        return self.a + self.b
    def minus(self):
        return self.a - self.b
    def multiply(self):
        return self.a * self.b
    def divide(self):
        if self.b != 0:
            return self.a / self.b
        else:
            return "Деление на 0!"
    def divide_mod(self):
        if self.b != 0:
            return self.a % self.b
        else:
            return "Деление на 0!"
    def power(self):
        return numpy.power(self.a, self.b)
    def divide_div(self):
        if self.b != 0:
            return self.a // self.b
        else:
            return "Деление на 0!"

a, b, cmd = float(input()), float(input()), str(input())
print(Calculator(a, b, cmd).calculate())