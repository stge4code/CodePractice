import socket
import threading, time


def receiver(conn):
    while True:
        data = conn.recv(1024).decode()
        if not data: break
        conn.send(data.encode())
    conn.close()
if __name__ == '__main__':
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(("0.0.0.0", 2222))
    while True:
        s.listen()
        conn, addr = s.accept()
        t = threading.Thread(target=receiver, args=(conn,))
        t.start()
#https://github.com/stge4code/CodePractice.git