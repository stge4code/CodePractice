import time

class Loggable:
    def log(self, msg):
        print(str(time.ctime()) + ": " + str(msg))

class LoggableList(list, Loggable):
    def __init__(self):
        pass

    def append(self, p_object):
        super().log(p_object)
        super().append(p_object)

lister = LoggableList()
lister.append('test')
