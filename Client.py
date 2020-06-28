import random
import time

from Utils import create_packet
import threading as th
from socket import *


class Client(th.Thread):
    """
    This class implements client side
    """

    def __init__(self, name, port, dst_port, dst_ip):
        th.Thread.__init__(self)
        self.name = name
        self.port = port
        self.dst_port = dst_port
        self.dst_ip = dst_ip

    def run(self):
        send_socket = socket(AF_INET, SOCK_DGRAM)
        data = 'Hello, I\'m ' + self.name
        time.sleep(random.randint(0, 5))
        transmit_datagram(self, send_socket, data)


def transmit_datagram(client, send_socket, data):
    """
    This function is necessary for transmitting UDP-datagram

    :param client: Client object
    :param send_socket: client socket
    :param data: data to send
    """
    packet = create_packet(client.port, client.dst_port, data)
    while packet:
        sent = send_socket.sendto(packet, (client.dst_ip, client.dst_port))
        packet = packet[sent:]
