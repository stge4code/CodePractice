import socket
import threading, time
def receiver(s):
    while True:
        conn, addr = s.accept()
        while True:
            data = conn.recv(1024).decode()
            if not data: break
            conn.send(data.encode())
        conn.close()
    time.sleep(2)
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(("0.0.0.0", 2222))
s.listen(10)
threads = []
for i in range(10):
    threading.Thread(target=receiver, args=(s,)).start()
