import socket
inp = '0'
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("127.0.0.1", 1234))
while inp != 'exit':
    s.send(inp.encode())
    print(s.recv(1024).decode())
    inp = input()
s.close()