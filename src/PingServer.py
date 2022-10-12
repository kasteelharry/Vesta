import socket
import sys
from src import SendEmail
from datetime import datetime

def pingServer(url, port, host=None):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    result = sock.connect_ex((url, port))
    if result == 0:
        print("Port is open")
    else:
        print("Connection failed, sending email")
        if host == None:
            host = url
        SendEmail.sendMail(url, datetime.now().time(), host, port)