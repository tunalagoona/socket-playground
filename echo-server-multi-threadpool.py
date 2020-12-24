import socket
from concurrent import futures

HOST = '127.0.0.1'  # Standard loopback interface address (localhost)
PORT = 65428        # Port to listen on (non-privileged ports are > 1023)


def handle_connection(conn, addr):
    with conn:
        while True:
            data = conn.recv(1024)
            print(f'recv: {addr} => {data}')
            if not data or data == b'exit\r\n':
                break
            conn.sendall(data)


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    print('bind')
    s.bind((HOST, PORT))
    print('listen')
    s.listen()

    with futures.ThreadPoolExecutor(max_workers=2) as executor:
        while True:
            print('accept')
            conn, addr = s.accept()
            print('connected: ', addr)
            executor.submit(handle_connection, conn=conn, addr=addr)
