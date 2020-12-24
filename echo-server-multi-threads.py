import socket
import threading

HOST = '127.0.0.1'  # Standard loopback interface address (localhost)
PORT = 65433        # Port to listen on (non-privileged ports are > 1023)


def handle_connection(conn, addr):
    with conn:
        while True:
            data = conn.recv(1024)
            print(f'recv: {addr} => {data}')
            if not data:
                break
            conn.sendall(data)


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    print('bind')
    s.bind((HOST, PORT))
    print('listen')
    s.listen()

    while True:
        print('accept')
        conn, addr = s.accept()

        print('connected: ', addr)
        conn_thread = threading.Thread(target=handle_connection, args=(conn, addr))
        conn_thread.start()
