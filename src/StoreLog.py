import os
import sys
import shutil
import datetime

def storeLog(time):
    """Copy's the Hades rsyslog file to the log folder

    Although the rsyslog server already stores the log of the Hades server off-site, 
    this method copies the log file over to the vesta-logs folder to have them in
    one place. It also makes debugging easier since the vesta-logs folder contains
    the log until the server went down.

    TODO maybe delete the old rsyslog file to save space. Not sure yet if and how.
    """
    srcDir = os.getcwd() + os.path.normpath('/Hades/HadesLog.log')
    dstDir = os.getcwd() + os.path.normpath('/vesta-logs/'+ time +'-HadesLog.log')
    # Copy the file to the vesta-log folder
    shutil.copy(srcDir, dstDir)
    # Set the permissions
    os.chmod(dstDir, 0o444)