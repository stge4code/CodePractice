class ExtendedStack(list):
    def sum(self):
        # операция сложения
        item1 = self.pop()
        item2 = self.pop()
        self.append(item1 + item2)

    def sub(self):
        # операция вычитания
        item1 = self.pop()
        item2 = self.pop()
        self.append(item1 - item2)

    def mul(self):
        # операция умножения
        item1 = self.pop()
        item2 = self.pop()
        self.append(item1 * item2)

    def div(self):
        # операция целочисленного деления
        item1 = self.pop()
        item2 = self.pop()
        self.append(item1 // item2)