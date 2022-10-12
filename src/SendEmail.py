import smtplib, ssl
from src import credentials
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def sendMail(url, time, host, port):

    port = credentials.port  # For SSL
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

    This is an automated email by Mercury informing you that Hades is down.
    
    The following details are linked to the failed connection request:
    Time of ping:&nbsp;&nbsp;&nbsp;&nbsp;{1}
    Hostname:&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;{2}
    Port:&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;{3}

    For the full log and subsequent reports please check the log folder.

    Kind regards,

    The Mercury system.

    """
    html = """\
    <html>
    <body>
        <p>Hi,<br><br>
        This is an automated email by Mercury informing you that <a href="https://{0}">Hades</a> is down.<br>
        <br>
        The following details are linked to the failed connection request: <br>
        Time of ping:&nbsp;&nbsp;&nbsp;&nbsp;{1}<br>
        Hostname:&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;{2}<br>
        Port:&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;{3}<br>
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
    part1 = MIMEText(text.format(url, time, host, port), "plain")
    part2 = MIMEText(html.format(url, time, host, port), "html")

    # Add HTML/plain-text parts to MIMEMultipart message
    # The email client will try to render the last part first
    message.attach(part1)
    message.attach(part2)


    # Create a secure SSL context
    context = ssl.create_default_context()

    # Try to log in to server and send email
    try:
        print("connecting to SMTP server")
        server = smtplib.SMTP(smtp_server,port)
        print("securing connection")
        server.starttls(context=context) # Secure the connection
        print("logging in")
        server.login(sender_email, password)
        print("sending email")
        server.sendmail(sender_email, receiver_email, message.as_string())
    except Exception as e:
        # Print any error messages to stdout
        print(e)
    finally:
        server.quit() 