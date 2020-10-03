#!/usr/bin/env python
import os
import platform

import createPath
import getClipBoardWindows
import makeWord
import getClipBoardMac
import getClipBoardLinux


def runProgram():
    #Get Current platform 
    current_platform = str(platform.system())



    # Path for word docx
    while not os.path.exists("path.txt"):
        createPath.makePath()

    path = createPath.openPath()

    if len(path) == 0:
        path = input("Input your desired path for your word file: ")
        createPath.updatePath(path)

    if "Mac" in current_platform:
        clipData = getClipBoardMac.getClipboardData()
        clipData = clipData.decode('UTF-8')
    elif "Windows" in current_platform:
        # Get special characters e.g. æ,ø,å 
        clipData = str(getClipBoardWindows.get_clipboard_text())
        clipData = clipData.encode('UTF-8')
        clipData = clipData.decode('unicode-escape')
        clipDataList = clipData.split("'")
        clipData = clipDataList[1]

    elif "Linux" in current_platform:
        clipData = getClipBoardLinux.getClipboardData()
        clipData = clipData.decode('UTF-8')
        
    

    # Runs the makeWord script
    makeWord.makeWordFile(path, clipData)
