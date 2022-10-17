import os
from datetime import datetime
from os import walk

def checkLogs():
    """Checks the folder containing the logs
    
    This method checks the folder containing the logs. If the folder has a logfile that was created
    withing the last hour, then the function returns true.

    """

    TIMEOUT = 60 * 60 * 1 # If a log was made in the last hour, do not try again.
    HOUR_MIN = 7
    HOUR_MAX = 21

    for (dirname, dirs, files) in walk(os.path.join("vesta-logs") ):
        for filename in files:
            timestamp = filename.split('.')[0]
            try:
                pastDate = datetime.strptime(timestamp, "%Y-%m-%d-%H-%M-%S")
                currentDate = datetime.now()
                diff = currentDate - pastDate
                # If the difference is smaller than the timeout and within the same day then do not check
                # the server for still being up. Since we can assume that the owner might not have fixed it in 10 minutes
                if (diff.seconds <= (TIMEOUT) and diff.days == 0):
                    print("Failed log found that was made less than 30 minutes ago. Preventing further execution.")
                    return True
                # If the check is done in the night (between 21:00 and 7:00) and there is a log file made in the same time
                # period then do not check the server because we are assuming that the owner is sleeping.
                # If no log is made in the night then go and check the server.
                elif not (HOUR_MAX > currentDate.hour > HOUR_MIN) and (diff.days <= 0) and not (HOUR_MAX > pastDate.hour > HOUR_MIN):
                    print("Inside night time mode and a log was found in that period")
                    return True
            except ValueError as err:
                print("Skipping file with non-timestamp name.")
                continue