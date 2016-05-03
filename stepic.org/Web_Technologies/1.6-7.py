import socket
import threading

class Semaphore():
    def __init__(self, maxcount):
        self.maxcount = maxcount
        self.count = self.maxcount
    def incr(self):
        if self.count < self.maxcount:
            self.count += 1
    def decr(self):
        if self.count > 0:
            self.count -= 1
    def check(self):
        if 0 <= self.count < self.maxcount:
            return True
        return False
    def get(self):
        return self.count

def receiver(conn, smph):
    smph.decr()
    print("In thread:", smph.get(), sep=' ')
    while True:
        data = conn.recv(1024).decode()
        if (not data) or (data == "close"): break
        conn.send(data.encode())
    conn.close()
    print("Out of thread:", smph.get(), sep=' ')
    smph.incr()
if __name__ == '__main__':
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(("127.0.0.1", 2222))
    smph = Semaphore(10)
    while True:
        if smph.get():
            s.listen()
            conn, addr = s.accept()
            t = threading.Thread(target=receiver, args=(conn, smph))
            t.start()
# https://github.com/stge4code/CodePractice/tree/master/stepic.org