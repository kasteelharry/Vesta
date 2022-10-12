# Vesta

This repository is home of Vesta, the software packet build for Mercurius (my Raspberry Pi). It currently contains a script that keeps track of Hades (my server) being online and reachable on a set port. In the event my Hades is unreachable, this script will send an email to my personal email address to warn me that the server is unreachable.

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
    ```

3. Setup a cronjob that executes at the maximum each 15 minutes.
4. Enjoy the emails when the server is down

## Usage

The main module has the following usage:

```bash
python Vesta.py <Server address> <Port to ping> [<URL of the admin dashboard>]
```
