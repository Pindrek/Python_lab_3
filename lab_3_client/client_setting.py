import socket

def client_program():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(('localhost', 18003))

    data = client.recv(1024)
    print(data.decode())

    client.close()

if __name__ == '__main__':
    client_program()