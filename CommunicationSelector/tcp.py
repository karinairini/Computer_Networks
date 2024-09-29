import socket


def make_server(ip, port):
    try:
        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server.bind((ip, port))
        server.listen(10)
        return server
    except Exception as ex:
        print(ex)
        return None


def accept(server):
    conn, addr = server.accept()
    return conn


def make_client():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    return client


def client_connect(client, ip, port):
    client.connect((ip, port))


def sendall(conn, mess):
    conn.send(str(mess).encode())


def rec(conn, rate):
    mess = conn.recv(rate).decode()
    return mess


def close(client):
    client.close()
