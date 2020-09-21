#!/usr/bin/env python
import os

import createPath
import getClipboard
import makeWord


def runProgram():
    # Path for word docx
    while not os.path.exists("path.txt"):
        createPath.makePath()

    path = createPath.openPath()

    if len(path) == 0:
        path = input("Input your desired path for your word file: ")
        createPath.updatePath(path)

    clipData = str(getClipboard.get_clipboard_text())

    # Format clipdata
    clipDataList = clipData.split("'")
    clipData = clipDataList[1]

    # Runs the makeWord script
    makeWord.makeWordFile(path, clipData)
