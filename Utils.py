import struct
import socket
import hashlib


def create_packet(source_port, destination_port, data):
    """
    This function is necessary for constructing UDP-datagram

    :param source_port: source port
    :param destination_port: destination port
    :param data: payload
    :return: packet data
    """

    header = struct.pack('III', source_port, destination_port, 8 + len(data))
    my_checksum = int(hashlib.md5(header + data.encode('utf-8')).hexdigest()[:6], 16)
    header = struct.pack('IIIq', source_port, destination_port, 8 + len(data), socket.htons(my_checksum))
    return header + data.encode('utf-8')
