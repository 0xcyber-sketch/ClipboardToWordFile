#!/usr/bin/env python
import os

import createLog
import getClipboard
import makeWord


def runProgram():
    # Path for word docx
    while not os.path.exists("path.txt"):
        createLog.makeLog()

    path = createLog.openLog()

    if len(path) == 0:
        path = input("Input your desired path for your word file: ")
        createLog.updateLog(path)

     # Get special characters e.g. æ,ø,å 
    clipData = str(getClipboard.get_clipboard_text())
    clipData = clipData.encode('UTF-8')
    clipData = clipData.decode('unicode-escape')

    # Format clipdata
    clipDataList = clipData.split("'")
    clipData = clipDataList[1]

    # Runs the makeWord script
    makeWord.makeWordFile(path, clipData)
