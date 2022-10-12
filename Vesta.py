import sys
import socket
from src import PingServer

try:
    portNum = int(sys.argv[2])
    if portNum > 65535:
        raise ValueError("To big port value")
    if len(sys.argv) > 3:
        PingServer.pingServer(sys.argv[1], portNum, sys.argv[3])
    else:
        PingServer.pingServer(sys.argv[1], portNum)
except ValueError as e:
    print("Please enter a number between 0 and 65535 for the port.")
except socket.gaierror as e:
    print("Please enter a correctly formatted hostname or ip address.")