# Vesta

This repository is home of Vesta, the software packet build for Mercurius (my Raspberry Pi). It currently contains a script that keeps track of Hades (my server) being online and reachable on a set port. In the event my Hades is unreachable, this script will send an email to my personal email address to warn me that the server is unreachable.

Once the server is down and the mail has been send, the script will try to send a Wake-On-LAN (WOL) packet to the mac address of the server. It is therefore important that the server is on the same LAN network as the machine that runs this script.

## Installation

1. Clone the repository to your machine of choice.
2. Create a ``credentials.py`` file in the root folder of this project with the following:

    ```python
    username = EMAIL_YOU_WANT_TO_SMTP_INTO
    password = PASSWORD_OF_YOUR_EMAIL_ACCOUNT
    receiver = EMAIL_THAT_RECEIVES_THE_WARNING
    smtpServer = SMTP_SERVER_HOSTNAME
    port = SMTP_HOST_PORT
    subject = EMAIL_SUBJECT
    MAC_ADDRESS = SERVER_MAC_ADDRESS
    ```

3. Setup a cronjob that executes at the maximum each 15 minutes.
4. Enjoy the emails when the server is down

## Usage

The main module has the following usage:

```bash
sudo python Vesta.py <Server address> <Port to ping> [<URL of the admin dashboard>]
```
