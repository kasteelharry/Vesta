import socket
import sys
from src import SendEmail
from datetime import datetime
import logging
import urllib.request

def pingServer(url, port, host=None):
    """Pings the server and send an email if unreachable.
    
    This method pings the url and port passed as parameters. If the
    url and port are unreachable, the method will call SendEmail to
    send an email to the owner to inform them that the server is
    offline.
    """
    # Get the IP of the machine that tried to connect to the server.
    publicIP = urllib.request.urlopen('https://checkip.amazonaws.com').read().decode('utf8')
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
        logging.warn("Tried to ping {0} on port {1} from {2}".format(url, port, publicIP))
        logging.info("Sending an email")

        # If no host was passed, set the url as the host.
        if host == None:
            host = url

        # Send email
        try:

            SendEmail.sendMail(url, time, host, port, publicIP)
        except Exception as e:
            logging.error("Could not send email, check the line below")
            logging.warn(e)
            print("Please check the logs")
        # TODO Send wake on lan packet to URL to turn it on again