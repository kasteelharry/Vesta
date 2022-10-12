import sys
import socket
import os
from src import PingServer
from src import CheckLogs

try:
    # Create the log folder if it doesn't exist yet.
    if not os.path.exists("vesta-logs"):
        os.makedirs("vesta-logs")
    # Check if there was a log made in the last 30 minutes.
    # If there was a file made, halt execution.
    if CheckLogs.checkLogs():
        sys.exit(0)
    # Convert the port number and if incorrect let the user know.
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