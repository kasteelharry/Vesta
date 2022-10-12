import smtplib, ssl
import credentials
import logging
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def sendMail(url, time, host, port, machineIP):
    """Sends an email
    
    This method sends an email to the email account that is defined in the
    credentials.py file.

    """

    portSSL = credentials.port  # For SSL
    password = credentials.password
    sender_email = credentials.username
    smtp_server = credentials.smtpServer
    receiver_email = credentials.receiver
    message = MIMEMultipart("alternative")
    message["Subject"] = credentials.subject
    message["From"] = sender_email
    message["To"] = receiver_email

    # Create the plain-text and HTML version of your message
    text = """\
    Hi,

    This is an automated email by Mercurius informing you that Hades is down.
    
    The following details are linked to the failed connection request:
    Run by: &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;{1}
    Time of ping:&nbsp;&nbsp;&nbsp;&nbsp;{2}
    Hostname:&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;{3}
    Port:&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;{4}

    For the full log and subsequent reports please check the log folder.

    Kind regards,

    The Mercury system.

    """
    html = """\
    <html>
    <body>
        <p>Hi,<br><br>
        This is an automated email by Mercurius informing you that <a href="https://{0}">Hades</a> is down.<br>
        <br>
        The following details are linked to the failed connection request: <br>
        Run by: &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;{1}<br>
        Time of ping:&nbsp;&nbsp;&nbsp;&nbsp;{2}<br>
        Hostname:&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;{3}<br>
        Port:&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;{4}<br>
        <br>
        For the full log and subsequent reports please check the log folder.<br>
        <br>
        Kind regards,<br>
        <br>
        The Mercury system.
        </p>
    </body>
    </html>
    """

    # Turn these into plain/html MIMEText objects
    part1 = MIMEText(text.format(host, machineIP, time, url, port), "plain")
    part2 = MIMEText(html.format(host, machineIP, time, url, port, machineIP), "html")

    # Add HTML/plain-text parts to MIMEMultipart message
    # The email client will try to render the last part first
    message.attach(part1)
    message.attach(part2)


    # Create a secure SSL context
    context = ssl.create_default_context()

    # Try to log in to server and send email
    try:
        logging.info("connecting to SMTP server.")
        server = smtplib.SMTP(smtp_server,portSSL)
        logging.info("securing connection.")
        server.starttls(context=context) # Secure the connection
        logging.info("logging in.")
        server.login(sender_email, password)
        logging.info("sending email.")
        server.sendmail(sender_email, receiver_email, message.as_string())
        logging.info("Email has been sent.")
    except Exception as e:
        # Print any error messages to stdout
        logging.warn("Was unable to send the email, check the stacktrace below.")
        logging.error(e)
    finally:
        logging.info("Closing the SMTP server")
        server.quit()