import threading
import time

import select
import sys
import tcp

print_lock = threading.Lock()


def print_message(mess):
    with print_lock:
        print(mess)


def create_thread_server(lock):
    ip = "127.0.0.1"
    port = 4445
    sub_port = 9000

    server = tcp.make_server(ip, port)
    if server is None:
        sys.exit(0)
    print("Starting server...")

    lock.set()

    client_nodes = {}
    num = 0

    while True:
        num = num + 1

        if num > 100:
            print("Process completed...")
            for client in client_nodes.values():
                tcp.close(client)
            break

        ready_sockets, _, _ = select.select([server] + list(client_nodes.values()), [], [], 0)

        if len(client_nodes) != 0:
            for client_conn in client_nodes.values():
                time.sleep(0.5)
                tcp.sendall(client_conn, num)

        for socket in ready_sockets:
            if socket == server:
                conn, _ = server.accept()
                sub_port = sub_port + 1
                client_nodes[sub_port] = conn
            else:
                message = socket.recv(1024).decode("utf-8")
                if message:
                    print_message(message)


def create_thread_client(lock, num):
    ip = "127.0.0.1"
    port = 4445

    lock.set()
    client = tcp.make_client()
    tcp.client_connect(client, ip, port)

    while True:
        message = tcp.rec(client, 1024)
        if message:
            number = int(message)
            if num == 3:
                if number % 3 == 0:
                    tcp.sendall(client, "ACK {} Divisible by 3!".format(number))
            if num == 5:
                if number % 5 == 0:
                    tcp.sendall(client, "ACK {} Divisible by 5!".format(number))


if __name__ == '__main__':
    lock_main = threading.Event()

    thread_server = threading.Thread(target=create_thread_server, args=(lock_main,))
    thread_client1 = threading.Thread(target=create_thread_client, args=(lock_main, 3))
    thread_client2 = threading.Thread(target=create_thread_client, args=(lock_main, 5))

    thread_server.start()
    thread_client1.start()
    thread_client2.start()

    thread_server.join()
    thread_client1.join()
    thread_client2.join()
