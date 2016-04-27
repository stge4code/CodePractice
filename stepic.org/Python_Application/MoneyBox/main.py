class MoneyBox:
    counter = 0
    capacity = 0

    def __init__(self, capacity):
        # конструктор с аргументом – вместимость копилки
        self.capacity = capacity

    def can_add(self, v):
        # True, если можно добавить v монет, False иначе
        if self.capacity >= self.counter + v:
            return True
        return False

    def add(self, v):
        # положить v монет в копилку
        self.counter += v