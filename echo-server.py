import socket

HOST = '127.0.0.1'  # Standard loopback interface address (localhost)
PORT = 65432        # Port to listen on (non-privileged ports are > 1023)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    print('bind')
    s.bind((HOST, PORT))
    print('listen')
    s.listen()
    print('accept')
    conn, addr = s.accept()
    with conn:
        print('recv: ', addr)
        while True:
            data = conn.recv(1024)
            print('data: ', str(data))
            if not data:
                break
            conn.sendall(data)
