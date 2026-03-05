import socket

def server_program():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(('localhost', 18003))
    server.listen(1)

    conn, addr = server.accept()
    conn.send(b"Hello man")

    conn.close()
    server.close()

if __name__ == '__main__':
    server_program()