import os
from datetime import datetime
from os import walk

def checkLogs():
    """Checks the folder containing the logs
    
    This method checks the folder containing the logs. If the folder has a logfile that was created
    withing the last 30 minutes, then the function returns true.

    """

    TIMEOUT = 30 * 60 # If a log was made in the last 30 minutes, do not try again.

    for (dirname, dirs, files) in walk(os.path.join("vesta-logs") ):
        for filename in files:
            timestamp = filename.split('.')[0]
            pastDate = datetime.strptime(timestamp, "%Y-%m-%d-%H-%M-%S")
            diff = datetime.now() - pastDate
            if (diff.seconds <= (TIMEOUT)):
                print("Failed log found that was made less than 30 minutes ago. Preventing further execution.")
                return True