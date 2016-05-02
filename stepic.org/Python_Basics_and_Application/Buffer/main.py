class Buffer:
    counter = 5
    data = []

    def __init__(self):
        # конструктор без аргументов
        pass
    def add(self, *a):
        for item in a:
            if self.counter > 0:
                self.data.append(item)
                self.counter -= 1
            else:
                print(self.get_sum())
                self.counter = 5
                self.data = []
                self.data.append(item)
                self.counter -= 1
        if self.counter == 0:
            print(self.get_sum())
            self.counter = 5
            self.data = []
        # добавить следующую часть последовательности

    def get_current_part(self):
        print(self.data)
        return(self.data)
        # вернуть сохраненные в текущий момент элементы последовательности в порядке, в котором они были
        # добавлены
    def get_sum(self):
        sum = 0
        for item_data in self.data:
            sum += item_data
        return sum

buf = Buffer()
buf.add(1, 2, 3)
buf.get_current_part() # вернуть [1, 2, 3]
buf.add(4, 5, 6) # print(15) – вывод суммы первой пятерки элементов
buf.get_current_part() # вернуть [6]
buf.add(7, 8, 9, 10) # print(40) – вывод суммы второй пятерки элементов
buf.get_current_part() # вернуть []
buf.add(1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1) # print(5), print(5) – вывод сумм третьей и четвертой пятерки
buf.get_current_part() # вернуть [1]