import socket
import sys

def pingServer(url, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    result = sock.connect_ex((url, port))
    if result == 0:
        print("Port is open")
    else:
        print("Connection failed")


try:
    portNum = int(sys.argv[2])
    if portNum > 65535:
        raise ValueError("To big port value")
    pingServer(sys.argv[1], portNum)
except ValueError as e:
    print("Please enter a number between 0 and 65535 for the port.")
except socket.gaierror as e:
    print("Please enter a correctly formatted hostname or ip address.")