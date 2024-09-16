
from socket import AF_INET, SOCK_STREAM, socket

def ip_address():
    sock = socket(AF_INET, SOCK_STREAM)
    sock.bind(('193.168.14.31', 80))
