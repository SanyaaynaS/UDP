import Client
import Server


DST_IP, DST_PORT, MTU, TIMEOUT = 'localhost', 8877, 1508, 10

if __name__ == '__main__':
    client1 = Client.Client('Alex', 8888, DST_PORT, DST_IP)
    client2 = Client.Client('Bob', 8889, DST_PORT, DST_IP)
    server = Server.Server(DST_PORT, DST_IP, MTU, TIMEOUT)

    server.start()
    client1.start()
    client2.start()

    client1.join()
    client2.join()
    server.join()
