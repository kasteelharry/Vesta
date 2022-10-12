import socket
import sys
from src import SendEmail
from datetime import datetime
import logging

def pingServer(url, port, host=None):
    """Pings the server and send an email if unreachable.
    
    This method pings the url and port passed as parameters. If the
    url and port are unreachable, the method will call SendEmail to
    send an email to the owner to inform them that the server is
    offline.
    """
    # Create the connection
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    result = sock.connect_ex((url, port))
    if result == 0:
        print("Server is up and running")
        return
    else:
        # Create log file
        time = datetime.now().strftime("%Y-%m-%d-%H-%M-%S")
        logFile = "vesta-logs/{0}.log".format(time)
        logging.basicConfig(filename=logFile,
                    filemode='a',
                    format='%(asctime)s %(name)s %(levelname)s %(message)s',
                    datefmt='%H:%M:%S',
                    level=logging.DEBUG)
        logging.error("Could not reach server. Started logging file")
        logging.warn("Tried to ping {0} on port {1}".format(url, port))
        logging.info("Sending an email")
        # If no host was passed, set the url as the host.
        if host == None:
            host = url
        # Send email
        SendEmail.sendMail(url, time, host, port)
        # TODO Send wake on lan packet to URL to turn it on again