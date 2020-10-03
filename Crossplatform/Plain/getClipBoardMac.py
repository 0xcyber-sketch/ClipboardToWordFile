"""
Copy clipbosrd on Mac devices. Requirement pbpaste and pbcopy. 
Author: https://stackoverflow.com/questions/43860227/python-getting-and-setting-clipboard-data-with-subprocesses 
"""

import subprocess


def getClipboardData():
    p = subprocess.Popen(['pbpaste'], stdout=subprocess.PIPE)
    retcode = p.wait()
    data = p.stdout.read()
    return data

