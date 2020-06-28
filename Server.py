import hashlib
import select
import threading as th
from socket import *
import struct


def listen(server, receive_socket, tout):
    """
    This function is necessary for listening to the connection

    :param server: Server object
    :param receive_socket: server socket
    :param tout: timeout in seconds
    """

    while select.select([receive_socket], [], [], tout)[0]:
        rec_packet, addr = receive_socket.recvfrom(server.mtu)

        if rec_packet is not None:
            rec_info = struct.unpack('IIIq', rec_packet[:24])
            rec_data = struct.unpack('{}s'.format(len(rec_packet[24:])), rec_packet[24:])[0].decode('utf-8')

            server_checksum = int(hashlib.md5(rec_packet[:12] + rec_data.encode('utf-8')).hexdigest()[:6], 16)
            if htons(server_checksum) == rec_info[-1]:
                print('INFO:', 'src_ip: {}; src_port: {}'.format(addr[0], rec_info[0]), sep='\n')
                print('DATA:', rec_data, sep='\n')
                print('\n')
            else:
                print('Corrupted data\n')


class Server(th.Thread):
    """
    This class implements server side
    """

    def __init__(self, port, ip, mtu, tout):
        th.Thread.__init__(self)
        self.port = port
        self.ip = ip
        self.mtu = mtu
        self.tout = tout

    def run(self):
        receive_socket = socket(AF_INET, SOCK_DGRAM)
        receive_socket.bind((self.ip, self.port))
        listen(self, receive_socket, self.tout)
